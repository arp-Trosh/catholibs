from textual.app import ComposeResult
from textual.containers import Horizontal
from textual.widgets import Button, Static

_METER_SEGMENTS = 10


class MusicBar(Horizontal):
    """Always-visible top-left widget: mute toggle + volume meter/controls."""

    def compose(self) -> ComposeResult:
        yield Button("\U0001f50a", id="music-mute-btn", classes="music-btn")
        yield Static("", id="music-meter")
        yield Button("-", id="music-vol-down-btn", classes="music-btn")
        yield Button("+", id="music-vol-up-btn", classes="music-btn")

    def on_mount(self) -> None:
        self._refresh()

    def _refresh(self) -> None:
        music = self.app.music  # type: ignore[attr-defined]
        mute_btn = self.query_one("#music-mute-btn", Button)
        meter = self.query_one("#music-meter", Static)
        if not music.available:
            mute_btn.label = "\U0001f507"
            meter.update("[dim]no audio[/dim]")
            return
        mute_btn.label = "\U0001f507" if music.muted else "\U0001f50a"
        filled = round(music.volume / 100 * _METER_SEGMENTS)
        bar = "█" * filled + "░" * (_METER_SEGMENTS - filled)
        pct = 0 if music.muted else music.volume
        meter.update(f"[gold3]{bar}[/gold3] {pct:>3d}%")

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
        else:
            return
        self._refresh()
        event.stop()
