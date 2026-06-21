"""Controller for Stack operations."""

from core.stack import Stack
from visualization.stack_drawer import StackDrawer
from .base_controller import BaseController
import copy


class StackController(BaseController):
    """Controller for managing Stack operations."""

    def __init__(self):
        """Initialize the stack controller."""
        self.stack = Stack()
        super().__init__()
        self._current_state = copy.deepcopy(self.stack)

    def perform_operation(self, operation, value=None):
        """Perform a stack operation.
        
        Args:
            operation: The operation to perform ('push', 'pop', 'peek', 'clear').
            value: The value for push operations.
            
        Returns:
            A dict with 'success' and 'message' keys.
        """
        self._save_state()
        
        try:
            if operation == 'push':
                if value is None:
                    return {'success': False, 'message': 'Value required for push'}
                self.stack.push(value)
                return {'success': True, 'message': f'Pushed {value}'}
            
            elif operation == 'pop':
                if self.stack.is_empty():
                    # Undo the state save since operation failed
                    self._history.pop()
                    return {'success': False, 'message': 'Stack is empty'}
                value = self.stack.pop()
                return {'success': True, 'message': f'Popped {value}'}
            
            elif operation == 'peek':
                if self.stack.is_empty():
                    self._history.pop()
                    return {'success': False, 'message': 'Stack is empty'}
                value = self.stack.peek()
                self._history.pop()  # Don't save state for peek
                return {'success': True, 'message': f'Top element: {value}'}
            
            elif operation == 'clear':
                self.stack.clear()
                return {'success': True, 'message': 'Stack cleared'}
            
            else:
                self._history.pop()
                return {'success': False, 'message': f'Unknown operation: {operation}'}
        
        except Exception as e:
            self._history.pop()
            return {'success': False, 'message': str(e)}
        
        finally:
            self._current_state = copy.deepcopy(self.stack)

    def undo(self):
        """Undo the last operation.
        
        Returns:
            A dict with 'success' and 'message' keys.
        """
        if len(self._history) > 1:
            self._history.pop()
            self.stack = copy.deepcopy(self._history[-1])
            self._current_state = copy.deepcopy(self.stack)
            return {'success': True, 'message': 'Operation undone'}
        else:
            return {'success': False, 'message': 'Nothing to undo'}

    def get_data_structure(self):
        """Get the current stack.
        
        Returns:
            The Stack object.
        """
        return self.stack

    def get_drawer(self, canvas):
        """Get the stack drawer.
        
        Args:
            canvas: The canvas to draw on.
            
        Returns:
            A StackDrawer object.
        """
        return StackDrawer(canvas)
