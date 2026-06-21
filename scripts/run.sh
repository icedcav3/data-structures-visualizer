#!/bin/bash
# Linux/macOS
set -e

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR/.."

echo "Starting Data Structures Visualizer..."
python src/main.py

if [ $? -ne 0 ]; then
    echo "Error: Failed to run the application."
    echo "Make sure Python is installed and accessible."
    exit 1
fi
