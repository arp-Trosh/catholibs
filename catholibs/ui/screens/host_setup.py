import socket

from textual.app import ComposeResult
from textual.binding import Binding
from textual.containers import Center, Middle, Vertical
from textual.screen import Screen
from textual.widgets import Button, Footer, Input, Static

DEFAULT_PORT = 5555


def _local_ip() -> str:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except OSError:
        return "127.0.0.1"


class HostSetupScreen(Screen):
    """Collects a name + port, then starts a server and enters the lobby."""

    BINDINGS = [
        Binding("escape", "go_back", "Back"),
    ]

    def compose(self) -> ComposeResult:
        with Middle():
            with Center():
                with Vertical(id="title-box"):
                    yield Static("[bold gold3]Host a Game[/bold gold3]")
                    yield Static(f"Your network address: [bold]{_local_ip()}[/bold]\n(share it with your friends, together with the port below)")
                    yield Input(placeholder="Your name", id="name-input", value="Host")
                    yield Input(placeholder=f"Port (default {DEFAULT_PORT})", id="port-input")
                    yield Static("", id="error-msg")
                    yield Button("Start Hosting  [Enter]", id="start-btn", variant="primary")
                    yield Button("Back  [esc]", id="back-btn")
        yield Footer()

    def on_input_submitted(self, event: Input.Submitted) -> None:
        self._start()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "start-btn":
            self._start()
        elif event.button.id == "back-btn":
            self.action_go_back()

    def _start(self) -> None:
        name = self.query_one("#name-input", Input).value.strip() or "Host"
        port_text = self.query_one("#port-input", Input).value.strip()
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

        self.app.push_screen(MultiplayerGameScreen(role="host", name=name, port=port))

    def action_go_back(self) -> None:
        self.app.pop_screen()
