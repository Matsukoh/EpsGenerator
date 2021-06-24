#!/usr/bin/env bash
# pyinstaller --onefile --noconsole --name EpsGenerator ./scripts/eps_generator.py
# python -OO -m PyInstaller --onefile --noconsole --name EpsGenerator eps_generator.py
pyinstaller -y --clean --windowed --name EpsGenerator --exclude-module _tkinter --exclude-module Tkinter --exclude-module enchant --exclude-module twisted ./scripts/eps_generator.py