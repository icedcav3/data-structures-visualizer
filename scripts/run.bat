# Windows
REM @echo off
REM setlocal enabledelayedexpansion
REM cd /d %~dp0
REM python src/main.py
REM pause

@echo off
title Data Structures Visualizer
cd /d "%~dp0"
python src/main.py
if errorlevel 1 (
    echo.
    echo Error: Failed to run the application.
    echo Make sure Python is installed and in your PATH.
    echo.
    pause
)
