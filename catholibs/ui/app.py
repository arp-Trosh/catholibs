from textual.app import App

from ..audio import MusicPlayer
from .screens.title import TitleScreen


class CatholibsApp(App):
    """Catholibs: the Catholic-inspired Mad-Libs TUI game."""

    CSS_PATH = "app.tcss"
    TITLE = "Catholibs"

    def __init__(self) -> None:
        super().__init__()
        self.music = MusicPlayer()

    def on_mount(self) -> None:
        self.music.start()
        self.push_screen(TitleScreen())
