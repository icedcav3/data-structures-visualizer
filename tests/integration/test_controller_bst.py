"""Integration tests for BST Controller."""

import pytest
from src.controllers.bst_controller import BSTController


class TestBSTController:
    """Integration tests for BSTController."""

    @pytest.fixture
    def controller(self):
        """Create a fresh controller for each test."""
        return BSTController()

    def test_insert_operation(self, controller):
        """Test insert operation."""
        result = controller.perform_operation('insert', 5)
        assert result['success'] is True
        assert controller.get_data_structure().search(5) is True

    def test_search_operation(self, controller):
        """Test search operation."""
        controller.perform_operation('insert', 5)
        result = controller.perform_operation('search', 5)
        assert result['success'] is True
        assert "Found" in result['message']

    def test_delete_operation(self, controller):
        """Test delete operation."""
        controller.perform_operation('insert', 5)
        result = controller.perform_operation('delete', 5)
        assert result['success'] is True
        assert controller.get_data_structure().search(5) is False

    def test_undo_operation(self, controller):
        """Test undo functionality."""
        controller.perform_operation('insert', 5)
        controller.perform_operation('insert', 3)
        assert controller.get_data_structure().search(3) is True
        
        result = controller.undo()
        assert result['success'] is True
        assert controller.get_data_structure().search(3) is False
        assert controller.get_data_structure().search(5) is True
