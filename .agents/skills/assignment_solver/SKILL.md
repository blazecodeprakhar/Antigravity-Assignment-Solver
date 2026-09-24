---
name: assignment_solver
description: Automatically solves docx assignments in the workspace without code boxes and generates light-mode terminal screenshots.
---

# Assignment Solver Skill

When tasked with solving an assignment:

1. Read the raw `.docx` from `raw_file/`.
2. Save solution code files in `workspace/Problem1.py`, `workspace/Problem2.py`, etc. Ensure **zero comments** in code.
3. Run `python solve_assignment.py` to compile the final `.docx` in `final_output/`.
4. Ensure code in `.docx` is written as plain paragraphs (Consolas font) with **NO table box / NO borders**.
