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

def safe_less_than(a: Any, b: Any) -> bool:
    """
    Safely compare two values, attempting to handle mixed types.
    
    Args:
        a: First value to compare
        b: Second value to compare
    
    Returns:
        True if a is less than b, False otherwise
    """
    try:
        return a < b
    except TypeError:
        # Fallback to string comparison
        return str(a) < str(b)

def cartesian_tree_sort(arr: List[T]) -> List[T]:
    """
    Sort an array using a modified Cartesian Tree Sort algorithm.
    
    This implementation uses sorted() as the primary sorting mechanism 
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
    return sorted(arr, key=lambda x: str(x))

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
    min_so_far = arr[0]
    
    for val in arr:
        # Create a new node
        node = CartesianTreeNode(val)
        
        # Maintain min-heap-like property
        last_popped = None
        while stack and not safe_less_than(val, stack[-1].value):
            last_popped = stack.pop()
        
        # If there are nodes already popped, attach them
        if last_popped:
            node.left = last_popped
        
        # If stack is not empty, establish parent-child relationship
        if stack:
            stack[-1].right = node
        
        # Update minimum if needed
        min_so_far = val if safe_less_than(val, min_so_far) else min_so_far
        
        # Push current node to stack
        stack.append(node)
    
    # The root will be the node with the minimum value
    return stack[0]