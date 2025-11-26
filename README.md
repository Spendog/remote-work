# Remote Work (v0.333)

**Current Status:** Pre-Alpha / Foundation  
**Base:** Forked from [Remote Keyboard v1.2](https://github.com/Spendog/remote-keyboard)

## Overview
This project is the evolution of the Remote Keyboard tool into a comprehensive "Remote Work" suite. The goal is to build an overarching program that provides seamless connection and specific productivity features for remote control and workflow management.

**Target Version 1.0 Goal:** A fully shaped idea with expanded features beyond simple input control.

## Installation & Usage
(Inherited from Remote Keyboard v1.2)

1.  **Run Setup**: `setup.bat` (Installs Python dependencies)
2.  **Start App**: `run.bat`
3.  **Connect**: Scan the QR code with your phone.

## Developer Instructions

### Versioning
*   **v0.333**: Current foundation (Remote Keyboard v1.2 engine).
*   **v1.0**: The first major release of the full "Remote Work" suite.

### Project Structure
*   `app.py`: Core Flask server and Socket.IO logic.
*   `gui_app.py`: Desktop GUI wrapper (PyQt/Tkinter).
*   `templates/remote.html`: The mobile frontend interface.

## Roadmap & Future Features
*   [ ] **Expanded Control**: Beyond keyboard/mouse (e.g., app launching, media control).
*   [ ] **Workflow Tools**: Features specific to remote work productivity.
*   [ ] **Security Enhancements**: Advanced pairing and encryption.
*   [ ] **UI Overhaul**: A new interface for the expanded feature set.

---
*Note: This repository was manually branched from Remote Keyboard due to GitHub restrictions on forking own repositories.*
