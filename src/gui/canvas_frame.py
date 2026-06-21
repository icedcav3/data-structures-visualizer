"""Canvas frame for visualization."""

import tkinter as tk


class CanvasFrame(tk.Frame):
    """Frame containing the canvas for visualizations."""

    def __init__(self, parent):
        """Initialize the canvas frame.
        
        Args:
            parent: The parent widget.
        """
        super().__init__(parent, bg="#f0f0f0", relief=tk.SUNKEN, bd=1)
        
        self.canvas = tk.Canvas(
            self,
            bg="#ffffff",
            relief=tk.FLAT,
            bd=0,
            highlightthickness=0
        )
        self.canvas.pack(fill=tk.BOTH, expand=True)
        
        # Bind resize event
        self.bind("<Configure>", self._on_resize)

    def _on_resize(self, event):
        """Handle canvas resize.
        
        Args:
            event: The configure event.
        """
        self.canvas.winfo_width()
        self.canvas.winfo_height()
