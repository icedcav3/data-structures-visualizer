"""Unit tests for Binary Search Tree implementation."""

import pytest
from src.core.bst import BinarySearchTree


class TestBST:
    """Test cases for Binary Search Tree data structure."""

    @pytest.fixture
    def bst(self):
        """Create a fresh BST for each test."""
        return BinarySearchTree()

    def test_insert_single_element(self, bst):
        """Test inserting a single element."""
        assert bst.insert(5) is True
        assert bst.root.value == 5

    def test_insert_multiple_elements(self, bst):
        """Test inserting multiple elements."""
        assert bst.insert(5) is True
        assert bst.insert(3) is True
        assert bst.insert(7) is True
        assert bst.root.value == 5
        assert bst.root.left.value == 3
        assert bst.root.right.value == 7

    def test_insert_duplicate(self, bst):
        """Test that duplicate values are not inserted."""
        assert bst.insert(5) is True
        assert bst.insert(5) is False

    def test_search_existing(self, bst):
        """Test searching for existing element."""
        bst.insert(5)
        bst.insert(3)
        bst.insert(7)
        assert bst.search(3) is True
        assert bst.search(5) is True
        assert bst.search(7) is True

    def test_search_nonexistent(self, bst):
        """Test searching for non-existent element."""
        bst.insert(5)
        bst.insert(3)
        assert bst.search(7) is False

    def test_search_empty_tree(self, bst):
        """Test searching in empty tree."""
        assert bst.search(5) is False

    def test_delete_leaf_node(self, bst):
        """Test deleting a leaf node."""
        bst.insert(5)
        bst.insert(3)
        bst.insert(7)
        assert bst.delete(3) is True
        assert bst.search(3) is False
        assert bst.search(5) is True

    def test_delete_node_with_one_child(self, bst):
        """Test deleting a node with one child."""
        bst.insert(5)
        bst.insert(3)
        bst.insert(2)
        assert bst.delete(3) is True
        assert bst.search(3) is False
        assert bst.search(2) is True

    def test_delete_node_with_two_children(self, bst):
        """Test deleting a node with two children."""
        bst.insert(5)
        bst.insert(3)
        bst.insert(7)
        bst.insert(6)
        bst.insert(8)
        assert bst.delete(5) is True
        assert bst.search(5) is False
        assert bst.search(3) is True
        assert bst.search(7) is True

    def test_delete_nonexistent(self, bst):
        """Test deleting non-existent element."""
        bst.insert(5)
        assert bst.delete(10) is False

    def test_inorder_traversal(self, bst):
        """Test inorder traversal."""
        bst.insert(5)
        bst.insert(3)
        bst.insert(7)
        bst.insert(2)
        bst.insert(4)
        result = bst.inorder_traversal()
        assert result == [2, 3, 4, 5, 7]

    def test_preorder_traversal(self, bst):
        """Test preorder traversal."""
        bst.insert(5)
        bst.insert(3)
        bst.insert(7)
        result = bst.preorder_traversal()
        assert result == [5, 3, 7]

    def test_postorder_traversal(self, bst):
        """Test postorder traversal."""
        bst.insert(5)
        bst.insert(3)
        bst.insert(7)
        result = bst.postorder_traversal()
        assert result == [3, 7, 5]

    def test_is_empty(self, bst):
        """Test empty state check."""
        assert bst.is_empty() is True
        bst.insert(5)
        assert bst.is_empty() is False

    def test_clear(self, bst):
        """Test clearing the tree."""
        bst.insert(5)
        bst.insert(3)
        bst.clear()
        assert bst.is_empty() is True
