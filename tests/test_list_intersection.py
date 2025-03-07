import pytest
from src.list_intersection import find_list_intersection

def test_basic_intersection():
    """Test basic list intersection"""
    assert sorted(find_list_intersection([1, 2, 3], [3, 4, 5])) == [3]

def test_multiple_common_elements():
    """Test lists with multiple common elements"""
    assert sorted(find_list_intersection([1, 2, 3, 4], [3, 4, 5, 6])) == [3, 4]

def test_no_intersection():
    """Test lists with no common elements"""
    assert find_list_intersection([1, 2], [3, 4]) == []

def test_empty_lists():
    """Test intersection with empty lists"""
    assert find_list_intersection([], [1, 2]) == []
    assert find_list_intersection([1, 2], []) == []

def test_identical_lists():
    """Test lists that are entirely identical"""
    assert sorted(find_list_intersection([1, 2, 3], [1, 2, 3])) == [1, 2, 3]

def test_lists_with_duplicates():
    """Test lists with duplicate elements"""
    assert sorted(find_list_intersection([1, 1, 2, 2], [1, 2, 3])) == [1, 2]

def test_string_lists():
    """Test intersection with string lists"""
    assert sorted(find_list_intersection(['a', 'b', 'c'], ['b', 'c', 'd'])) == ['b', 'c']

def test_mixed_type_lists():
    """Test lists with mixed types"""
    assert sorted(find_list_intersection([1, 'a', 2], [2, 'a', 3])) == [2, 'a']