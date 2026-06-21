"""Status bar for messages."""

import tkinter as tk
from tkinter import ttk


class StatusBar(ttk.Frame):
    """Status bar for displaying messages and errors."""

    def __init__(self, parent):
        """Initialize the status bar.
        
        Args:
            parent: The parent widget.
        """
        super().__init__(parent, relief=tk.SUNKEN, bd=1)
        
        self.label = ttk.Label(
            self,
            text="Ready",
            foreground="#2c3e50",
            font=("Arial", 10)
        )
        self.label.pack(side=tk.LEFT, padx=5, pady=2)

    def set_message(self, message):
        """Set a status message.
        
        Args:
            message: The message to display.
        """
        self.label.config(text=message, foreground="#2c3e50")

    def set_error(self, message):
        """Set an error message.
        
        Args:
            message: The error message to display.
        """
        self.label.config(text=f"Error: {message}", foreground="#e74c3c")

    def set_warning(self, message):
        """Set a warning message.
        
        Args:
            message: The warning message to display.
        """
        self.label.config(text=f"Warning: {message}", foreground="#f39c12")
