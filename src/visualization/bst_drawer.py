"""Binary Search Tree visualization drawer."""

import math
from .base_drawer import BaseDrawer


class BSTDrawer(BaseDrawer):
    """Drawer for visualizing a Binary Search Tree data structure."""

    def __init__(self, canvas):
        """Initialize the BST drawer.
        
        Args:
            canvas: The tkinter Canvas widget to draw on.
        """
        super().__init__(canvas)
        self.search_path = set()  # Track nodes in search path
        self.highlight_node = None  # Track node to highlight

    def draw(self, bst):
        """Draw the BST on the canvas.
        
        Args:
            bst: The BinarySearchTree object to visualize.
        """
        self.clear()
        
        if bst.is_empty():
            self.draw_text(
                self.canvas_width // 2,
                self.canvas_height // 2,
                "Empty Tree",
                font=self.FONT_LARGE,
                fill="#7f8c8d"
            )
            return
        
        # Calculate tree dimensions
        height = self._get_height(bst.root)
        width = 2 ** (height + 1) * self.SPACING
        
        # Draw the tree starting from root
        self._draw_node(
            bst.root,
            self.canvas_width // 2,
            50,
            width // 2
        )

    def _draw_node(self, node, x, y, offset):
        """Recursively draw a node and its children.
        
        Args:
            node: The current node to draw.
            x: X coordinate of the node.
            y: Y coordinate of the node.
            offset: Horizontal offset for positioning children.
        """
        if node is None:
            return
        
        # Draw edges to children first (so they appear behind nodes)
        if node.left is not None:
            left_x = x - offset
            left_y = y + 80
            self.draw_line(x, y + self.NODE_RADIUS, left_x, left_y - self.NODE_RADIUS,
                          fill=self.COLOR_EDGE, width=2)
            self._draw_node(node.left, left_x, left_y, offset // 2)
        
        if node.right is not None:
            right_x = x + offset
            right_y = y + 80
            self.draw_line(x, y + self.NODE_RADIUS, right_x, right_y - self.NODE_RADIUS,
                          fill=self.COLOR_EDGE, width=2)
            self._draw_node(node.right, right_x, right_y, offset // 2)
        
        # Determine node color
        if node.value == self.highlight_node:
            fill_color = self.COLOR_HIGHLIGHT
        elif node.value in self.search_path:
            fill_color = self.COLOR_SEARCH
        else:
            fill_color = self.COLOR_NODE
        
        # Draw the node circle
        self.draw_circle(x, y, radius=self.NODE_RADIUS,
                        fill=fill_color, outline="#2c3e50", width_outline=2)
        
        # Draw the value
        self.draw_text(x, y, str(node.value), font=self.FONT_DEFAULT,
                      fill=self.COLOR_TEXT)

    def _get_height(self, node):
        """Get the height of the tree.
        
        Args:
            node: The current node.
            
        Returns:
            The height of the subtree rooted at this node.
        """
        if node is None:
            return 0
        return 1 + max(self._get_height(node.left), self._get_height(node.right))

    def highlight_search_path(self, path):
        """Set the nodes to highlight as part of a search path.
        
        Args:
            path: A list of node values that form the search path.
        """
        self.search_path = set(path)

    def highlight_node_value(self, value):
        """Set a node to highlight.
        
        Args:
            value: The value of the node to highlight.
        """
        self.highlight_node = value

    def clear_highlights(self):
        """Clear all highlights."""
        self.search_path = set()
        self.highlight_node = None
