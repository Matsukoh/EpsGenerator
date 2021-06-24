#!/usr/bin/env bash
pyinstaller -y --clean --windowed EpsGenerator.spec
pushd dist
hdiutil create ./EpsGenerator.dmg -srcfolder EpsGenerator.app -ov
popd