"""Background music: loops the bundled tracks through pygame's mixer.

pygame's wheels bundle their own copy of SDL2_mixer, so playback needs
nothing installed on the host beyond the project's normal ``pip install`` --
no external player binary, on any platform. When pygame (or its mixer)
isn't usable -- missing dependency, no audio device, etc. -- ``available``
is False and every call becomes a no-op, so the game still runs without
sound.
"""
from __future__ import annotations

import atexit
import random
import threading
from pathlib import Path

MUSIC_DIR = Path(__file__).with_name("assets") / "music"
DEFAULT_VOLUME = 50
_POLL_SECONDS = 0.2

try:
    import pygame
except ImportError:
    pygame = None


class MusicPlayer:
    """Owns a background thread that loops the bundled music playlist."""

    def __init__(self) -> None:
        self.volume: int = DEFAULT_VOLUME
        self.muted: bool = False
        self.available: bool = False
        self._tracks: list[str] = []
        self._thread: threading.Thread | None = None
        self._stop_event = threading.Event()

    def start(self) -> None:
        """Initialize the mixer and launch the playback thread."""
        if pygame is None:
            return
        self._tracks = sorted(str(p) for p in MUSIC_DIR.glob("*.ogg"))
        if not self._tracks:
            return
        try:
            pygame.mixer.init()
        except (pygame.error, NotImplementedError):
            return
        self.available = True
        self._apply_volume()
        self._thread = threading.Thread(target=self._run, daemon=True)
        self._thread.start()
        atexit.register(self._shutdown)

    def _run(self) -> None:
        playlist = list(self._tracks)
        random.shuffle(playlist)
        index = 0
        while not self._stop_event.is_set():
            if index >= len(playlist):
                random.shuffle(playlist)
                index = 0
            try:
                pygame.mixer.music.load(playlist[index])
                pygame.mixer.music.play()
            except pygame.error:
                return
            index += 1
            while pygame.mixer.music.get_busy() and not self._stop_event.is_set():
                self._stop_event.wait(_POLL_SECONDS)

    def set_volume(self, volume: int) -> None:
        self.volume = max(0, min(100, volume))
        self._apply_volume()

    def change_volume(self, delta: int) -> None:
        self.set_volume(self.volume + delta)

    def toggle_mute(self) -> None:
        self.muted = not self.muted
        self._apply_volume()

    def _apply_volume(self) -> None:
        if not self.available:
            return
        level = 0 if self.muted else self.volume
        pygame.mixer.music.set_volume(level / 100)

    def _shutdown(self) -> None:
        if not self.available:
            return
        self.available = False
        self._stop_event.set()
        pygame.mixer.music.stop()
        if self._thread is not None:
            self._thread.join(timeout=1)
        pygame.mixer.quit()
