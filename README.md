# ⚡ Antigravity Universal Academic Assignment Solver v2.0

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-brightgreen.svg)](https://www.python.org/)
[![AI-Powered](https://img.shields.io/badge/Powered%20By-Antigravity%20AI-purple.svg)]()
[![Multi-Language](https://img.shields.io/badge/Languages-Python%20%7C%20Java%20%7C%20C%2B%2B%20%7C%20C%23%20%7C%20JS%20%7C%20C%20%7C%20Go%20%7C%20Rust-orange.svg)]()

> An autonomous, end-to-end academic lab assignment solver engine built for **Antigravity AI**. It automatically parses lab assignment `.docx` files, writes clean multi-language solution code, executes programs, generates high-definition light-mode terminal screenshots, and compiles publication-grade Word documents & PDFs with **zero manual formatting effort**.

---

## 📌 GitHub Repository Details
- **Repository**: [`https://github.com/blazecodeprakhar/Antigravity-Assignment-Solver.git`](https://github.com/blazecodeprakhar/Antigravity-Assignment-Solver.git)
- **Branch**: `main`

---

## 🚀 Enterprise Key Features & Modules

- ⚡ **Zero-Click Master Solver (`solve_assignment.py`)**: Run a single command or double-click `Run_Solver.bat` to process raw assignments, execute code, capture output screenshots, and build final `.docx` & `.pdf` files.
- 🧠 **Intelligent Question Parser & Template Generator (`auto_template.py`)**: Scans raw assignment `.docx` files, extracts problem statements, and generates starter template scripts (`workspace/Problem1.py`, etc.).
- 🎨 **Multi-Theme Terminal Renderer**: Configurable light mode terminal themes (`cmd_light`, `powershell_light`, `macos_light`) via `config.json`.
- 📕 **Automated PDF Export Module (`export_pdf.py`)**: Converts completed Word documents into university-compliant PDF files automatically.
- 🚫 **No Code Boxes / Tables**: Formats code lines directly as **plain text paragraphs** in `Consolas` ($10.5\text{ pt}$, $1.15\text{ line spacing}$) without table borders or shaded boxes.
- 🧹 **Automatic Comment Removal**: Strips all comment lines (`#`, `//`, `/* */`) from solution files prior to document compilation to satisfy strict academic submission criteria.
- 📄 **100% Original Page Preservation**: Leaves Pages 1–2 of the raw assignment completely untouched, appending solutions after a clean Page Break.
- 🛡️ **Workspace Reset Persistence**: `Clear_Workspace.bat` resets temporary data folders (`raw_file/`, `workspace/`, `final_output/`) while leaving master solver scripts, skills, and configuration rules completely intact.

---

## 📁 Repository Structure

```text
ai class work/
├── raw_file/             # Place raw input assignment (.docx) here
├── workspace/            # Staging area for code (Problem1.py, etc.) & output screenshots
├── final_output/         # Completed, fully solved docx & pdf assignments
├── guides/               # Reference guidelines & example documents
├── .agents/              # Antigravity agent skills & protocol rules
│   ├── AGENTS.md
│   └── skills/
│       └── assignment_solver/
│           └── SKILL.md
├── config.json           # Global solver theme & layout configuration settings
├── auto_template.py      # Question extractor & solution template generator
├── solve_assignment.py   # Master automated Python pipeline script
├── export_pdf.py         # Automated docx-to-pdf conversion module
├── Run_Solver.bat        # Double-click launcher for Windows execution
├── Clear_Workspace.bat   # Double-click script to reset workspace folders
└── README.md             # Complete documentation & architecture guide
```

---

## 🌐 Supported Programming Languages

| Language | File Extension | Execution Command |
| :--- | :--- | :--- |
| **Python** | `.py` | `python Problem1.py` |
| **JavaScript / Node.js** | `.js` | `node Problem1.js` |
| **C++** | `.cpp` | `g++ Problem1.cpp -o Problem1.exe && Problem1.exe` |
| **C** | `.c` | `gcc Problem1.c -o Problem1.exe && Problem1.exe` |
| **Java** | `.java` | `javac Problem1.java && java Problem1` |
| **C#** | `.cs` | `dotnet run` / `csc Problem1.cs` |
| **Go** | `.go` | `go run Problem1.go` |
| **Rust** | `.rs` | `rustc Problem1.rs && Problem1.exe` |

---

## 🤖 How to Use Antigravity AI for Instant Assignment Solving

**Antigravity** (Google DeepMind's agentic AI coding assistant) solves any assignment autonomously using this repository. Here is how:

### Step 1: Place Your Assignment
Place your raw assignment `.docx` file into the `raw_file/` directory.

### Step 2: Prompt Antigravity AI
Send the prompt below to **Antigravity AI**:

```text
Start assignment
```

### Step 3: What Antigravity Does Automatically
1. **Parses Assignment**: Reads questions, diagrams, and requirements from `raw_file/*.docx`.
2. **Generates Templates & Solutions**: Writes optimized code files in `workspace/Problem1.py`, `workspace/Problem2.py`, etc. (**with zero comments**).
3. **Executes & Captures**: Runs `python solve_assignment.py` to execute solution scripts and capture light-mode terminal screenshots.
4. **Delivers Solved Document & PDF**: Compiles finished `.docx` & `.pdf` files inside `final_output/`.

---

## 🛠️ Double-Click & CLI Usage

- **Double-Click Execution (Windows)**: Simply double-click `Run_Solver.bat`.
- **Manual CLI Command**:
  ```bash
  python solve_assignment.py
  python export_pdf.py
  ```

---

## 🧹 Clearing Workspace for a New Assignment

Double-click `Clear_Workspace.bat` to reset temporary assignment data for the next project while keeping all solver scripts and rules 100% intact.
