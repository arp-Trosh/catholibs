"""Wire protocol for Catholibs multiplayer: newline-delimited JSON messages."""
from __future__ import annotations

import json
from typing import Any

MAX_PLAYERS = 8


def encode(message: dict[str, Any]) -> bytes:
    return (json.dumps(message) + "\n").encode("utf-8")


async def read_message(reader) -> dict[str, Any] | None:
    """Read one line-delimited JSON message. Returns None on disconnect."""
    line = await reader.readline()
    if not line:
        return None
    line = line.strip()
    if not line:
        return {}
    return json.loads(line.decode("utf-8"))
