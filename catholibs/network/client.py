"""Asyncio TCP client used by every Catholibs player, including the host
(the host connects to its own locally-bound server over loopback)."""
from __future__ import annotations

import asyncio
from typing import Callable

from .protocol import encode, read_message

MessageHandler = Callable[[dict], None]


class GameClient:
    def __init__(self, on_message: MessageHandler) -> None:
        self.on_message = on_message
        self.reader: asyncio.StreamReader | None = None
        self.writer: asyncio.StreamWriter | None = None
        self.player_id: int | None = None
        self.is_host: bool = False
        self.connected: bool = False
        self._listen_task: asyncio.Task | None = None

    async def connect(self, host: str, port: int, name: str, timeout: float = 5.0) -> None:
        self.reader, self.writer = await asyncio.wait_for(
            asyncio.open_connection(host, port), timeout=timeout
        )
        await self._send({"type": "hello", "name": name})
        msg = await asyncio.wait_for(read_message(self.reader), timeout=timeout)
        if not msg:
            raise ConnectionError("Server closed the connection.")
        if msg.get("type") == "error":
            raise ConnectionError(msg.get("message", "Could not join the game."))
        if msg.get("type") != "welcome":
            raise ConnectionError("Unexpected response from server.")
        self.player_id = msg["player_id"]
        self.is_host = bool(msg["is_host"])
        self.connected = True
        self._listen_task = asyncio.create_task(self._listen())

    async def _listen(self) -> None:
        try:
            while True:
                msg = await read_message(self.reader)
                if msg is None:
                    break
                if msg.get("type") == "promoted_host":
                    self.is_host = True
                self.on_message(msg)
        except (ConnectionResetError, asyncio.IncompleteReadError):
            pass
        finally:
            self.connected = False
            self.on_message({"type": "disconnected"})

    async def _send(self, msg: dict) -> None:
        assert self.writer is not None
        self.writer.write(encode(msg))
        await self.writer.drain()

    async def send_chat(self, text: str) -> None:
        await self._send({"type": "chat", "text": text})

    async def send_begin(self, prayer_id: str | None = None) -> None:
        msg = {"type": "begin_game"}
        if prayer_id:
            msg["prayer_id"] = prayer_id
        await self._send(msg)

    async def send_end(self) -> None:
        await self._send({"type": "end_game"})

    async def send_restart(self, prayer_id: str | None = None) -> None:
        msg = {"type": "restart_game"}
        if prayer_id:
            msg["prayer_id"] = prayer_id
        await self._send(msg)

    async def send_answer(self, blank_index: int, text: str) -> None:
        await self._send({"type": "answer", "blank_index": blank_index, "text": text})

    def close(self) -> None:
        if self._listen_task is not None:
            self._listen_task.cancel()
        if self.writer is not None:
            self.writer.close()
