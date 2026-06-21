"""Operation log display."""

import tkinter as tk
from tkinter import ttk
from datetime import datetime


class OperationLog(ttk.Frame):
    """Display and manage operation history."""

    def __init__(self, parent, on_undo=None):
        """Initialize the operation log.
        
        Args:
            parent: The parent widget.
            on_undo: Callback for undo button press.
        """
        super().__init__(parent, relief=tk.SUNKEN, bd=1)
        
        self.on_undo = on_undo
        self.operations = []
        
        # Listbox for operations
        listbox_frame = ttk.Frame(self)
        listbox_frame.pack(fill=tk.BOTH, expand=True)
        
        self.listbox = tk.Listbox(
            listbox_frame,
            height=8,
            font=("Courier", 10),
            bg="#f8f8f8",
            relief=tk.FLAT,
            bd=1
        )
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(listbox_frame, orient=tk.VERTICAL, command=self.listbox.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.listbox.config(yscrollcommand=scrollbar.set)
        
        # Control buttons
        button_frame = ttk.Frame(self)
        button_frame.pack(fill=tk.X, padx=5, pady=5)
        
        ttk.Button(
            button_frame,
            text="Undo Last",
            command=self._on_undo_button
        ).pack(side=tk.LEFT, padx=2)
        
        ttk.Button(
            button_frame,
            text="Clear Log",
            command=self.clear
        ).pack(side=tk.LEFT, padx=2)

    def add_operation(self, operation):
        """Add an operation to the log.
        
        Args:
            operation: Description of the operation.
        """
        timestamp = datetime.now().strftime("%H:%M:%S")
        log_entry = f"[{timestamp}] {operation}"
        self.operations.append(operation)
        self.listbox.insert(tk.END, log_entry)
        self.listbox.see(tk.END)  # Auto-scroll to bottom

    def clear(self):
        """Clear the operation log."""
        self.listbox.delete(0, tk.END)
        self.operations.clear()

    def _on_undo_button(self):
        """Handle undo button press."""
        if self.operations:
            self.operations.pop()
            self.listbox.delete(tk.END)  # Remove last item (accounting for 0-indexing)
            if self.on_undo:
                self.on_undo()
