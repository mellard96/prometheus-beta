from typing import List, TypeVar, Optional, Any, Callable

T = TypeVar('T')

class CartesianTreeNode:
    """
    Node class for Cartesian Tree implementation.
    
    Attributes:
        value: The value stored in the node
        left: Left child node
        right: Right child node
        original_index: Original index in the input array
    """
    def __init__(self, value, original_index):
        """
        Initialize a Cartesian Tree Node.
        
        Args:
            value: The value to be stored in the node
            original_index: Original index of the value in the input array
        """
        self.value = value
        self.original_index = original_index
        self.left = None
        self.right = None

def build_cartesian_tree(arr: List[T]) -> Optional[CartesianTreeNode]:
    """
    Build a Cartesian Tree from a given array.
    
    A Cartesian Tree is a binary tree constructed from an array such that:
    1. It is a min-heap based on the input array
    2. An in-order traversal of the tree preserves the original order for equal elements
    
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
    
    # Use indexed comparison to maintain original order for equal elements
    indexed_arr = list(enumerate(arr))
    
    # Stack to maintain the nodes of the Cartesian Tree
    stack = []
    
    for idx, val in indexed_arr:
        # Create a new node
        node = CartesianTreeNode(val, idx)
        
        # Find the last node that is greater than the current node
        last_popped = None
        while stack and (stack[-1].value > val or 
                         (stack[-1].value == val and stack[-1].original_index > idx)):
            last_popped = stack.pop()
        
        # If stack is not empty, the top node becomes the parent
        if stack:
            stack[-1].right = node
        
        # If we popped some nodes, the last one becomes the left child
        if last_popped:
            node.left = last_popped
        
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