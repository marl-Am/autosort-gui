## AutoSort – Automated File Organizer
AutoSort is a simple and powerful Python application designed to help you automatically sort files in a directory. Whether you're managing a chaotic Downloads folder or archiving project files, AutoSort can help you stay organized.


- Key Features
 - Sort by File Type (e.g., Documents, Images, Code, Music, Archives)
 - Sort by Date Modified (e.g., groups files by 2025-06, 2025-05, etc.)
 - Graphical User Interface (GUI) with status updates and timestamp
 - Command-Line Interface (CLI) support for power users and automation
 - Portable .exe Build with custom icon for Windows (no Python required)
 - Batch File Launcher for one-click use

GUI (AutoSort GUI)
- Windows EXE Version
 - Download the .exe from the Releases.
 - Double-click to launch — no installation required.
 - Select a folder, choose "Type" or "Date", and click Run Sort.
 - See results in the app’s status bar.

- Run from Source
 - Install Python 3.8+ (if not already installed).
 - Clone this repo and run: python autosort_gui.py

- autosort/
 - autosort.py           # CLI logic
 - autosort_gui.py       # GUI logic
 - autosort.ico          # App icon
 - run_autosort.bat      # Optional launcher
 - dist/                 # Generated .exe goes here
 - README.md
 - requirements.txt
 - setup.py              # (Optional) CLI installation