"""Entry point for the Windows .exe build.

Double-clicking an exe on Windows normally runs it in the bare conhost
window, which renders Textual apps poorly (no true color, no ligatures).
If Windows Terminal is installed, this relaunches the game inside it and
exits; otherwise it just runs in whatever console is already attached.
"""
from __future__ import annotations

import os
import shutil
import subprocess
import sys


def _relaunch_in_windows_terminal() -> bool:
    wt = shutil.which("wt.exe") or shutil.which("wt")
    if not wt:
        return False

    exe = sys.executable if getattr(sys, "frozen", False) else os.path.abspath(sys.argv[0])
    env = os.environ.copy()
    env["CATHOLIBS_NO_RELAUNCH"] = "1"
    try:
        subprocess.Popen([wt, "new-tab", "--title", "Catholibs", exe], env=env, close_fds=True)
    except OSError:
        return False
    return True


def main() -> None:
    if (
        sys.platform == "win32"
        and "WT_SESSION" not in os.environ
        and "CATHOLIBS_NO_RELAUNCH" not in os.environ
        and _relaunch_in_windows_terminal()
    ):
        return

    from catholibs.ui.app import CatholibsApp

    CatholibsApp().run()


if __name__ == "__main__":
    main()
