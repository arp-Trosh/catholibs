from textual.app import ComposeResult
from textual.binding import Binding
from textual.containers import Center, Middle, Vertical
from textual.screen import Screen
from textual.widgets import Button, Footer, Input, Static

DEFAULT_PORT = 5555


class JoinSetupScreen(Screen):
    """Collects a name + server address, then connects and enters the lobby."""

    BINDINGS = [
        Binding("escape", "go_back", "Back"),
    ]

    def compose(self) -> ComposeResult:
        with Middle():
            with Center():
                with Vertical(id="title-box"):
                    yield Static("[bold gold3]Join a Game[/bold gold3]")
                    yield Input(placeholder="Your name", id="name-input", value="Player")
                    yield Input(placeholder=f"Server address (e.g. 192.168.1.5:{DEFAULT_PORT})", id="address-input")
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
        address_text = self.query_one("#address-input", Input).value.strip()
        if not address_text:
            self.query_one("#error-msg", Static).update("[red]Please enter a server address.[/red]")
            return

        if ":" in address_text:
            host, _, port_text = address_text.rpartition(":")
            try:
                port = int(port_text)
            except ValueError:
                self.query_one("#error-msg", Static).update("[red]Invalid port in address.[/red]")
                return
        else:
            host, port = address_text, DEFAULT_PORT

        if not host:
            self.query_one("#error-msg", Static).update("[red]Please enter a valid host.[/red]")
            return

        from .multiplayer_game import MultiplayerGameScreen

        self.app.push_screen(MultiplayerGameScreen(role="join", name=name, address=host, port=port))

    def action_go_back(self) -> None:
        self.app.pop_screen()
