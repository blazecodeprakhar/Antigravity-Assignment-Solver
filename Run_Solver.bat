@echo off
title Antigravity Assignment Solver Launcher
echo ==================================================
echo      ANTIGRAVITY AUTOMATED ASSIGNMENT SOLVER      
echo ==================================================
echo.
echo Running automated assignment solver...
python solve_assignment.py
echo.
echo Attempting PDF export if MS Word is available...
python export_pdf.py 2>nul
echo.
echo ==================================================
echo Finished! Check 'final_output' folder for solutions.
echo ==================================================
pause
