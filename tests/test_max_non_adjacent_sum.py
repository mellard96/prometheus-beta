import pytest
from src.max_non_adjacent_sum import max_non_adjacent_digit_sum

def test_single_digit_number():
    """Test single digit number"""
    assert max_non_adjacent_digit_sum(5) == 5

def test_two_digit_number():
    """Test two digit number"""
    assert max_non_adjacent_digit_sum(42) == 6  # max(4, 2)
    assert max_non_adjacent_digit_sum(24) == 6  # max(4, 2)

def test_multi_digit_number():
    """Test multi-digit numbers"""
    assert max_non_adjacent_digit_sum(1234) == 8  # 1+4 or 2+6
    assert max_non_adjacent_digit_sum(9876) == 15  # 9+6

def test_larger_number():
    """Test larger multi-digit number"""
    assert max_non_adjacent_digit_sum(54321) == 10  # 5+5

def test_zero():
    """Test zero input"""
    assert max_non_adjacent_digit_sum(0) == 0

def test_invalid_input():
    """Test invalid input types"""
    with pytest.raises(ValueError):
        max_non_adjacent_digit_sum(-1)
    
    with pytest.raises(ValueError):
        max_non_adjacent_digit_sum("123")

def test_special_case_numbers():
    """Test some special case numbers"""
    assert max_non_adjacent_digit_sum(10) == 1
    assert max_non_adjacent_digit_sum(11) == 2
    assert max_non_adjacent_digit_sum(123) == 4  # 1+3
    assert max_non_adjacent_digit_sum(9999) == 18  # 9+9