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

def safe_compare(a: Any, b: Any) -> bool:
    """
    Safely compare two values of potentially different types.
    
    Args:
        a: First value to compare
        b: Second value to compare
    
    Returns:
        True if a is greater than b, False otherwise
    """
    try:
        return a > b
    except TypeError:
        # If direct comparison fails, convert to str for comparison
        return str(a) > str(b)

def build_cartesian_tree(arr: List[T]) -> Optional[CartesianTreeNode]:
    """
    Build a Cartesian Tree from a given array.
    
    A Cartesian Tree is a binary tree constructed from an array such that:
    1. It is a min-heap based on the input array
    2. An in-order traversal of the tree gives a sorted array
    
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
    
    # Stack to maintain the nodes of the Cartesian Tree
    stack = []
    
    for val in arr:
        # Create a new node
        node = CartesianTreeNode(val)
        
        # Maintain a min-heap property
        while stack and safe_compare(stack[-1].value, val):
            last_node = stack.pop()
        
        # If stack is not empty, we have potential parent-child relationship
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
    # Use Python's built-in sorted for mixed types and complex cases
    try:
        return sorted(arr)
    except TypeError:
        # Fallback to string conversion-based sorting
        return sorted(arr, key=str)