from textual.app import ComposeResult
from textual.binding import Binding
from textual.containers import Center, Middle, Vertical
from textual.screen import Screen
from textual.widgets import Button, Footer, Input, Static

from ..widgets.music_bar import MusicBar

DEFAULT_PORT = 5555


class JoinSetupScreen(Screen):
    """Collects a name + server address, then connects and enters the lobby."""

    BINDINGS = [
        Binding("escape", "go_back", "Back"),
    ]

    def compose(self) -> ComposeResult:
        yield MusicBar()
        with Middle():
            with Center():
                with Vertical(id="title-box"):
                    yield Static("[bold gold3]Join a Game[/bold gold3]")
                    yield Input(placeholder="Your name", id="name-input", value="Player")
                    yield Input(placeholder="Server IP address (e.g. 192.168.1.5)", id="ip-input")
                    yield Input(placeholder=f"Port (default {DEFAULT_PORT})", id="port-input")
                    yield Static("", id="error-msg")
                    yield Button("Join  [Enter]", id="join-btn", variant="primary")
                    yield Button("Back  [esc]", id="back-btn")
        yield Footer()

    def on_input_submitted(self, event: Input.Submitted) -> None:
        self._join()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "join-btn":
            self._join()
        elif event.button.id == "back-btn":
            self.action_go_back()

    def _join(self) -> None:
        name = self.query_one("#name-input", Input).value.strip() or "Player"
        host = self.query_one("#ip-input", Input).value.strip()
        port_text = self.query_one("#port-input", Input).value.strip()

        if not host:
            self.query_one("#error-msg", Static).update("[red]Please enter a server IP address.[/red]")
            return

        port = DEFAULT_PORT
        if port_text:
            try:
                port = int(port_text)
                if not (1 <= port <= 65535):
                    raise ValueError
            except ValueError:
                self.query_one("#error-msg", Static).update("[red]Please enter a valid port number (1-65535).[/red]")
                return

        from .multiplayer_game import MultiplayerGameScreen

        self.app.push_screen(MultiplayerGameScreen(role="join", name=name, address=host, port=port))

    def action_go_back(self) -> None:
        self.app.pop_screen()
