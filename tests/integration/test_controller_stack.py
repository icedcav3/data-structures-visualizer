"""Integration tests for Stack Controller."""

import pytest
from src.controllers.stack_controller import StackController


class TestStackController:
    """Integration tests for StackController."""

    @pytest.fixture
    def controller(self):
        """Create a fresh controller for each test."""
        return StackController()

    def test_push_operation(self, controller):
        """Test push operation."""
        result = controller.perform_operation('push', 5)
        assert result['success'] is True
        assert controller.get_data_structure().peek() == 5

    def test_pop_operation(self, controller):
        """Test pop operation."""
        controller.perform_operation('push', 5)
        result = controller.perform_operation('pop')
        assert result['success'] is True
        assert controller.get_data_structure().is_empty()

    def test_undo_operation(self, controller):
        """Test undo functionality."""
        controller.perform_operation('push', 5)
        controller.perform_operation('push', 3)
        assert controller.get_data_structure().size() == 2
        
        result = controller.undo()
        assert result['success'] is True
        assert controller.get_data_structure().size() == 1
        assert controller.get_data_structure().peek() == 5

    def test_clear_operation(self, controller):
        """Test clear operation."""
        controller.perform_operation('push', 1)
        controller.perform_operation('push', 2)
        result = controller.perform_operation('clear')
        assert result['success'] is True
        assert controller.get_data_structure().is_empty()
