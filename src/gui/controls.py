"""Control panel for user input."""

import tkinter as tk
from tkinter import ttk


class ControlPanel(ttk.Frame):
    """Control panel for selecting structure and performing operations."""

    def __init__(self, parent, on_structure_changed=None, on_operation=None):
        """Initialize the control panel.
        
        Args:
            parent: The parent widget.
            on_structure_changed: Callback for structure selection change.
            on_operation: Callback for operation button press.
        """
        super().__init__(parent, relief=tk.SUNKEN, bd=1)
        
        self.on_structure_changed = on_structure_changed
        self.on_operation = on_operation
        
        self.current_structure = None
        self.operation_buttons = {}
        
        # Structure selection
        ttk.Label(self, text="Select Structure", font=("Arial", 12, "bold")).pack(pady=10)
        
        structure_frame = ttk.Frame(self)
        structure_frame.pack(fill=tk.X, padx=10, pady=5)
        
        self.structure_var = tk.StringVar(value="stack")
        structures = [
            ("Stack", "stack"),
            ("Queue", "queue"),
            ("BST", "bst"),
        ]
        
        for label, value in structures:
            rb = ttk.Radiobutton(
                structure_frame,
                text=label,
                variable=self.structure_var,
                value=value,
                command=self._on_structure_changed
            )
            rb.pack(anchor=tk.W, pady=5)
        
        # Value input
        ttk.Label(self, text="Value Input", font=("Arial", 12, "bold")).pack(pady=(15, 10))
        
        input_frame = ttk.Frame(self)
        input_frame.pack(fill=tk.X, padx=10, pady=5)
        
        ttk.Label(input_frame, text="Value:").pack(anchor=tk.W)
        self.value_var = tk.StringVar()
        self.value_entry = ttk.Entry(input_frame, textvariable=self.value_var, width=20)
        self.value_entry.pack(fill=tk.X, pady=5)
        
        # Operations frame
        ttk.Label(self, text="Operations", font=("Arial", 12, "bold")).pack(pady=(15, 10))
        
        self.operations_frame = ttk.Frame(self)
        self.operations_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        # Control buttons
        button_frame = ttk.Frame(self)
        button_frame.pack(fill=tk.X, padx=10, pady=10)
        
        ttk.Button(
            button_frame,
            text="Clear All",
            command=self._on_clear_all
        ).pack(side=tk.LEFT, padx=2)
        
        ttk.Button(
            button_frame,
            text="Undo",
            command=self._on_undo
        ).pack(side=tk.LEFT, padx=2)

    def _on_structure_changed(self):
        """Handle structure change."""
        new_structure = self.structure_var.get()
        if new_structure != self.current_structure:
            self.current_structure = new_structure
            self._update_operations()
            if self.on_structure_changed:
                self.on_structure_changed(new_structure)

    def _update_operations(self):
        """Update operation buttons based on selected structure."""
        # Clear existing buttons
        for widget in self.operations_frame.winfo_children():
            widget.destroy()
        self.operation_buttons.clear()
        
        operations = self._get_operations_for_structure(self.current_structure)
        
        for op_name, op_key in operations:
            needs_value = op_key in ['push', 'enqueue', 'insert', 'delete', 'search']
            
            btn = ttk.Button(
                self.operations_frame,
                text=op_name,
                command=lambda key=op_key, nv=needs_value: self._on_operation_button(key, nv)
            )
            btn.pack(fill=tk.X, pady=3)
            self.operation_buttons[op_key] = btn

    def _get_operations_for_structure(self, structure):
        """Get available operations for a structure.
        
        Args:
            structure: The structure type.
            
        Returns:
            A list of (display_name, operation_key) tuples.
        """
        operations = {
            'stack': [
                ("Push", "push"),
                ("Pop", "pop"),
                ("Peek", "peek"),
            ],
            'queue': [
                ("Enqueue", "enqueue"),
                ("Dequeue", "dequeue"),
                ("Front", "front"),
            ],
            'bst': [
                ("Insert", "insert"),
                ("Delete", "delete"),
                ("Search", "search"),
                ("Inorder", "inorder"),
            ],
        }
        return operations.get(structure, [])

    def _on_operation_button(self, operation, needs_value):
        """Handle operation button press.
        
        Args:
            operation: The operation to perform.
            needs_value: Whether the operation requires a value.
        """
        value = None
        if needs_value:
            value = self.value_var.get().strip()
            if not value:
                return  # Don't perform operation without value
            try:
                value = int(value)
            except ValueError:
                try:
                    value = float(value)
                except ValueError:
                    pass  # Keep as string
            self.value_entry.delete(0, tk.END)  # Clear input
        
        if self.on_operation:
            self.on_operation(operation, value)

    def _on_clear_all(self):
        """Handle clear all button."""
        if self.on_operation:
            self.on_operation('clear', None)

    def _on_undo(self):
        """Handle undo button."""
        if self.on_structure_changed:  # Use the parent's undo handler
            pass  # This will be handled by the app's _on_undo

    def update_for_structure(self, structure):
        """Update UI for a structure.
        
        Args:
            structure: The structure type.
        """
        self.structure_var.set(structure)
        self.current_structure = structure
        self._update_operations()
