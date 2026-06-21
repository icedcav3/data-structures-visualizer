"""Binary Search Tree (BST) implementation."""


class TreeNode:
    """A node in the binary search tree."""

    def __init__(self, value):
        """Initialize a tree node.
        
        Args:
            value: The value to store in the node.
        """
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    """A Binary Search Tree (BST) data structure."""

    def __init__(self):
        """Initialize an empty binary search tree."""
        self.root = None

    def insert(self, value):
        """Insert a value into the BST.
        
        Args:
            value: The value to insert.
            
        Returns:
            True if the value was inserted, False if it already exists.
        """
        if self.root is None:
            self.root = TreeNode(value)
            return True
        return self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        """Recursively insert a value into the BST.
        
        Args:
            node: The current node in the recursion.
            value: The value to insert.
            
        Returns:
            True if the value was inserted, False otherwise.
        """
        if value == node.value:
            return False  # Duplicate values not allowed
        
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
                return True
            return self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = TreeNode(value)
                return True
            return self._insert_recursive(node.right, value)

    def search(self, value):
        """Search for a value in the BST.
        
        Args:
            value: The value to search for.
            
        Returns:
            True if the value is found, False otherwise.
        """
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        """Recursively search for a value in the BST.
        
        Args:
            node: The current node in the recursion.
            value: The value to search for.
            
        Returns:
            True if the value is found, False otherwise.
        """
        if node is None:
            return False
        
        if value == node.value:
            return True
        elif value < node.value:
            return self._search_recursive(node.left, value)
        else:
            return self._search_recursive(node.right, value)

    def delete(self, value):
        """Delete a value from the BST.
        
        Args:
            value: The value to delete.
            
        Returns:
            True if the value was deleted, False otherwise.
        """
        self.root, deleted = self._delete_recursive(self.root, value)
        return deleted

    def _delete_recursive(self, node, value):
        """Recursively delete a value from the BST.
        
        Args:
            node: The current node in the recursion.
            value: The value to delete.
            
        Returns:
            A tuple of (updated_node, deleted) where deleted is True if the value was deleted.
        """
        if node is None:
            return None, False
        
        if value < node.value:
            node.left, deleted = self._delete_recursive(node.left, value)
            return node, deleted
        elif value > node.value:
            node.right, deleted = self._delete_recursive(node.right, value)
            return node, deleted
        else:  # Found the node to delete
            # Case 1: Node has no children (leaf node)
            if node.left is None and node.right is None:
                return None, True
            
            # Case 2: Node has only right child
            if node.left is None:
                return node.right, True
            
            # Case 3: Node has only left child
            if node.right is None:
                return node.left, True
            
            # Case 4: Node has both children
            # Find the inorder successor (smallest value in the right subtree)
            successor_parent = node
            successor = node.right
            
            while successor.left is not None:
                successor_parent = successor
                successor = successor.left
            
            # Replace node's value with successor's value
            node.value = successor.value
            
            # Delete the successor
            if successor_parent == node:
                node.right = successor.right
            else:
                successor_parent.left = successor.right
            
            return node, True

    def inorder_traversal(self):
        """Get inorder traversal of the tree (Left, Root, Right).
        
        Returns:
            A list of values in inorder sequence.
        """
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        """Recursively perform inorder traversal.
        
        Args:
            node: The current node.
            result: The list to accumulate results.
        """
        if node is not None:
            self._inorder_recursive(node.left, result)
            result.append(node.value)
            self._inorder_recursive(node.right, result)

    def preorder_traversal(self):
        """Get preorder traversal of the tree (Root, Left, Right).
        
        Returns:
            A list of values in preorder sequence.
        """
        result = []
        self._preorder_recursive(self.root, result)
        return result

    def _preorder_recursive(self, node, result):
        """Recursively perform preorder traversal.
        
        Args:
            node: The current node.
            result: The list to accumulate results.
        """
        if node is not None:
            result.append(node.value)
            self._preorder_recursive(node.left, result)
            self._preorder_recursive(node.right, result)

    def postorder_traversal(self):
        """Get postorder traversal of the tree (Left, Right, Root).
        
        Returns:
            A list of values in postorder sequence.
        """
        result = []
        self._postorder_recursive(self.root, result)
        return result

    def _postorder_recursive(self, node, result):
        """Recursively perform postorder traversal.
        
        Args:
            node: The current node.
            result: The list to accumulate results.
        """
        if node is not None:
            self._postorder_recursive(node.left, result)
            self._postorder_recursive(node.right, result)
            result.append(node.value)

    def clear(self):
        """Remove all nodes from the tree."""
        self.root = None

    def is_empty(self):
        """Check if the tree is empty.
        
        Returns:
            True if the tree is empty, False otherwise.
        """
        return self.root is None
