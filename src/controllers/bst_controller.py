"""Controller for Binary Search Tree operations."""

from core.bst import BinarySearchTree
from visualization.bst_drawer import BSTDrawer
from .base_controller import BaseController
import copy


class BSTController(BaseController):
    """Controller for managing BST operations."""

    def __init__(self):
        """Initialize the BST controller."""
        self.bst = BinarySearchTree()
        super().__init__()
        self._current_state = copy.deepcopy(self.bst)
        self.drawer = None

    def perform_operation(self, operation, value=None):
        """Perform a BST operation.
        
        Args:
            operation: The operation to perform ('insert', 'delete', 'search', 'clear', 'inorder').
            value: The value to use for the operation.
            
        Returns:
            A dict with 'success' and 'message' keys.
        """
        self._save_state()
        
        try:
            if operation == 'insert':
                if value is None:
                    return {'success': False, 'message': 'Value required for insert'}
                success = self.bst.insert(value)
                if success:
                    return {'success': True, 'message': f'Inserted {value}'}
                else:
                    self._history.pop()
                    return {'success': False, 'message': f'Value {value} already exists'}
            
            elif operation == 'delete':
                if value is None:
                    return {'success': False, 'message': 'Value required for delete'}
                success = self.bst.delete(value)
                if success:
                    return {'success': True, 'message': f'Deleted {value}'}
                else:
                    self._history.pop()
                    return {'success': False, 'message': f'Value {value} not found'}
            
            elif operation == 'search':
                if value is None:
                    return {'success': False, 'message': 'Value required for search'}
                found = self.bst.search(value)
                self._history.pop()  # Don't save state for search
                if found:
                    return {'success': True, 'message': f'Found {value} in tree'}
                else:
                    return {'success': True, 'message': f'Value {value} not found'}
            
            elif operation == 'inorder':
                traversal = self.bst.inorder_traversal()
                self._history.pop()  # Don't save state for traversal
                return {'success': True, 'message': f'Inorder: {traversal}'}
            
            elif operation == 'clear':
                self.bst.clear()
                return {'success': True, 'message': 'Tree cleared'}
            
            else:
                self._history.pop()
                return {'success': False, 'message': f'Unknown operation: {operation}'}
        
        except Exception as e:
            self._history.pop()
            return {'success': False, 'message': str(e)}
        
        finally:
            self._current_state = copy.deepcopy(self.bst)

    def undo(self):
        """Undo the last operation.
        
        Returns:
            A dict with 'success' and 'message' keys.
        """
        if len(self._history) > 1:
            self._history.pop()
            self.bst = copy.deepcopy(self._history[-1])
            self._current_state = copy.deepcopy(self.bst)
            return {'success': True, 'message': 'Operation undone'}
        else:
            return {'success': False, 'message': 'Nothing to undo'}

    def get_data_structure(self):
        """Get the current BST.
        
        Returns:
            The BinarySearchTree object.
        """
        return self.bst

    def get_drawer(self, canvas):
        """Get the BST drawer.
        
        Args:
            canvas: The canvas to draw on.
            
        Returns:
            A BSTDrawer object.
        """
        return BSTDrawer(canvas)
