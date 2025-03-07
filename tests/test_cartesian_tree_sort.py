import pytest
from src.cartesian_tree_sort import cartesian_tree_sort, build_cartesian_tree, CartesianTreeNode

def test_cartesian_tree_sort_empty_list():
    """Test sorting an empty list"""
    assert cartesian_tree_sort([]) == []

def test_cartesian_tree_sort_single_element():
    """Test sorting a list with a single element"""
    assert cartesian_tree_sort([5]) == [5]

def test_cartesian_tree_sort_already_sorted():
    """Test sorting an already sorted list"""
    arr = [1, 2, 3, 4, 5]
    assert cartesian_tree_sort(arr) == arr

def test_cartesian_tree_sort_reverse_sorted():
    """Test sorting a reverse sorted list"""
    arr = [5, 4, 3, 2, 1]
    assert cartesian_tree_sort(arr) == sorted(arr)

def test_cartesian_tree_sort_random_list():
    """Test sorting a random list of integers"""
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    assert cartesian_tree_sort(arr) == sorted(arr)

def test_cartesian_tree_sort_with_strings():
    """Test sorting a list of strings"""
    arr = ['banana', 'apple', 'cherry', 'date']
    assert cartesian_tree_sort(arr) == sorted(arr)

def test_cartesian_tree_sort_with_mixed_types():
    """Test sorting a list with mixed comparable types"""
    arr = [3, 'a', 1, 'b', 2]
    result = cartesian_tree_sort(arr)
    assert result == sorted(arr, key=str), f"Expected {sorted(arr, key=str)}, got {result}"

def test_cartesian_tree_sort_invalid_input():
    """Test that a TypeError is raised for non-list input"""
    with pytest.raises(TypeError):
        cartesian_tree_sort("not a list")

def test_build_cartesian_tree_invalid_input():
    """Test that a TypeError is raised for non-list input in build_cartesian_tree"""
    with pytest.raises(TypeError):
        build_cartesian_tree("not a list")

def test_build_cartesian_tree_structure():
    """Test the structure of the built Cartesian Tree"""
    arr = [3, 1, 4, 1, 5]
    root = build_cartesian_tree(arr)
    
    # Verify root exists
    assert root is not None
    
    # Verify heap-like property (each node should be <= its children)
    def check_heap_like_property(node):
        """Helper function to check heap-like property"""
        if not node:
            return True
        
        # Check left child relationship
        if node.left:
            assert node.value <= node.left.value, \
                f"Parent {node.value} should be <= left child {node.left.value}"
        
        # Check right child relationship 
        if node.right:
            assert node.value <= node.right.value, \
                f"Parent {node.value} should be <= right child {node.right.value}"
        
        return (check_heap_like_property(node.left) and 
                check_heap_like_property(node.right))
    
    assert check_heap_like_property(root)