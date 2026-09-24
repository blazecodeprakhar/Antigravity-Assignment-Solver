# ⚡ Antigravity Universal Academic Assignment Solver

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-brightgreen.svg)](https://www.python.org/)
[![AI-Powered](https://img.shields.io/badge/Powered%20By-Antigravity%20AI-purple.svg)]()
[![Multi-Language](https://img.shields.io/badge/Languages-Python%20%7C%20Java%20%7C%20C%2B%2B%20%7C%20C%23%20%7C%20JS%20%7C%20C%20%7C%20Go%20%7C%20Rust-orange.svg)]()

> An autonomous, end-to-end academic lab assignment solver engine built for **Antigravity AI**. It automatically parses lab assignment `.docx` files, writes clean multi-language solution code, executes programs, generates high-definition light-mode terminal screenshots, and compiles publication-grade Word documents with **zero manual formatting effort**.

---

## 📌 Recommended Git Repository Names

If you are uploading this project to GitHub, here are the top recommended repository names:

1. `Antigravity-Assignment-Solver` *(Recommended)*
2. `AutoLab-Assignment-Solver`
3. `Universal-Academic-Assignment-Solver`
4. `Antigravity-Lab-Automation`

---

## 🚀 Key Features & Highlights

- ⚡ **Zero-Click Automation**: Run a single command (`python solve_assignment.py`) to process raw assignments, execute code, capture output screenshots, and build the final Word document.
- 🚫 **No Code Boxes / Tables**: Formats code lines directly as **plain text paragraphs** in `Consolas` ($10.5\text{ pt}$, $1.15\text{ line spacing}$) without table borders or shaded boxes.
- 🧹 **Automatic Comment Removal**: Strips all comment lines (`#`, `//`, `/* */`) from solution files prior to document compilation to satisfy strict academic submission criteria.
- 📸 **Crisp Light-Mode Terminal Screenshots**: Automatically renders light-mode window screenshots with active title bars, action buttons, blue command prompts, and high-contrast text.
- 📄 **100% Original Page Preservation**: Leaves Pages 1–2 of the raw assignment completely untouched, appending solutions after a clean Page Break.
- 🛡️ **Workspace Reset Persistence**: `Clear_Workspace.bat` resets temporary data folders (`raw_file/`, `workspace/`, `final_output/`) while leaving master solver scripts, skills, and configuration rules completely intact.

---

## 📁 Repository Structure

```text
ai class work/
├── raw_file/             # Place raw input assignment (.docx) here
├── workspace/            # Staging area for code (Problem1.py, etc.) & output screenshots
├── final_output/         # Completed, fully solved docx assignments
├── guides/               # Reference guidelines & example documents
├── .agents/              # Antigravity agent skills & protocol rules
│   ├── AGENTS.md
│   └── skills/
│       └── assignment_solver/
│           └── SKILL.md
├── solve_assignment.py   # Master automated Python pipeline script
├── Clear_Workspace.bat   # Double-click script to reset workspace folders
└── README.md             # Complete documentation & usage guide
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

**Antigravity** (Google DeepMind's agentic AI coding assistant) can solve any assignment autonomously using this repository. Here is how:

### Step 1: Place Your Assignment
Place your assignment `.docx` file into the `raw_file/` directory.

### Step 2: Prompt Antigravity AI
Simply send the prompt below to **Antigravity AI**:

```text
Start assignment
```

*Or use the Master Prompt:*

```text
You are an automated academic assignment solver. Execute the assignment solver protocol:
1. Inspect the raw document in raw_file/.
2. Solve each problem separately in workspace/ (Problem1.py, Problem2.py, etc.) with ZERO code comments.
3. Run `python solve_assignment.py` to compile the final docx into final_output/.
4. Ensure code is written as plain Consolas paragraphs with NO code boxes/tables.
```

### Step 3: What Antigravity Does Automatically
1. **Parses Assignment**: Reads questions, diagrams, and requirements from `raw_file/*.docx`.
2. **Generates Solutions**: Writes optimized code files in `workspace/Problem1.py`, `workspace/Problem2.py`, etc.
3. **Executes & Captures**: Runs `python solve_assignment.py` to execute solution scripts and capture light-mode terminal screenshots.
4. **Delivers Solved Document**: Compiles the finished `.docx` in `final_output/`.

---

## 🛠️ Manual CLI Usage

If you prefer to run the solver manually:

1. Place your raw assignment file in `raw_file/` (e.g. `raw_file/Assignment1.docx`).
2. Add your problem code files into `workspace/` (e.g. `workspace/Problem1.py`, `workspace/Problem2.py`).
3. Run the master script:
   ```bash
   python solve_assignment.py
   ```
4. Find your solved assignment inside `final_output/Assignment1.docx`.

---

## 🧹 Clearing Workspace for a New Assignment

Double-click `Clear_Workspace.bat` or run:
```cmd
Clear_Workspace.bat
```
This resets `raw_file/`, `workspace/`, and `final_output/` while keeping all solver scripts and agent rules completely intact for the next assignment.

---

## ⚖️ Strict Layout Rules Enforced

1. **No Code Boxes / Tables**: Code is inserted as plain paragraphs using `Consolas` font.
2. **Zero Code Comments**: Comment lines (`#`, `//`, `/* */`) are automatically stripped.
3. **Preserve Pages 1-2**: Original assignment content is untouched, followed by a Page Break.
4. **Light-Mode Terminal Output**: Screenshots use `#FFFFFF` background with crisp `#111111` font and window title bar.
