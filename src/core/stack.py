"""Stack data structure implementation."""


class Stack:
    """A Last-In-First-Out (LIFO) data structure."""

    def __init__(self):
        """Initialize an empty stack."""
        self._items = []

    def push(self, value):
        """Add an element to the top of the stack.
        
        Args:
            value: The value to push onto the stack.
        """
        self._items.append(value)

    def pop(self):
        """Remove and return the top element of the stack.
        
        Returns:
            The value at the top of the stack.
            
        Raises:
            IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def peek(self):
        """Return the top element without removing it.
        
        Returns:
            The value at the top of the stack.
            
        Raises:
            IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._items[-1]

    def is_empty(self):
        """Check if the stack is empty.
        
        Returns:
            True if the stack is empty, False otherwise.
        """
        return len(self._items) == 0

    def size(self):
        """Get the number of elements in the stack.
        
        Returns:
            The number of elements in the stack.
        """
        return len(self._items)

    def get_items(self):
        """Get a copy of all items in the stack (from bottom to top).
        
        Returns:
            A list of items in the stack.
        """
        return self._items.copy()

    def clear(self):
        """Remove all elements from the stack."""
        self._items.clear()
