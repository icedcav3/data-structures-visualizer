"""Base drawer class with common visualization utilities."""

from abc import ABC, abstractmethod


class BaseDrawer(ABC):
    """Abstract base class for data structure visualization."""

    # Color constants
    COLOR_BACKGROUND = "#f0f0f0"
    COLOR_NODE = "#3498db"
    COLOR_NODE_HOVER = "#2980b9"
    COLOR_TEXT = "#ffffff"
    COLOR_EDGE = "#34495e"
    COLOR_HIGHLIGHT = "#e74c3c"
    COLOR_SEARCH = "#f39c12"
    
    # Font constants
    FONT_DEFAULT = ("Arial", 12)
    FONT_LARGE = ("Arial", 14, "bold")
    FONT_SMALL = ("Arial", 10)
    
    # Dimension constants
    NODE_RADIUS = 25
    NODE_WIDTH = 50
    NODE_HEIGHT = 40
    PADDING = 20
    SPACING = 60

    def __init__(self, canvas):
        """Initialize the drawer with a canvas.
        
        Args:
            canvas: The tkinter Canvas widget to draw on.
        """
        self.canvas = canvas
        self.canvas_width = canvas.winfo_width()
        self.canvas_height = canvas.winfo_height()

    @abstractmethod
    def draw(self, data_structure):
        """Draw the data structure on the canvas.
        
        Args:
            data_structure: The data structure to visualize.
        """
        pass

    def clear(self):
        """Clear the canvas."""
        self.canvas.delete("all")

    def draw_rectangle(self, x, y, width, height, fill="#3498db", outline="#2c3e50", width_outline=2):
        """Draw a rectangle on the canvas.
        
        Args:
            x: X coordinate of the top-left corner.
            y: Y coordinate of the top-left corner.
            width: Width of the rectangle.
            height: Height of the rectangle.
            fill: Fill color.
            outline: Outline color.
            width_outline: Outline width.
            
        Returns:
            The canvas item ID.
        """
        return self.canvas.create_rectangle(
            x - width // 2, y - height // 2,
            x + width // 2, y + height // 2,
            fill=fill, outline=outline, width=width_outline
        )

    def draw_circle(self, x, y, radius=25, fill="#3498db", outline="#2c3e50", width_outline=2):
        """Draw a circle on the canvas.
        
        Args:
            x: X coordinate of the center.
            y: Y coordinate of the center.
            radius: Radius of the circle.
            fill: Fill color.
            outline: Outline color.
            width_outline: Outline width.
            
        Returns:
            The canvas item ID.
        """
        return self.canvas.create_oval(
            x - radius, y - radius,
            x + radius, y + radius,
            fill=fill, outline=outline, width=width_outline
        )

    def draw_text(self, x, y, text, font=None, fill="#ffffff"):
        """Draw text on the canvas.
        
        Args:
            x: X coordinate.
            y: Y coordinate.
            text: Text to display.
            font: Font tuple (family, size, style).
            fill: Text color.
            
        Returns:
            The canvas item ID.
        """
        if font is None:
            font = self.FONT_DEFAULT
        return self.canvas.create_text(x, y, text=str(text), font=font, fill=fill)

    def draw_line(self, x1, y1, x2, y2, fill="#34495e", width=2):
        """Draw a line on the canvas.
        
        Args:
            x1: X coordinate of the start point.
            y1: Y coordinate of the start point.
            x2: X coordinate of the end point.
            y2: Y coordinate of the end point.
            fill: Line color.
            width: Line width.
            
        Returns:
            The canvas item ID.
        """
        return self.canvas.create_line(x1, y1, x2, y2, fill=fill, width=width)
