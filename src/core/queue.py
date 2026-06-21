"""Queue data structure implementation."""

from collections import deque


class Queue:
    """A First-In-First-Out (FIFO) data structure."""

    def __init__(self):
        """Initialize an empty queue."""
        self._items = deque()

    def enqueue(self, value):
        """Add an element to the rear of the queue.
        
        Args:
            value: The value to add to the queue.
        """
        self._items.append(value)

    def dequeue(self):
        """Remove and return the front element of the queue.
        
        Returns:
            The value at the front of the queue.
            
        Raises:
            IndexError: If the queue is empty.
        """
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self._items.popleft()

    def front(self):
        """Return the front element without removing it.
        
        Returns:
            The value at the front of the queue.
            
        Raises:
            IndexError: If the queue is empty.
        """
        if self.is_empty():
            raise IndexError("front of empty queue")
        return self._items[0]

    def is_empty(self):
        """Check if the queue is empty.
        
        Returns:
            True if the queue is empty, False otherwise.
        """
        return len(self._items) == 0

    def size(self):
        """Get the number of elements in the queue.
        
        Returns:
            The number of elements in the queue.
        """
        return len(self._items)

    def get_items(self):
        """Get a copy of all items in the queue (front to rear).
        
        Returns:
            A list of items in the queue.
        """
        return list(self._items)

    def clear(self):
        """Remove all elements from the queue."""
        self._items.clear()
