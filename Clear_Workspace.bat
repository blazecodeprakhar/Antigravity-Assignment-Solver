@echo off
title Clear Workspace Tool
echo ==================================================
echo         AUTOMATED WORKSPACE CLEARING TOOL        
echo ==================================================
echo.
echo Closing MS Word processes if active...
taskkill /f /im WINWORD.EXE 2>nul

echo Clearing 'raw_file' folder...
del /q /f "%~dp0raw_file\*.*" 2>nul
for /d %%p in ("%~dp0raw_file\*") do rmdir /s /q "%%p" 2>nul

echo Clearing 'workspace' folder...
del /q /f "%~dp0workspace\*.*" 2>nul
for /d %%p in ("%~dp0workspace\*") do rmdir /s /q "%%p" 2>nul

echo Clearing 'final_output' folder...
del /q /f "%~dp0final_output\*.*" 2>nul
for /d %%p in ("%~dp0final_output\*") do rmdir /s /q "%%p" 2>nul

echo.
echo SUCCESS: Workspace cleared cleanly!
echo Guides and system instruction files remain untouched.
echo You can now place your new assignment file into 'raw_file' folder.
echo.
pause
