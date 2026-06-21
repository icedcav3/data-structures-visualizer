"""Unit tests for Queue implementation."""

import pytest
from src.core.queue import Queue


class TestQueue:
    """Test cases for Queue data structure."""

    @pytest.fixture
    def queue(self):
        """Create a fresh queue for each test."""
        return Queue()

    def test_enqueue_single_element(self, queue):
        """Test enqueueing a single element."""
        queue.enqueue(5)
        assert queue.front() == 5
        assert queue.size() == 1

    def test_enqueue_multiple_elements(self, queue):
        """Test enqueueing multiple elements."""
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        assert queue.front() == 1
        assert queue.size() == 3

    def test_dequeue_single_element(self, queue):
        """Test dequeuing a single element."""
        queue.enqueue(5)
        result = queue.dequeue()
        assert result == 5
        assert queue.is_empty()

    def test_dequeue_multiple_elements(self, queue):
        """Test dequeuing multiple elements in FIFO order."""
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        
        assert queue.dequeue() == 1
        assert queue.dequeue() == 2
        assert queue.dequeue() == 3
        assert queue.is_empty()

    def test_dequeue_from_empty_queue(self, queue):
        """Test that dequeuing from empty queue raises error."""
        with pytest.raises(IndexError):
            queue.dequeue()

    def test_front(self, queue):
        """Test getting front element without removing."""
        queue.enqueue(5)
        assert queue.front() == 5
        assert queue.size() == 1  # Size unchanged

    def test_front_empty_queue(self, queue):
        """Test that getting front from empty queue raises error."""
        with pytest.raises(IndexError):
            queue.front()

    def test_is_empty(self, queue):
        """Test empty state check."""
        assert queue.is_empty()
        queue.enqueue(1)
        assert not queue.is_empty()
        queue.dequeue()
        assert queue.is_empty()

    def test_size(self, queue):
        """Test size tracking."""
        assert queue.size() == 0
        queue.enqueue(1)
        assert queue.size() == 1
        queue.enqueue(2)
        assert queue.size() == 2
        queue.dequeue()
        assert queue.size() == 1

    def test_get_items(self, queue):
        """Test getting items list."""
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        items = queue.get_items()
        assert items == [1, 2, 3]
        assert isinstance(items, list)

    def test_clear(self, queue):
        """Test clearing the queue."""
        queue.enqueue(1)
        queue.enqueue(2)
        queue.clear()
        assert queue.is_empty()
        assert queue.size() == 0
