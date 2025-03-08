import pytest
from src.find_missing_numbers import find_missing_numbers

def test_basic_missing_numbers():
    """Test finding missing numbers in a basic scenario."""
    arr = [1, 2, 4, 6, 3, 7, 8]
    assert find_missing_numbers(arr) == [5]

def test_no_missing_numbers():
    """Test when no numbers are missing."""
    arr = [1, 2, 3, 4, 5]
    assert find_missing_numbers(arr) == []

def test_sparse_array():
    """Test with a sparse array of numbers."""
    arr = [10, 20, 30, 50]
    assert find_missing_numbers(arr) == [40]

def test_negative_numbers():
    """Test with negative numbers in the array."""
    arr = [-3, -1, 0, 2, 4]
    assert find_missing_numbers(arr) == [-2, 1, 3]

def test_empty_array():
    """Test with an empty array."""
    arr = []
    assert find_missing_numbers(arr) == []

def test_single_element_array():
    """Test with a single-element array."""
    arr = [5]
    assert find_missing_numbers(arr) == []

def test_invalid_input_non_list():
    """Test raising TypeError for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        find_missing_numbers("not a list")

def test_invalid_input_non_integers():
    """Test raising ValueError for non-integer elements."""
    with pytest.raises(ValueError, match="All elements must be integers"):
        find_missing_numbers([1, 2, "3", 4])

def test_invalid_input_duplicate_values():
    """Test raising ValueError for duplicate values."""
    with pytest.raises(ValueError, match="Input array must contain unique integers"):
        find_missing_numbers([1, 2, 2, 3, 4])