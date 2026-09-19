from textual.app import ComposeResult
from textual.binding import Binding
from textual.containers import Center, Middle, Vertical
from textual.screen import Screen
from textual.widgets import Button, Footer, Static


class MultiplayerMenuScreen(Screen):
    """Choose to Host a new game or Join an existing one."""

    BINDINGS = [
        Binding("h", "host", "Host"),
        Binding("j", "join", "Join"),
        Binding("escape", "go_back", "Main Menu"),
    ]

    def compose(self) -> ComposeResult:
        with Middle():
            with Center():
                with Vertical(id="title-box"):
                    yield Static("[bold gold3]Multiplayer[/bold gold3]")
                    yield Static(
                        "Old-school net-play: one of you Hosts, up to 7 others Join.\n",
                        id="mp-subheading",
                    )
                    yield Button("Host a Game  [h]", id="host-btn", variant="primary")
                    yield Button("Join a Game  [j]", id="join-btn", variant="primary")
                    yield Button("Back  [esc]", id="back-btn")
        yield Footer()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "host-btn":
            self.action_host()
        elif event.button.id == "join-btn":
            self.action_join()
        elif event.button.id == "back-btn":
            self.action_go_back()

    def action_host(self) -> None:
        from .host_setup import HostSetupScreen

        self.app.push_screen(HostSetupScreen())

    def action_join(self) -> None:
        from .join_setup import JoinSetupScreen

        self.app.push_screen(JoinSetupScreen())

    def action_go_back(self) -> None:
        self.app.pop_screen()
