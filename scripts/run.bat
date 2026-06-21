@echo off
REM Script to run the application on Windows

cd /d "%~dp0"..
if errorlevel 1 exit /b 1

python src/main.py
