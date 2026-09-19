"""Asyncio TCP server hosting a Catholibs multiplayer game (up to 8 players).

Turn order is fixed when the host clicks Begin. Players answer their blank
in turn; everyone else only learns the requested word-type, never the actual
word, until the final reveal.
"""
from __future__ import annotations

import asyncio
import random
from dataclasses import dataclass

from ..mad_lib import MadLib, build_mad_lib
from ..prayers_data import PRAYERS, Prayer, get_prayer
from .protocol import MAX_PLAYERS, encode, read_message


@dataclass
class Player:
    id: int
    name: str
    writer: asyncio.StreamWriter
    connected: bool = True


class GameServer:
    def __init__(self) -> None:
        self.players: dict[int, Player] = {}
        self._next_id = 0
        self.host_id: int | None = None
        self.mad_lib: MadLib | None = None
        self.turn_order: list[int] = []
        self.current_turn_pos: int = 0
        self.phase: str = "lobby"  # lobby | playing | reveal
        self._server: asyncio.base_events.Server | None = None

    async def start(self, port: int) -> None:
        self._server = await asyncio.start_server(self._handle_client, "0.0.0.0", port)

    def stop(self) -> None:
        if self._server is not None:
            self._server.close()
        for player in self.players.values():
            player.writer.close()

    # -- connection lifecycle -------------------------------------------------

    async def _handle_client(self, reader: asyncio.StreamReader, writer: asyncio.StreamWriter) -> None:
        try:
            hello = await read_message(reader)
        except Exception:
            hello = None
        if not hello or hello.get("type") != "hello":
            writer.close()
            return

        name = str(hello.get("name") or "Player").strip()[:20] or "Player"
        if len(self.players) >= MAX_PLAYERS:
            await self._send(writer, {"type": "error", "message": "Server is full (8 players max)."})
            writer.close()
            return

        player_id = self._next_id
        self._next_id += 1
        is_host = self.host_id is None
        if is_host:
            self.host_id = player_id
        player = Player(id=player_id, name=name, writer=writer)
        self.players[player_id] = player

        await self._send(writer, {"type": "welcome", "player_id": player_id, "is_host": is_host})
        await self._broadcast_player_list()
        await self._broadcast_system(f"{name} joined the game.")

        try:
            while True:
                msg = await read_message(reader)
                if msg is None:
                    break
                await self._handle_message(player, msg)
        except (ConnectionResetError, asyncio.IncompleteReadError):
            pass
        finally:
            await self._on_disconnect(player)

    async def _on_disconnect(self, player: Player) -> None:
        player.connected = False
        self.players.pop(player.id, None)
        await self._broadcast_system(f"{player.name} left the game.")
        await self._broadcast_player_list()
        if player.id == self.host_id:
            self.host_id = next(iter(self.players), None)
            if self.host_id is not None:
                await self._send(self.players[self.host_id].writer, {"type": "promoted_host"})
        if self.phase == "playing":
            await self._prompt_next_turn()
        player.writer.close()

    # -- message handling -------------------------------------------------------

    async def _handle_message(self, player: Player, msg: dict) -> None:
        kind = msg.get("type")
        if kind == "chat":
            text = str(msg.get("text", "")).strip()[:500]
            if text:
                await self._broadcast({"type": "chat", "from": player.name, "text": text})
        elif kind == "begin_game" and player.id == self.host_id and self.phase == "lobby":
            await self._begin_game(msg.get("prayer_id"))
        elif kind == "answer" and self.phase == "playing":
            await self._handle_answer(player, msg)
        elif kind == "end_game" and player.id == self.host_id:
            await self._end_game()
        elif kind == "restart_game" and player.id == self.host_id:
            await self._begin_game(msg.get("prayer_id"))

    # -- game flow ----------------------------------------------------------

    def _pick_prayer(self, prayer_id: str | None) -> Prayer:
        if prayer_id:
            try:
                return get_prayer(prayer_id)
            except KeyError:
                pass
        return random.choice(PRAYERS)

    async def _begin_game(self, prayer_id: str | None) -> None:
        if not self.players:
            return
        prayer = self._pick_prayer(prayer_id)
        self.mad_lib = build_mad_lib(prayer)
        self.turn_order = list(self.players.keys())
        self.current_turn_pos = 0
        self.phase = "playing"
        await self._broadcast({
            "type": "game_started",
            "prayer_title": prayer.title,
            "total_blanks": self.mad_lib.total_blanks,
            "turn_order": [self.players[pid].name for pid in self.turn_order if pid in self.players],
        })
        await self._prompt_next_turn()

    async def _prompt_next_turn(self) -> None:
        if self.mad_lib is None:
            return
        order = self.mad_lib.blank_order
        player = None
        while self.current_turn_pos < len(order):
            player_id = self.turn_order[self.current_turn_pos % len(self.turn_order)]
            player = self.players.get(player_id)
            if player is None or not player.connected:
                blank_index = order[self.current_turn_pos]
                self.mad_lib.set_answer(blank_index, "(absent)", answered_by="(disconnected)")
                self.current_turn_pos += 1
                player = None
                continue
            break
        if player is None:
            await self._reveal()
            return

        blank = self.mad_lib.blanks[order[self.current_turn_pos]]
        blank_number = self.current_turn_pos + 1
        total = len(order)
        await self._send(player.writer, {
            "type": "your_turn",
            "blank_index": blank.index,
            "category": blank.category.name,
            "prompt": blank.category.prompt,
            "blank_number": blank_number,
            "total_blanks": total,
        })
        await self._broadcast(
            {
                "type": "waiting_on",
                "player_name": player.name,
                "prompt": blank.category.prompt,
                "blank_number": blank_number,
                "total_blanks": total,
            },
            exclude={player.id},
        )

    async def _handle_answer(self, player: Player, msg: dict) -> None:
        if self.mad_lib is None:
            return
        order = self.mad_lib.blank_order
        if self.current_turn_pos >= len(order):
            return
        expected_id = self.turn_order[self.current_turn_pos % len(self.turn_order)]
        if player.id != expected_id:
            return
        blank_index = order[self.current_turn_pos]
        if msg.get("blank_index") != blank_index:
            return
        text = str(msg.get("text", "")).strip()[:60] or "..."
        self.mad_lib.set_answer(blank_index, text, answered_by=player.name)
        self.current_turn_pos += 1
        await self._prompt_next_turn()

    async def _reveal(self) -> None:
        if self.mad_lib is None:
            return
        self.phase = "reveal"
        await self._broadcast({
            "type": "reveal",
            "title": self.mad_lib.prayer.title,
            "text": self.mad_lib.render_rich(),
        })

    async def _end_game(self) -> None:
        self.phase = "lobby"
        self.mad_lib = None
        await self._broadcast({"type": "game_ended"})

    # -- low-level send helpers ----------------------------------------------

    async def _send(self, writer: asyncio.StreamWriter, msg: dict) -> None:
        try:
            writer.write(encode(msg))
            await writer.drain()
        except (ConnectionResetError, BrokenPipeError):
            pass

    async def _broadcast(self, msg: dict, exclude: set[int] | None = None) -> None:
        exclude = exclude or set()
        for pid, player in list(self.players.items()):
            if pid in exclude:
                continue
            await self._send(player.writer, msg)

    async def _broadcast_system(self, text: str) -> None:
        await self._broadcast({"type": "chat", "from": "System", "text": text, "system": True})

    async def _broadcast_player_list(self) -> None:
        await self._broadcast({
            "type": "player_list",
            "players": [{"id": p.id, "name": p.name} for p in self.players.values()],
            "host_id": self.host_id,
        })
