"""Integration tests for Queue Controller."""

import pytest
from src.controllers.queue_controller import QueueController


class TestQueueController:
    """Integration tests for QueueController."""

    @pytest.fixture
    def controller(self):
        """Create a fresh controller for each test."""
        return QueueController()

    def test_enqueue_operation(self, controller):
        """Test enqueue operation."""
        result = controller.perform_operation('enqueue', 5)
        assert result['success'] is True
        assert controller.get_data_structure().front() == 5

    def test_dequeue_operation(self, controller):
        """Test dequeue operation."""
        controller.perform_operation('enqueue', 5)
        result = controller.perform_operation('dequeue')
        assert result['success'] is True
        assert controller.get_data_structure().is_empty()

    def test_undo_operation(self, controller):
        """Test undo functionality."""
        controller.perform_operation('enqueue', 5)
        controller.perform_operation('enqueue', 3)
        assert controller.get_data_structure().size() == 2
        
        result = controller.undo()
        assert result['success'] is True
        assert controller.get_data_structure().size() == 1
        assert controller.get_data_structure().front() == 5
