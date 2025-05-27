@echo off
cd /d %~dp0

REM Run the standalone exe using the 'data' folder
autosort_gui.exe

echo.
echo AutoSort GUI closed. Press any key to exit.
pause >nul
