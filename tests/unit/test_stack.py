"""Unit tests for Stack implementation."""

import pytest
from src.core.stack import Stack


class TestStack:
    """Test cases for Stack data structure."""

    @pytest.fixture
    def stack(self):
        """Create a fresh stack for each test."""
        return Stack()

    def test_push_single_element(self, stack):
        """Test pushing a single element."""
        stack.push(5)
        assert stack.peek() == 5
        assert stack.size() == 1

    def test_push_multiple_elements(self, stack):
        """Test pushing multiple elements."""
        stack.push(1)
        stack.push(2)
        stack.push(3)
        assert stack.peek() == 3
        assert stack.size() == 3

    def test_pop_single_element(self, stack):
        """Test popping a single element."""
        stack.push(5)
        result = stack.pop()
        assert result == 5
        assert stack.is_empty()

    def test_pop_multiple_elements(self, stack):
        """Test popping multiple elements in LIFO order."""
        stack.push(1)
        stack.push(2)
        stack.push(3)
        
        assert stack.pop() == 3
        assert stack.pop() == 2
        assert stack.pop() == 1
        assert stack.is_empty()

    def test_pop_from_empty_stack(self, stack):
        """Test that popping from empty stack raises error."""
        with pytest.raises(IndexError):
            stack.pop()

    def test_peek(self, stack):
        """Test peeking without removing."""
        stack.push(5)
        assert stack.peek() == 5
        assert stack.size() == 1  # Size unchanged

    def test_peek_empty_stack(self, stack):
        """Test that peeking empty stack raises error."""
        with pytest.raises(IndexError):
            stack.peek()

    def test_is_empty(self, stack):
        """Test empty state check."""
        assert stack.is_empty()
        stack.push(1)
        assert not stack.is_empty()
        stack.pop()
        assert stack.is_empty()

    def test_size(self, stack):
        """Test size tracking."""
        assert stack.size() == 0
        stack.push(1)
        assert stack.size() == 1
        stack.push(2)
        assert stack.size() == 2
        stack.pop()
        assert stack.size() == 1

    def test_get_items(self, stack):
        """Test getting items list."""
        stack.push(1)
        stack.push(2)
        stack.push(3)
        items = stack.get_items()
        assert items == [1, 2, 3]
        assert isinstance(items, list)

    def test_clear(self, stack):
        """Test clearing the stack."""
        stack.push(1)
        stack.push(2)
        stack.clear()
        assert stack.is_empty()
        assert stack.size() == 0
