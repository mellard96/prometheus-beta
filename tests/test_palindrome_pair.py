import pytest
from src.palindrome_pair import palindrome_pair

def test_palindrome_pair_basic_positive():
    """Test basic positive case with palindrome difference."""
    assert palindrome_pair([10, 20, 30]) == True  # 20 - 10 = 10 (2-digit palindrome)

def test_palindrome_pair_basic_negative():
    """Test case with no palindrome difference."""
    assert palindrome_pair([1, 3, 5, 7]) == False

def test_palindrome_pair_exact_palindrome():
    """Test with exactly palindrome difference."""
    assert palindrome_pair([11, 22]) == True  # 22 - 11 = 11 (2-digit palindrome)

def test_palindrome_pair_unsorted_input():
    """Test that function works with unsorted input."""
    assert palindrome_pair([30, 10, 20]) == True

def test_palindrome_pair_empty_list():
    """Test empty list returns False."""
    assert palindrome_pair([]) == False

def test_palindrome_pair_single_element():
    """Test single element list returns False."""
    assert palindrome_pair([5]) == False

def test_palindrome_pair_negative_numbers():
    """Test with negative numbers."""
    assert palindrome_pair([-22, -11, 0, 11, 22]) == True

def test_palindrome_pair_invalid_input_type():
    """Test invalid input type raises TypeError."""
    with pytest.raises(TypeError):
        palindrome_pair("not a list")

def test_palindrome_pair_invalid_list_elements():
    """Test list with non-integer elements raises ValueError."""
    with pytest.raises(ValueError):
        palindrome_pair([1, 2, "3"])