"""Queue visualization drawer."""

from .base_drawer import BaseDrawer


class QueueDrawer(BaseDrawer):
    """Drawer for visualizing a Queue data structure."""

    def draw(self, queue):
        """Draw the queue on the canvas.
        
        Args:
            queue: The Queue object to visualize.
        """
        self.clear()
        
        items = queue.get_items()
        if not items:
            self.draw_text(
                self.canvas_width // 2,
                self.canvas_height // 2,
                "Empty Queue",
                font=self.FONT_LARGE,
                fill="#7f8c8d"
            )
            return
        
        # Calculate dimensions
        box_width = self.NODE_WIDTH + 20
        box_height = self.NODE_HEIGHT + 20
        total_width = len(items) * (box_width + 10) + self.PADDING * 2
        
        start_x = max(self.PADDING, (self.canvas_width - total_width) // 2)
        start_y = self.canvas_height // 2
        
        # Draw queue boxes from front to rear (left to right)
        for i, value in enumerate(items):
            x = start_x + i * (box_width + 10) + box_width // 2
            
            # Highlight front element
            fill_color = self.COLOR_HIGHLIGHT if i == 0 else (
                self.COLOR_SEARCH if i == len(items) - 1 else self.COLOR_NODE
            )
            
            # Draw the box
            self.draw_rectangle(
                x, start_y, box_width, box_height,
                fill=fill_color, outline="#2c3e50", width_outline=2
            )
            
            # Draw the value
            self.draw_text(
                x, start_y,
                str(value),
                font=self.FONT_DEFAULT,
                fill=self.COLOR_TEXT
            )
            
            # Draw position label
            label = "Front" if i == 0 else ("Rear" if i == len(items) - 1 else "")
            if label:
                self.draw_text(
                    x, start_y + box_height // 2 + 25,
                    label,
                    font=self.FONT_SMALL,
                    fill="#2c3e50"
                )
        
        # Draw arrows between elements
        for i in range(len(items) - 1):
            x1 = start_x + (i + 1) * (box_width + 10) - 5
            x2 = start_x + (i + 1) * (box_width + 10) + 5
            y = start_y
            self.draw_line(x1, y, x2, y, fill="#2c3e50", width=2)
            # Arrow head
            self.draw_text(x1 + 2, y - 8, "→", font=self.FONT_LARGE, fill="#2c3e50")
        
        # Draw size info
        self.draw_text(
            self.canvas_width - 60, 20,
            f"Size: {queue.size()}",
            font=self.FONT_SMALL,
            fill="#2c3e50"
        )
