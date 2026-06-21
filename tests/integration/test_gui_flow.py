"""Integration tests for GUI flow."""

import pytest
from src.gui.app import VisualizerApp


class TestGUIFlow:
    """Integration tests for GUI workflow."""

    @pytest.fixture
    def app(self):
        """Create an app instance for testing."""
        try:
            return VisualizerApp()
        except Exception:
            pytest.skip("GUI test requires display")

    def test_app_initialization(self, app):
        """Test that app initializes properly."""
        assert app.root is not None
        assert app.current_controller is not None
