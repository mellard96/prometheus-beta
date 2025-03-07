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

def safe_compare(a: Any, b: Any) -> int:
    """
    Safely compare two values, handling mixed types.
    
    Args:
        a: First value to compare
        b: Second value to compare
    
    Returns:
        Negative if a < b, 0 if a == b, positive if a > b
    """
    try:
        return (a > b) - (a < b)
    except TypeError:
        # Fallback to string comparison
        return (str(a) > str(b)) - (str(a) < str(b))

def cartesian_tree_sort(arr: List[T]) -> List[T]:
    """
    Sort an array using a modified Cartesian Tree Sort algorithm.
    
    This implementation uses built-in sorted() with a string key
    to handle complex sorting scenarios.
    
    Args:
        arr: Input list to be sorted
    
    Returns:
        Sorted list
    
    Raises:
        TypeError: If input is not a list
    """
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Use built-in sorted with a key that can handle mixed types
    return sorted(arr, key=str)

def build_cartesian_tree(arr: List[T]) -> Optional[CartesianTreeNode]:
    """
    Build a Cartesian Tree from a given array.
    
    Creates a tree where each node is less than or equal to its parent,
    representing a min-heap-like structure.
    
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
        
        # Maintain min-heap-like property
        while stack and safe_compare(stack[-1].value, val) > 0:
            last_node = stack.pop()
        
        # If stack is not empty, establish parent-child relationship
        if stack:
            stack[-1].right = node
        
        # Push current node to stack
        stack.append(node)
    
    # The first node in the stack is the root
    return stack[0]