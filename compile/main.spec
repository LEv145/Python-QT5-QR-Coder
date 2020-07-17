# -*- mode: python ; coding: utf-8 -*-

import os
import sys

from pathlib import Path

from pylibdmtx import pylibdmtx
from pyzbar import pyzbar

block_cipher = None


a = Analysis(['main.py'],
             pathex=[str(Path('.').absolute())],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=os.getenv('EXCLUDE_MODULES', '').split(' '),
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)

a.binaries += TOC([
    (Path(dep._name).name, dep._name, 'BINARY')
    for dep in pylibdmtx.EXTERNAL_DEPENDENCIES + pyzbar.EXTERNAL_DEPENDENCIES
])

a.datas += [('icon.png','D:\\Desktop\\projects\\Qt\\QR\\QR\\compile\\icon.png','DATA')]

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)



exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='main',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False,icon='D:\\Desktop\\projects\\Qt\\QR\\QR\\compile\\icon.ico')

