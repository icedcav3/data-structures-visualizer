"""Controller for Queue operations."""

from core.queue import Queue
from visualization.queue_drawer import QueueDrawer
from .base_controller import BaseController
import copy


class QueueController(BaseController):
    """Controller for managing Queue operations."""

    def __init__(self):
        """Initialize the queue controller."""
        self.queue = Queue()
        super().__init__()
        self._current_state = copy.deepcopy(self.queue)

    def perform_operation(self, operation, value=None):
        """Perform a queue operation.
        
        Args:
            operation: The operation to perform ('enqueue', 'dequeue', 'front', 'clear').
            value: The value for enqueue operations.
            
        Returns:
            A dict with 'success' and 'message' keys.
        """
        self._save_state()
        
        try:
            if operation == 'enqueue':
                if value is None:
                    return {'success': False, 'message': 'Value required for enqueue'}
                self.queue.enqueue(value)
                return {'success': True, 'message': f'Enqueued {value}'}
            
            elif operation == 'dequeue':
                if self.queue.is_empty():
                    self._history.pop()
                    return {'success': False, 'message': 'Queue is empty'}
                value = self.queue.dequeue()
                return {'success': True, 'message': f'Dequeued {value}'}
            
            elif operation == 'front':
                if self.queue.is_empty():
                    self._history.pop()
                    return {'success': False, 'message': 'Queue is empty'}
                value = self.queue.front()
                self._history.pop()  # Don't save state for front
                return {'success': True, 'message': f'Front element: {value}'}
            
            elif operation == 'clear':
                self.queue.clear()
                return {'success': True, 'message': 'Queue cleared'}
            
            else:
                self._history.pop()
                return {'success': False, 'message': f'Unknown operation: {operation}'}
        
        except Exception as e:
            self._history.pop()
            return {'success': False, 'message': str(e)}
        
        finally:
            self._current_state = copy.deepcopy(self.queue)

    def undo(self):
        """Undo the last operation.
        
        Returns:
            A dict with 'success' and 'message' keys.
        """
        if len(self._history) > 1:
            self._history.pop()
            self.queue = copy.deepcopy(self._history[-1])
            self._current_state = copy.deepcopy(self.queue)
            return {'success': True, 'message': 'Operation undone'}
        else:
            return {'success': False, 'message': 'Nothing to undo'}

    def get_data_structure(self):
        """Get the current queue.
        
        Returns:
            The Queue object.
        """
        return self.queue

    def get_drawer(self, canvas):
        """Get the queue drawer.
        
        Args:
            canvas: The canvas to draw on.
            
        Returns:
            A QueueDrawer object.
        """
        return QueueDrawer(canvas)
