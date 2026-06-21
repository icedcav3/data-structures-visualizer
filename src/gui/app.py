"""Main application window."""

import tkinter as tk
from tkinter import ttk
from pathlib import Path

from .controls import ControlPanel
from .canvas_frame import CanvasFrame
from .operation_log import OperationLog
from .status_bar import StatusBar
from controllers.stack_controller import StackController
from controllers.queue_controller import QueueController
from controllers.bst_controller import BSTController
from persistence.config import Config


class VisualizerApp:
    """Main application window for the Data Structures Visualizer."""

    def __init__(self):
        """Initialize the application."""
        self.root = tk.Tk()
        self.root.title("Data Structures Visualizer")
        self.root.geometry("1200x800")
        
        # Initialize configuration
        self.config = Config()
        
        # Create controllers
        self.controllers = {
            'stack': StackController(),
            'queue': QueueController(),
            'bst': BSTController(),
        }
        
        self.current_controller = None
        
        # Setup UI
        self._setup_ui()
        
    def _setup_ui(self):
        """Set up the user interface."""
        # Create main frames
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Left panel - Controls
        left_frame = ttk.Frame(main_frame)
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=False, padx=5)
        
        self.control_panel = ControlPanel(
            left_frame,
            on_structure_changed=self._on_structure_changed,
            on_operation=self._on_operation
        )
        
        # Right panel - Visualization and Log
        right_frame = ttk.Frame(main_frame)
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=5)
        
        # Canvas for visualization
        canvas_label = ttk.Label(right_frame, text="Visualization", font=("Arial", 12, "bold"))
        canvas_label.pack(anchor=tk.W, pady=(0, 5))
        
        self.canvas_frame = CanvasFrame(right_frame)
        self.canvas_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        
        # Operation log
        log_label = ttk.Label(right_frame, text="Operation Log", font=("Arial", 12, "bold"))
        log_label.pack(anchor=tk.W, pady=(0, 5))
        
        self.operation_log = OperationLog(
            right_frame,
            on_undo=self._on_undo
        )
        self.operation_log.pack(fill=tk.BOTH, expand=False, pady=(0, 10))
        
        # Status bar
        self.status_bar = StatusBar(self.root)
        self.status_bar.pack(fill=tk.X, side=tk.BOTTOM)
        
        # Initialize with default structure
        self._on_structure_changed('stack')

    def _on_structure_changed(self, structure_type):
        """Handle structure type change.
        
        Args:
            structure_type: The type of structure ('stack', 'queue', or 'bst').
        """
        self.current_controller = self.controllers[structure_type]
        self.control_panel.update_for_structure(structure_type)
        self.operation_log.clear()
        self._redraw()
        self.status_bar.set_message(f"Switched to {structure_type.upper()}")

    def _on_operation(self, operation, value=None):
        """Handle operation button press.
        
        Args:
            operation: The operation to perform (e.g., 'push', 'pop').
            value: The value to use for the operation (if applicable).
        """
        if not self.current_controller:
            return
        
        try:
            result = self.current_controller.perform_operation(operation, value)
            if result['success']:
                self.operation_log.add_operation(f"{operation.upper()}: {value}" if value else operation.upper())
                self._redraw()
                self.status_bar.set_message(result.get('message', f"Operation completed: {operation}"))
            else:
                self.status_bar.set_error(result.get('message', f"Operation failed: {operation}"))
        except Exception as e:
            self.status_bar.set_error(str(e))

    def _on_undo(self):
        """Handle undo operation."""
        if not self.current_controller:
            return
        
        try:
            result = self.current_controller.undo()
            if result['success']:
                self._redraw()
                self.status_bar.set_message("Operation undone")
            else:
                self.status_bar.set_error("Nothing to undo")
        except Exception as e:
            self.status_bar.set_error(str(e))

    def _redraw(self):
        """Redraw the visualization."""
        if self.current_controller:
            drawer = self.current_controller.get_drawer(self.canvas_frame.canvas)
            data_structure = self.current_controller.get_data_structure()
            drawer.draw(data_structure)

    def run(self):
        """Run the application."""
        self.root.mainloop()
