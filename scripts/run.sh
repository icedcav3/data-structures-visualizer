#!/bin/bash
# Script to run the application on Linux/macOS

cd "$(dirname "$0")"/.. || exit
python src/main.py
