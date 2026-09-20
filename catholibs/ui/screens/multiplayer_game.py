import asyncio

from textual.app import ComposeResult
from textual.binding import Binding
from textual.containers import Container, Horizontal, Vertical, VerticalScroll
from textual.screen import Screen
from textual.widgets import Button, Footer, Header, Input, ListItem, ListView, RichLog, Select, Static

from ...network.client import GameClient
from ...network.server import GameServer
from ...prayers_data import PRAYERS
from ..widgets.music_bar import MusicBar

RANDOM_PRAYER = "__random__"


class MultiplayerGameScreen(Screen):
    """The 3-pane multiplayer screen: game status (top), chat (bottom-left),
    and players / host controls (bottom-right). Covers lobby, play, and reveal."""

    BINDINGS = [
        Binding("b", "begin", "Begin", show=False),
        Binding("e", "end", "End Game", show=False),
        Binding("r", "restart", "Restart", show=False),
        Binding("escape", "leave", "Leave Game"),
    ]

    def __init__(self, role: str, name: str, port: int, address: str = "127.0.0.1") -> None:
        super().__init__()
        self.role = role  # "host" or "join"
        self.player_name = name
        self.port = port
        self.address = address

        self.server: GameServer | None = None
        self.client: GameClient | None = None

        self.phase = "connecting"  # connecting | lobby | playing | reveal
        self.players: list[dict] = []
        self.host_id: int | None = None
        self.prayer_title: str = ""
        self.is_my_turn = False
        self.current_prompt: str | None = None
        self.current_blank_index: int | None = None
        self.progress_text = ""
        self.selected_prayer_id: str | None = None  # None means "Random"

        self._msg_queue: asyncio.Queue = asyncio.Queue()
        # Renders are triggered from two independent tasks (the initial
        # connect handshake and the message loop), which can otherwise
        # interleave mid-render and mount duplicate-ID widgets.
        self._game_content_lock = asyncio.Lock()
        self._side_panel_lock = asyncio.Lock()

    # -- layout ---------------------------------------------------------------

    def compose(self) -> ComposeResult:
        yield MusicBar()
        yield Header()
        with Container(id="mp-root"):
            with Container(id="game-panel"):
                yield Static("Connecting...", id="game-content")
            with Horizontal(id="lower-area"):
                with Vertical(id="chat-panel"):
                    yield RichLog(id="chat-log", wrap=True, min_width=0, markup=True, highlight=False)
                    yield Input(placeholder="Type a message and press Enter...", id="chat-input")
                with VerticalScroll(id="side-panel"):
                    yield Static("[bold]Players[/bold]", id="players-title")
                    yield ListView(id="player-list")
                    yield Vertical(id="host-controls")
        yield Footer()

    def on_mount(self) -> None:
        self.run_worker(self._message_loop(), exclusive=False)
        self.run_worker(self._network_setup(), exclusive=False)

    # -- networking bootstrap ---------------------------------------------------

    async def _network_setup(self) -> None:
        log = self.query_one("#chat-log", RichLog)
        try:
            if self.role == "host":
                self.server = GameServer()
                await self.server.start(self.port)
                connect_host, connect_port = "127.0.0.1", self.port
            else:
                connect_host, connect_port = self.address, self.port

            self.client = GameClient(on_message=self._on_network_message)
            await self.client.connect(connect_host, connect_port, self.player_name)
        except (ConnectionError, OSError, asyncio.TimeoutError) as exc:
            log.write(f"[red]Could not connect: {exc}[/red]")
            self._set_game_content(f"[red]Connection failed:[/red] {exc}\n\nPress escape to go back.")
            return

        self.phase = "lobby"
        await self._render_all()

    def _on_network_message(self, msg: dict) -> None:
        self._msg_queue.put_nowait(msg)

    async def _message_loop(self) -> None:
        while True:
            msg = await self._msg_queue.get()
            await self._process_message(msg)

    # -- incoming message handling ------------------------------------------

    async def _process_message(self, msg: dict) -> None:
        kind = msg.get("type")
        log = self.query_one("#chat-log", RichLog)

        if kind == "player_list":
            self.players = msg["players"]
            self.host_id = msg["host_id"]
            await self._render_side_panel()
            await self._render_game_content()

        elif kind == "chat":
            sender = msg.get("from", "?")
            text = msg.get("text", "")
            if msg.get("system"):
                log.write(f"[dim italic]* {text}[/dim italic]")
            else:
                log.write(f"[bold]{sender}:[/bold] {text}")

        elif kind == "game_started":
            self.phase = "playing"
            self.prayer_title = msg["prayer_title"]
            order = ", ".join(msg["turn_order"])
            log.write(f"[bold gold3]--- {self.prayer_title} begins! Turn order: {order} ---[/bold gold3]")
            await self._render_game_content()
            await self._render_side_panel()

        elif kind == "your_turn":
            self.is_my_turn = True
            self.current_prompt = msg["prompt"]
            self.current_blank_index = msg["blank_index"]
            self.progress_text = f"blank {msg['blank_number']} of {msg['total_blanks']}"
            await self._render_game_content()

        elif kind == "waiting_on":
            self.is_my_turn = False
            self.progress_text = f"blank {msg['blank_number']} of {msg['total_blanks']}"
            log.write(f"[cyan]➤ Waiting on {msg['player_name']} — {msg['prompt']}...[/cyan]")
            await self._render_game_content()

        elif kind == "reveal":
            self.phase = "reveal"
            self.is_my_turn = False
            self.prayer_title = msg["title"]
            self._reveal_text = msg["text"]
            log.write(f"[bold gold3]--- The mad-lib is revealed! ---[/bold gold3]")
            await self._render_game_content()
            await self._render_side_panel()

        elif kind == "game_ended":
            self.phase = "lobby"
            log.write("[dim italic]* The host ended the game.[/dim italic]")
            await self._render_game_content()
            await self._render_side_panel()

        elif kind == "promoted_host":
            log.write("[bold]* You are now the host.[/bold]")
            await self._render_side_panel()

        elif kind == "error":
            log.write(f"[red]{msg.get('message')}[/red]")

        elif kind == "disconnected":
            log.write("[red]Disconnected from server.[/red]")
            self._set_game_content("[red]Disconnected from server.[/red] Press escape to go back.")

    # -- rendering ------------------------------------------------------------

    def _set_game_content(self, text: str) -> None:
        self.query_one("#game-content", Static).update(text)

    async def _render_all(self) -> None:
        await self._render_game_content()
        await self._render_side_panel()

    async def _render_game_content(self) -> None:
        async with self._game_content_lock:
            await self._do_render_game_content()

    async def _do_render_game_content(self) -> None:
        container = self.query_one("#game-panel", Container)
        # Drop any dynamically-mounted answer input from a previous turn.
        for child in list(container.query("#answer-row")):
            await child.remove()

        if self.phase == "lobby":
            names = ", ".join(p["name"] for p in self.players) or "(none yet)"
            lines = [
                "[bold]Lobby[/bold]",
                f"Players ({len(self.players)}/8): {names}",
            ]
            if self.client and self.client.is_host:
                lines.append("\n[bold cyan]You are the host — press Begin (b) when everyone's ready.[/bold cyan]")
            else:
                lines.append("\n[dim]Waiting for the host to begin the game...[/dim]")
            self._set_game_content("\n".join(lines))

        elif self.phase == "playing":
            lines = [f"[bold]{self.prayer_title}[/bold]  —  {self.progress_text}"]
            if self.is_my_turn:
                lines.append(f"\n[bold cyan]{self.current_prompt}:[/bold cyan]")
            else:
                lines.append("\n[dim]Watch the chat log to see whose turn it is.[/dim]")
            self._set_game_content("\n".join(lines))
            if self.is_my_turn:
                row = Horizontal(
                    Input(placeholder="Type your word...", id="answer-input"),
                    Button("Submit  [Enter]", id="submit-answer-btn", variant="primary"),
                    id="answer-row",
                )
                await container.mount(row)
                self.query_one("#answer-input", Input).focus()

        elif self.phase == "reveal":
            text = getattr(self, "_reveal_text", "")
            self._set_game_content(f"[bold gold3]{self.prayer_title} — Revealed![/bold gold3]\n\n{text}")

    async def _render_side_panel(self) -> None:
        async with self._side_panel_lock:
            await self._do_render_side_panel()

    async def _do_render_side_panel(self) -> None:
        player_list = self.query_one("#player-list", ListView)
        await player_list.clear()
        my_id = self.client.player_id if self.client else None
        for p in self.players:
            tag = ""
            if p["id"] == self.host_id:
                tag += " (host)"
            if p["id"] == my_id:
                tag += " (you)"
            await player_list.append(ListItem(Static(f"{p['name']}{tag}")))

        controls = self.query_one("#host-controls", Vertical)
        await controls.remove_children()
        if self.client and self.client.is_host:
            await controls.mount(Static("[bold]Next prayer[/bold]"))
            await controls.mount(self._build_prayer_select())
            if self.phase == "lobby":
                await controls.mount(Button("Begin Game  [b]", id="begin-btn", variant="primary"))
            else:
                await controls.mount(Button("End Game  [e]", id="end-btn"))
                await controls.mount(Button("Restart  [r]", id="restart-btn", variant="primary"))

    def _build_prayer_select(self) -> Select:
        options = [("Random", RANDOM_PRAYER)] + [
            (p.title, p.id) for p in sorted(PRAYERS, key=lambda p: p.title.casefold())
        ]
        return Select(
            options,
            value=self.selected_prayer_id or RANDOM_PRAYER,
            id="prayer-select",
            allow_blank=False,
        )

    # -- user input -------------------------------------------------------------

    async def on_input_submitted(self, event: Input.Submitted) -> None:
        if event.input.id == "chat-input":
            text = event.value.strip()
            event.input.value = ""
            if text and self.client:
                await self.client.send_chat(text)
        elif event.input.id == "answer-input":
            await self._submit_answer(event.value)

    def on_select_changed(self, event: Select.Changed) -> None:
        if event.select.id == "prayer-select":
            self.selected_prayer_id = None if event.value == RANDOM_PRAYER else event.value

    async def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "begin-btn":
            await self.action_begin()
        elif event.button.id == "end-btn":
            await self.action_end()
        elif event.button.id == "restart-btn":
            await self.action_restart()
        elif event.button.id == "submit-answer-btn":
            await self._submit_answer(self.query_one("#answer-input", Input).value)

    async def _submit_answer(self, text: str) -> None:
        if self.client and self.current_blank_index is not None:
            await self.client.send_answer(self.current_blank_index, text)
            self.is_my_turn = False
            self.current_blank_index = None

    # -- host actions -------------------------------------------------------------

    async def action_begin(self) -> None:
        if self.client and self.client.is_host and self.phase == "lobby":
            await self.client.send_begin(self.selected_prayer_id)

    async def action_end(self) -> None:
        if self.client and self.client.is_host:
            await self.client.send_end()

    async def action_restart(self) -> None:
        if self.client and self.client.is_host:
            await self.client.send_restart(self.selected_prayer_id)

    def action_leave(self) -> None:
        if self.client:
            self.client.close()
        if self.server:
            self.server.stop()
        self.app.pop_screen()
