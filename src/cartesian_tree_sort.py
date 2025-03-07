from typing import List, TypeVar, Optional, Any

T = TypeVar('T')

class CartesianTreeNode:
    """
    Node class for Cartesian Tree implementation.
    
    Attributes:
        value: The value stored in the node
        left: Left child node
        right: Right child node
    """
    def __init__(self, value):
        """
        Initialize a Cartesian Tree Node.
        
        Args:
            value: The value to be stored in the node
        """
        self.value = value
        self.left = None
        self.right = None

def build_cartesian_tree(arr: List[T]) -> Optional[CartesianTreeNode]:
    """
    Build a Cartesian Tree from a given array.
    
    A Cartesian Tree is a binary tree constructed from an array such that:
    1. It is a min-heap based on the input array
    2. An in-order traversal of the tree produces the original array
    
    Args:
        arr: Input list to build the Cartesian Tree from
    
    Returns:
        Root node of the constructed Cartesian Tree, or None if input is empty
    
    Raises:
        TypeError: If input is not a list
    """
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    if not arr:
        return None
    
    # If the list contains mixed types, convert to strings for comparison
    def safe_compare(a: Any, b: Any) -> bool:
        try:
            return a > b
        except TypeError:
            return str(a) > str(b)
    
    # Stack to maintain the nodes of the Cartesian Tree
    stack = []
    
    for val in arr:
        # Create a new node
        node = CartesianTreeNode(val)
        
        # Find the last node that is greater than the current node
        while stack and safe_compare(stack[-1].value, val):
            stack.pop()
        
        # If stack is not empty, the top node becomes the parent
        if stack:
            stack[-1].right = node
        
        # Push current node to stack
        stack.append(node)
    
    # The first node in the stack is the root
    return stack[0]

def cartesian_tree_sort(arr: List[T]) -> List[T]:
    """
    Sort an array using Cartesian Tree Sort algorithm.
    
    This implementation builds a Cartesian Tree and then performs an in-order 
    traversal to get the sorted array.
    
    Args:
        arr: Input list to be sorted
    
    Returns:
        Sorted list
    
    Raises:
        TypeError: If input is not a list
    """
    # Build the Cartesian Tree
    root = build_cartesian_tree(arr)
    
    # If the tree is empty, return an empty list
    if not root:
        return []
    
    # Perform in-order traversal to get sorted list
    def in_order_traversal(node):
        """Helper function to perform in-order traversal"""
        if not node:
            return []
        
        return (in_order_traversal(node.left) + 
                [node.value] + 
                in_order_traversal(node.right))
    
    return in_order_traversal(root)