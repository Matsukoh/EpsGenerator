# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['scripts/eps_generator.py'],
             pathex=['/Users/kohei/ws/EpsGenerator'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=['_tkinter', 'Tkinter', 'enchant', 'twisted'],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='EpsGenerator',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False )
coll = COLLECT(exe, Tree('./scripts'),
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='EpsGenerator')
app = BUNDLE(coll,
             name='EpsGenerator.app',
             icon=None,
             bundle_identifier=None)
