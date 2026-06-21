"""Stack visualization drawer."""

from .base_drawer import BaseDrawer


class StackDrawer(BaseDrawer):
    """Drawer for visualizing a Stack data structure."""

    def draw(self, stack):
        """Draw the stack on the canvas.
        
        Args:
            stack: The Stack object to visualize.
        """
        self.clear()
        
        items = stack.get_items()
        if not items:
            self.draw_text(
                self.canvas_width // 2,
                self.canvas_height // 2,
                "Empty Stack",
                font=self.FONT_LARGE,
                fill="#7f8c8d"
            )
            return
        
        # Calculate starting position
        box_height = self.NODE_HEIGHT
        box_width = self.NODE_WIDTH + 40
        total_height = len(items) * (box_height + 10) + self.PADDING * 2
        
        start_y = max(self.PADDING, (self.canvas_height - total_height) // 2)
        start_x = self.canvas_width // 2
        
        # Draw stack boxes from bottom to top
        for i, value in enumerate(items):
            y = start_y + (len(items) - 1 - i) * (box_height + 10) + box_height // 2
            
            # Highlight the top element
            fill_color = self.COLOR_HIGHLIGHT if i == len(items) - 1 else self.COLOR_NODE
            
            # Draw the box
            self.draw_rectangle(
                start_x, y, box_width, box_height,
                fill=fill_color, outline="#2c3e50", width_outline=2
            )
            
            # Draw the index
            self.draw_text(
                start_x - box_width // 2 + 20, y,
                str(i),
                font=self.FONT_SMALL,
                fill=self.COLOR_TEXT
            )
            
            # Draw the value
            self.draw_text(
                start_x + 10, y,
                str(value),
                font=self.FONT_DEFAULT,
                fill=self.COLOR_TEXT
            )
        
        # Draw labels
        self.draw_text(
            start_x - box_width // 2 - 40, start_y - 20,
            f"Size: {stack.size()}",
            font=self.FONT_SMALL,
            fill="#2c3e50"
        )
