"""Main entry point for the Data Structures Visualizer application."""

import sys
from pathlib import Path

# Add src directory to path
sys.path.insert(0, str(Path(__file__).parent))

from gui.app import VisualizerApp


def main():
    """Initialize and run the main application."""
    app = VisualizerApp()
    app.run()


if __name__ == "__main__":
    main()
