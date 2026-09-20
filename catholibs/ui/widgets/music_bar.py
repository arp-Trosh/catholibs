from textual.app import ComposeResult
from textual.containers import Horizontal
from textual.widgets import Button, Static

_METER_SEGMENTS = 10
_TRACK_BOX_WIDTH = 18
_TRACK_SEPARATOR = "   -   "
_SCROLL_INTERVAL = 0.3


class MusicBar(Horizontal):
    """Always-visible top-left widget: mute toggle, volume meter/controls,
    scrolling current-track name, and previous/next track buttons."""

    def compose(self) -> ComposeResult:
        yield Button("\U0001f50a", id="music-mute-btn", classes="music-btn")
        yield Static("", id="music-meter")
        yield Button("-", id="music-vol-down-btn", classes="music-btn")
        yield Button("+", id="music-vol-up-btn", classes="music-btn")
        yield Button("⏮", id="music-prev-btn", classes="music-btn")
        yield Static("", id="music-track")
        yield Button("⏭", id="music-next-btn", classes="music-btn")

    def on_mount(self) -> None:
        self._track_name = ""
        self._scroll_pos = 0
        self._refresh()
        self.set_interval(_SCROLL_INTERVAL, self._tick)

    def _refresh(self) -> None:
        music = self.app.music  # type: ignore[attr-defined]
        mute_btn = self.query_one("#music-mute-btn", Button)
        meter = self.query_one("#music-meter", Static)
        prev_btn = self.query_one("#music-prev-btn", Button)
        next_btn = self.query_one("#music-next-btn", Button)
        if not music.available:
            mute_btn.label = "\U0001f507"
            meter.update("[dim]no audio[/dim]")
            prev_btn.disabled = True
            next_btn.disabled = True
            self.query_one("#music-track", Static).update("")
            return
        mute_btn.label = "\U0001f507" if music.muted else "\U0001f50a"
        filled = round(music.volume / 100 * _METER_SEGMENTS)
        bar = "█" * filled + "░" * (_METER_SEGMENTS - filled)
        pct = 0 if music.muted else music.volume
        meter.update(f"[gold3]{bar}[/gold3] {pct:>3d}%")
        prev_btn.disabled = False
        next_btn.disabled = False
        self._sync_track_name(music.current_track_name)

    def _sync_track_name(self, name: str) -> None:
        if name != self._track_name:
            self._track_name = name
            self._scroll_pos = 0
        self._render_track()

    def _render_track(self) -> None:
        track = self.query_one("#music-track", Static)
        name = self._track_name
        if not name:
            track.update("")
            return
        if len(name) <= _TRACK_BOX_WIDTH:
            track.update(f"[gold3]{name.center(_TRACK_BOX_WIDTH)}[/gold3]")
            return
        loop = name + _TRACK_SEPARATOR
        window = (loop * 2)[self._scroll_pos : self._scroll_pos + _TRACK_BOX_WIDTH]
        track.update(f"[gold3]{window}[/gold3]")

    def _tick(self) -> None:
        music = self.app.music  # type: ignore[attr-defined]
        if not music.available:
            return
        if music.current_track_name != self._track_name:
            self._sync_track_name(music.current_track_name)
            return
        if len(self._track_name) > _TRACK_BOX_WIDTH:
            loop_len = len(self._track_name) + len(_TRACK_SEPARATOR)
            self._scroll_pos = (self._scroll_pos + 1) % loop_len
        self._render_track()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        music = self.app.music  # type: ignore[attr-defined]
        if not music.available:
            event.stop()
            return
        if event.button.id == "music-mute-btn":
            music.toggle_mute()
        elif event.button.id == "music-vol-down-btn":
            music.change_volume(-10)
        elif event.button.id == "music-vol-up-btn":
            music.change_volume(10)
        elif event.button.id == "music-prev-btn":
            music.previous_track()
        elif event.button.id == "music-next-btn":
            music.next_track()
        else:
            return
        self._refresh()
        event.stop()
