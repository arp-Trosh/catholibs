# ☩ Catholibs ☩

*The Catholic-inspired Mad-Libs game — for Saints and Sinners!*

Catholibs is a terminal game built with [Textual](https://textual.textualize.io/).
Pick one of 200+ traditional Catholic prayers, fill in the blanks with nouns,
verbs, adjectives, animals, celebrities, sins, and more, then read the
(ir)reverent result aloud. Hymns play in the background while you play.

## Features

- **Single player** — pick a prayer, answer every prompt yourself, see the finished prayer.
- **Multiplayer over LAN** — one player hosts, up to 8 players join. Players take turns
  filling blanks and only see the word *type* being asked for, never the other players'
  words, until the big reveal at the end.
- **Grammar-aware blanks** — blanked words come from a hand-tagged part-of-speech list,
  so the prompts ("a verb ending in -ing", "a plural noun", ...) keep the sentence grammatical.
- **Background music** — a looping playlist of hymns, with mute, volume, and previous/next
  track controls in the top-left corner. If no audio device is available, the game runs silently.

## Requirements

- Python 3.10+
- A terminal with true color support is recommended

## Installation

```bash
git clone https://github.com/arp-Trosh/catholibs.git
cd catholibs
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Running

```bash
python -m catholibs
```

### Keyboard shortcuts

| Key      | Action                     |
|----------|----------------------------|
| `1`      | Single Player (title menu) |
| `2`      | Multiplayer (title menu)   |
| `Esc`    | Back to the main menu      |
| `q`      | Quit                       |

## Multiplayer

1. The host chooses **Multiplayer → Host a Game** (`h`), enters a name, and optionally a port
   (default `5555`). The host screen shows their local network address.
2. Other players choose **Multiplayer → Join a Game** (`j`) and enter the host's address and port.
3. When everyone has joined, the host starts the game.

The host's machine must allow incoming TCP connections on the chosen port.

## Windows

A standalone Windows `.exe` is built with PyInstaller by the
[Build Windows exe](.github/workflows/windows-build.yml) GitHub Actions workflow
(run it manually from the Actions tab). The latest build is published under the
[`windows-build` release](https://github.com/arp-Trosh/catholibs/releases/tag/windows-build).

The exe is unsigned, so Windows SmartScreen may show an "Unknown publisher" prompt —
click **More info → Run anyway**. If Windows Terminal is installed, the game
relaunches inside it for better rendering.

To build locally on Windows:

```bash
pip install -r requirements.txt pyinstaller
pyinstaller packaging/windows/catholibs.spec --noconfirm
```

## Project layout

```
catholibs/
├── __main__.py         # entry point (python -m catholibs)
├── mad_lib.py          # turns prayer text into blanks and renders the result
├── prayers_data.py     # the prayer texts
├── prayer_tags.py      # hand-verified part-of-speech tags for blankable words
├── audio.py            # background music via pygame's mixer
├── network/            # asyncio TCP server/client and JSON message protocol
├── ui/                 # Textual app, screens, widgets, and stylesheet
└── assets/music/       # bundled hymn tracks
packaging/windows/      # PyInstaller spec and version info
```
