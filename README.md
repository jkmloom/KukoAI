# Kuko AI 🎙️💻

> **Version:** kukoai_a1.0  
> **Release Date:** January 09, 2026

## 📖 About
**Kuko AI** is a voice-activated AI agent designed to perform general computer operations, such as opening and managing files, entirely through voice commands. 

This project was developed by a group of Computer Science students at **ABSS Institute of Technology, Meerut**, with the goal of exploring desktop automation and speech recognition technologies.

## 🛠️ Tech Stack
* **Language:** Python (v3.10.11)
* **Speech Engine:** Google Speech Recognition (via `speech_recognition`)
* **Core Libraries:**
    * `speech_recognition` (Voice input processing)
    * `win32com.client` (Windows OS interaction)
    * `webbrowser` (Web navigation)
    * `os` (System commands)
    * `openai` (LLM integration)
    * `datetime` (Time-based operations)

## 🖥️ Compatibility & Platform
* **Primary Platform:** Windows 11
* **Compatibility:** Compatible with most modern Windows OS versions.

> **⚠️ Important Note for Mac/Linux Users:** > The source code is developed exclusively for the Windows ecosystem (specifically relying on `win32com`). If you intend to run this on macOS or Linux, you must replace Windows-specific libraries with their Unix equivalents (e.g., using `applescript` or `subprocess` for system control).

## 📥 Installation / Usage
You can run the source code directly or download the standalone executable for Windows.

* **[Download .exe for Windows](INSERT_YOUR_LINK_HERE)**

## 🚧 Known Issues & Roadmap
This project is currently in **Alpha (a1.0)**. We are aware of the following limitations and actively looking for contributions or solutions:

1.  **Limited Functionality:** The agent currently lacks several basic desktop automation features.
2.  **App Termination:** While many apps can be *opened* via voice, closing them via voice command is not yet fully supported.
3.  **API Instability:** The OpenAI API integration is currently throwing intermittent errors.
4.  **Hardcoded Logic:** Operations are currently limited to pre-programmed tasks defined in `main.py`; the agent cannot yet infer new tasks dynamically.
5.  **Optimization:** System resource management needs improvement.
6.  **Context Awareness:** Kuko AI currently has no short-term or long-term memory management (no context retention between commands).

## 👥 Credits
Developed by CS Students at **ABSS Institute of Technology, Meerut** (Jan 2026).

* **Jatin Kumar Mehta** (Python Developer) - [GitHub Profile](https://github.com/jkmloom)
* **Aryan Shakya** (Python Developer) - [GitHub Profile](https://github.com/shakyaryan)
* **Abhishek Charak** (Web Developer) - [GitHub Profile](https://github.com/abicharak)