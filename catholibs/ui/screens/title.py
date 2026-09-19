from textual.app import ComposeResult
from textual.binding import Binding
from textual.containers import Center, Middle, Vertical
from textual.screen import Screen
from textual.widgets import Button, Footer, Static


class TitleScreen(Screen):
    """The main menu: pick Single Player or Multiplayer."""

    BINDINGS = [
        Binding("1", "single_player", "Single Player"),
        Binding("2", "multiplayer", "Multiplayer"),
        Binding("q", "quit", "Quit"),
    ]

    def compose(self) -> ComposeResult:
        with Middle():
            with Center():
                with Vertical(id="title-box"):
                    yield Static(
                        "[bold gold3]☩ C A T H O L I B S ☩[/bold gold3]",
                        id="title-heading",
                    )
                    yield Static(
                        "[italic]the Catholic-inspired Mad-Libs game[/italic]\n"
                        "for Saints and Sinners!",
                        id="title-subheading",
                    )
                    yield Button("Single Player  [1]", id="single-player-btn", variant="primary")
                    yield Button("Multiplayer  [2]", id="multiplayer-btn", variant="primary")
                    yield Button("Quit  [q]", id="quit-btn")
        yield Footer()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "single-player-btn":
            self.action_single_player()
        elif event.button.id == "multiplayer-btn":
            self.action_multiplayer()
        elif event.button.id == "quit-btn":
            self.action_quit()

    def action_single_player(self) -> None:
        from .single_player import SinglePlayerScreen

        self.app.push_screen(SinglePlayerScreen())

    def action_multiplayer(self) -> None:
        from .multiplayer_menu import MultiplayerMenuScreen

        self.app.push_screen(MultiplayerMenuScreen())

    def action_quit(self) -> None:
        self.app.exit()
