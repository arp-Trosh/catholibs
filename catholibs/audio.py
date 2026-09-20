"""Background music: loops the bundled tracks through an external ``mpv``
process, controlled at runtime over mpv's JSON IPC socket.

mpv (rather than a Python audio library) keeps this dependency-free -- the
game only shells out to a binary that either exists on the host or doesn't.
When it's missing, ``MusicPlayer.available`` is False and every call becomes
a no-op, so the game still runs without sound.
"""
from __future__ import annotations

import atexit
import json
import random
import shutil
import socket
import subprocess
import tempfile
import time
import uuid
from pathlib import Path

MUSIC_DIR = Path(__file__).with_name("assets") / "music"
DEFAULT_VOLUME = 50


class MusicPlayer:
    """Owns the mpv subprocess that loops the background music playlist."""

    def __init__(self) -> None:
        self.volume: int = DEFAULT_VOLUME
        self.muted: bool = False
        self.available: bool = shutil.which("mpv") is not None
        self._process: subprocess.Popen | None = None
        self._socket_path = Path(tempfile.gettempdir()) / f"catholibs-mpv-{uuid.uuid4().hex}.sock"

    def start(self) -> None:
        """Launch mpv looping all bundled tracks in shuffled order."""
        if not self.available:
            return
        tracks = sorted(str(p) for p in MUSIC_DIR.glob("*.mp4"))
        if not tracks:
            self.available = False
            return
        random.shuffle(tracks)
        try:
            self._process = subprocess.Popen(
                [
                    "mpv",
                    "--no-video",
                    "--no-terminal",
                    "--loop-playlist=inf",
                    f"--volume={self.volume}",
                    f"--input-ipc-server={self._socket_path}",
                    *tracks,
                ],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )
        except OSError:
            self.available = False
            return
        atexit.register(self._shutdown)

    def set_volume(self, volume: int) -> None:
        self.volume = max(0, min(100, volume))
        self._send(["set_property", "volume", self.volume])

    def change_volume(self, delta: int) -> None:
        self.set_volume(self.volume + delta)

    def toggle_mute(self) -> None:
        self.muted = not self.muted
        self._send(["set_property", "mute", self.muted])

    def _send(self, command: list) -> None:
        if not self.available:
            return
        payload = json.dumps({"command": command}).encode() + b"\n"
        # mpv needs a beat after launch to create the socket file; a couple
        # of quick retries covers a command sent right after startup.
        for attempt in range(3):
            try:
                with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as sock:
                    sock.settimeout(0.3)
                    sock.connect(str(self._socket_path))
                    sock.sendall(payload)
                return
            except OSError:
                if attempt == 2:
                    return
                time.sleep(0.05)

    def _shutdown(self) -> None:
        if self._process and self._process.poll() is None:
            self._process.terminate()
            try:
                self._process.wait(timeout=2)
            except subprocess.TimeoutExpired:
                self._process.kill()
        self._socket_path.unlink(missing_ok=True)
