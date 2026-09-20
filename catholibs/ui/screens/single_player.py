import random

from textual.app import ComposeResult
from textual.binding import Binding
from textual.containers import Container, Horizontal, VerticalScroll
from textual.screen import Screen
from textual.widgets import Button, Footer, Header, Input, ListItem, ListView, Static

from ...mad_lib import MadLib, build_mad_lib
from ...prayers_data import PRAYERS
from ..widgets.music_bar import MusicBar


class SinglePlayerScreen(Screen):
    """Solo Catholibs: pick a prayer, fill every blank yourself, see the result."""

    BINDINGS = [
        Binding("escape", "go_back", "Main Menu"),
        Binding("r", "replay", "Play Again", show=False),
        Binding("m", "main_menu", "Main Menu", show=False),
    ]

    def __init__(self) -> None:
        super().__init__()
        self.mad_lib: MadLib | None = None
        self.blank_positions: list[int] = []
        self.blank_cursor: int = 0
        self.phase: str = "select"

    def compose(self) -> ComposeResult:
        yield MusicBar()
        yield Header()
        with Container(id="game-panel"):
            yield VerticalScroll(id="game-scroll")
        yield Footer()

    async def on_mount(self) -> None:
        await self._show_prayer_picker()

    # -- phase: pick a prayer -------------------------------------------------

    async def _show_prayer_picker(self) -> None:
        self.phase = "select"
        scroll = self.query_one("#game-scroll", VerticalScroll)
        await scroll.remove_children()
        await scroll.mount(Static("[bold]Choose today's prayer:[/bold]"))
        list_view = ListView(id="prayer-list")
        await scroll.mount(list_view)
        for prayer in sorted(PRAYERS, key=lambda p: p.title.casefold()):
            await list_view.append(ListItem(Static(prayer.title), name=prayer.id))
        list_view.focus()

    async def on_list_view_selected(self, event: ListView.Selected) -> None:
        if event.list_view.id == "prayer-list":
            prayer_id = event.item.name
            prayer = next(p for p in PRAYERS if p.id == prayer_id)
            self.mad_lib = build_mad_lib(prayer, rng=random.Random())
            self.blank_positions = self.mad_lib.blank_order
            self.blank_cursor = 0
            await self._show_next_prompt()

    # -- phase: filling in the blanks -----------------------------------------

    async def _show_next_prompt(self) -> None:
        self.phase = "playing"
        assert self.mad_lib is not None
        scroll = self.query_one("#game-scroll", VerticalScroll)
        await scroll.remove_children()

        total = len(self.blank_positions)
        await scroll.mount(
            Static(f"[bold]{self.mad_lib.prayer.title}[/bold]  —  blank {self.blank_cursor + 1} of {total}")
        )
        await scroll.mount(
            Static("[dim]The finished prayer stays hidden until every blank is filled...[/dim]")
        )

        blank_index = self.blank_positions[self.blank_cursor]
        blank = self.mad_lib.blanks[blank_index]
        await scroll.mount(Static(f"\n[bold cyan]{blank.category.prompt}:[/bold cyan]"))
        await scroll.mount(
            Horizontal(
                Input(placeholder="Type your word...", id="answer-input"),
                Button("Submit  [Enter]", id="submit-btn", variant="primary"),
            )
        )
        self.query_one("#answer-input", Input).focus()

    async def on_input_submitted(self, event: Input.Submitted) -> None:
        if event.input.id == "answer-input":
            await self._submit_answer(event.value)

    async def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "submit-btn":
            await self._submit_answer(self.query_one("#answer-input", Input).value)
        elif event.button.id == "play-again-btn":
            await self._show_prayer_picker()
        elif event.button.id == "main-menu-btn":
            self.action_go_back()

    async def _submit_answer(self, text: str) -> None:
        assert self.mad_lib is not None
        blank_index = self.blank_positions[self.blank_cursor]
        self.mad_lib.set_answer(blank_index, text)
        self.blank_cursor += 1
        if self.blank_cursor >= len(self.blank_positions):
            await self._show_final_prayer()
        else:
            await self._show_next_prompt()

    # -- phase: reveal ---------------------------------------------------------

    async def _show_final_prayer(self) -> None:
        self.phase = "done"
        assert self.mad_lib is not None
        scroll = self.query_one("#game-scroll", VerticalScroll)
        await scroll.remove_children()
        await scroll.mount(Static(f"[bold gold3]{self.mad_lib.prayer.title} — Completed![/bold gold3]\n"))
        await scroll.mount(Static(self.mad_lib.render_rich(), id="prayer-final"))
        await scroll.mount(
            Horizontal(
                Button("Play Again  [r]", id="play-again-btn", variant="primary"),
                Button("Main Menu  [m]", id="main-menu-btn"),
            )
        )

    def action_go_back(self) -> None:
        self.app.pop_screen()

    async def action_replay(self) -> None:
        if self.phase == "done":
            await self._show_prayer_picker()

    def action_main_menu(self) -> None:
        if self.phase == "done":
            self.action_go_back()
