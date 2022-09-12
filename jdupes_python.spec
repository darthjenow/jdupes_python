# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


find_duplicates_a = Analysis(
    ['find_duplicates.py'],
    pathex=[],
    binaries=[],
    datas=[('jdupes.exe', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
find_duplicates_pyz = PYZ(find_duplicates_a.pure, find_duplicates_a.zipped_data, cipher=block_cipher)

find_duplicates_exe = EXE(
    find_duplicates_pyz,
    find_duplicates_a.scripts,
    find_duplicates_a.binaries,
    find_duplicates_a.zipfiles,
    find_duplicates_a.datas,
    [],
    name='find_duplicates',
    debug=False,
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
)

move_duplicates_a = Analysis(
    ['move_duplicates.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
move_duplicates_pyz = PYZ(move_duplicates_a.pure, move_duplicates_a.zipped_data, cipher=block_cipher)

move_duplicates_exe = EXE(
    move_duplicates_pyz,
    move_duplicates_a.scripts,
    move_duplicates_a.binaries,
    move_duplicates_a.zipfiles,
    move_duplicates_a.datas,
    [],
    name='move_duplicates',
    debug=False,
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
)

search_empty_a = Analysis(
    ['search_empty.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
search_empty_pyz = PYZ(search_empty_a.pure, search_empty_a.zipped_data, cipher=block_cipher)

search_empty_exe = EXE(
    search_empty_pyz,
    search_empty_a.scripts,
    search_empty_a.binaries,
    search_empty_a.zipfiles,
    search_empty_a.datas,
    [],
    name='search_empty',
    debug=False,
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
)