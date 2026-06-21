"""Base controller class."""

from abc import ABC, abstractmethod
import copy


class BaseController(ABC):
    """Abstract base class for data structure controllers."""

    def __init__(self):
        """Initialize the controller."""
        self._history = []
        self._current_state = None
        self._save_state()

    def _save_state(self):
        """Save the current state for undo."""
        if self._current_state is not None:
            self._history.append(copy.deepcopy(self._current_state))

    @abstractmethod
    def perform_operation(self, operation, value=None):
        """Perform an operation on the data structure.
        
        Args:
            operation: The operation to perform.
            value: The value to use (if applicable).
            
        Returns:
            A dict with 'success' and 'message' keys.
        """
        pass

    def undo(self):
        """Undo the last operation.
        
        Returns:
            A dict with 'success' and 'message' keys.
        """
        if len(self._history) > 1:
            self._history.pop()  # Remove current state
            self._current_state = copy.deepcopy(self._history[-1])
            return {'success': True, 'message': 'Operation undone'}
        else:
            return {'success': False, 'message': 'Nothing to undo'}

    @abstractmethod
    def get_data_structure(self):
        """Get the current data structure.
        
        Returns:
            The data structure object.
        """
        pass

    @abstractmethod
    def get_drawer(self, canvas):
        """Get the appropriate drawer for visualization.
        
        Args:
            canvas: The canvas to draw on.
            
        Returns:
            A Drawer object.
        """
        pass
