# Terminal Utility CLI

A lightweight personal terminal utility built with Python, Typer, Rich, SymPy, and psutil to handle daily tasks directly from the command line.

---

## Features

- **Symbolic Math Solver:** Solve algebraic equations and simplify expressions directly in the console (`cli math`).
- **Hardware Telemetry:** Quick readouts for Apple Silicon CPU usage and RAM pressure (`cli stats`).
- **Focus Study Timer:** Terminal countdown timer with native macOS alert notifications (`python main.py timer --minutes 1`).

---

## Getting Started

```bash
# Clone the repository
git clone [https://github.com/sohamshewani/terminal-utility.git](https://github.com/sohamshewani/terminal-utility.git)
cd terminal-utility

# Set up environment
python3 -m venv venv
source venv/bin/activate
pip install typer rich sympy psutil

# Usage
python main.py stats
python main.py math "x**2 - 9"

