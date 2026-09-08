# -*- mode: python ; coding: utf-8 -*-


block_cipher = None
from kivy_deps import sdl2, glew
from kivymd import hooks_path as kivymd_hooks_path


a = Analysis(
    ['H:\\Learning\\code something big\\Projects_end\\Icon\\main.py'],
    pathex=['H:\\Learning\\code something big\\Projects_end\\Icon\\dist'],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=['C:\\Users\\Alex Dynamo\\AppData\\Local\\Programs\\Python\\Python310\\Lib\\site-packages\\kivymd\\tools\\packaging\\pyinstaller'],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)
splash = Splash(
    'H:\\Learning\\code something big\\Projects_end\\Icon\\iconlogo.ico',
    binaries=a.binaries,
    datas=a.datas,
    text_pos=None,
    text_size=12,
    minify_script=True,
    always_on_top=True,
)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)],
    splash,
    splash.binaries,
    [],
    name='Icon list',
    debug=True,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['H:\\Learning\\code something big\\Projects_end\\Icon\\iconlogo.ico'],
)
