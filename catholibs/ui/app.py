from textual.app import App

from .screens.title import TitleScreen


class CatholibsApp(App):
    """Catholibs: the Catholic-inspired Mad-Libs TUI game."""

    CSS_PATH = "app.tcss"
    TITLE = "Catholibs"

    def on_mount(self) -> None:
        self.push_screen(TitleScreen())
