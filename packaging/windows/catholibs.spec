# -*- mode: python ; coding: utf-8 -*-
"""PyInstaller spec for the Windows build of Catholibs.

Build with:
    pyinstaller packaging/windows/catholibs.spec --distpath dist --workpath build --noconfirm

Notes on avoiding antivirus/SmartScreen false positives:
  - upx=False: UPX-compressed executables are a well-known heuristic
    trigger, since a lot of malware uses UPX to shrink and obfuscate
    itself. Leaving the exe uncompressed makes it look far more like
    ordinary compiled software.
  - version file: embeds genuine, non-impersonating metadata (see
    version_info.txt) instead of shipping an anonymous binary.
  - built on a clean windows-latest GitHub Actions runner, not
    cross-compiled through Wine (Wine-built PyInstaller binaries are
    disproportionately flagged by AV engines).
None of this can remove the "Unknown publisher" Windows SmartScreen
prompt on first run -- that requires a paid code-signing certificate,
which this project does not have.
"""
from pathlib import Path

from PyInstaller.utils.hooks import collect_all

project_root = Path(SPECPATH).resolve().parent.parent

textual_datas, textual_binaries, textual_hidden = collect_all("textual")
rich_datas, rich_binaries, rich_hidden = collect_all("rich")

datas = [
    (str(project_root / "catholibs" / "assets" / "music"), "catholibs/assets/music"),
    (str(project_root / "catholibs" / "ui" / "app.tcss"), "catholibs/ui"),
    (str(project_root / "catholibs" / "ui" / "screens" / "jesus.txt"), "catholibs/ui/screens"),
    *textual_datas,
    *rich_datas,
]

a = Analysis(
    [str(project_root / "catholibs" / "windows_launcher.py")],
    pathex=[str(project_root)],
    binaries=[*textual_binaries, *rich_binaries],
    datas=datas,
    hiddenimports=[*textual_hidden, *rich_hidden],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name="catholibs",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    version=str(project_root / "packaging" / "windows" / "version_info.txt"),
)
