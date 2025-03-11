import pytest
from src.count_occurrences import count_element_occurrences

def test_count_basic_occurrences():
    """Test counting occurrences of an element in a simple list."""
    assert count_element_occurrences([1, 2, 3, 2, 2, 4], 2) == 3

def test_count_string_occurrences():
    """Test counting occurrences of strings."""
    assert count_element_occurrences(['a', 'b', 'a', 'c', 'a'], 'a') == 3

def test_count_no_occurrences():
    """Test counting when element is not in the list."""
    assert count_element_occurrences([1, 2, 3, 4], 5) == 0

def test_count_empty_list():
    """Test counting in an empty list."""
    assert count_element_occurrences([], 1) == 0

def test_count_mixed_types():
    """Test counting in a list with mixed types."""
    assert count_element_occurrences([1, '1', 1, '1', 2], 1) == 2

def test_invalid_input_type():
    """Test that a TypeError is raised for non-list inputs."""
    with pytest.raises(TypeError, match="Input must be a list"):
        count_element_occurrences("not a list", 1)
        
def test_count_none():
    """Test counting occurrences of None."""
    assert count_element_occurrences([None, 1, None, 2], None) == 2