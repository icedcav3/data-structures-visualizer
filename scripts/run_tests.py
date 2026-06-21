#!/usr/bin/env python
"""Script to run all tests with coverage report."""

import subprocess
import sys


def run_tests():
    """Run all tests with pytest and generate coverage report."""
    print("Running tests with coverage...")
    
    result = subprocess.run(
        [
            sys.executable, "-m", "pytest",
            "--cov=src",
            "--cov-report=html",
            "--cov-report=term",
            "-v",
            "tests/"
        ],
        cwd="."
    )
    
    if result.returncode == 0:
        print("\n" + "="*60)
        print("All tests passed!")
        print("Coverage report generated in htmlcov/index.html")
        print("="*60)
    else:
        print("\n" + "="*60)
        print("Some tests failed.")
        print("="*60)
    
    return result.returncode


if __name__ == "__main__":
    sys.exit(run_tests())
