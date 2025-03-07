import pytest
import math
from src.standard_deviation import calculate_standard_deviation

def test_standard_deviation_basic():
    """Test standard deviation of a simple list of numbers."""
    numbers = [2, 4, 4, 4, 5, 5, 7, 9]
    expected = math.sqrt(sum((x - 5)**2 for x in numbers) / len(numbers))
    assert math.isclose(calculate_standard_deviation(numbers), expected, rel_tol=1e-10)

def test_standard_deviation_single_number():
    """Test standard deviation with a single number."""
    assert calculate_standard_deviation([5]) == 0

def test_standard_deviation_floats():
    """Test standard deviation with floating point numbers."""
    numbers = [1.5, 2.5, 3.5, 4.5, 5.5]
    expected = math.sqrt(sum((x - 3.5)**2 for x in numbers) / len(numbers))
    assert math.isclose(calculate_standard_deviation(numbers), expected, rel_tol=1e-10)

def test_empty_list_raises_error():
    """Test that an empty list raises a ValueError."""
    with pytest.raises(ValueError, match="Cannot calculate standard deviation of an empty list"):
        calculate_standard_deviation([])

def test_non_numeric_input_raises_error():
    """Test that non-numeric input raises a TypeError."""
    with pytest.raises(TypeError, match="All elements must be numeric"):
        calculate_standard_deviation(['a', 'b', 'c'])
    
    with pytest.raises(TypeError, match="All elements must be numeric"):
        calculate_standard_deviation([1, 2, '3', 4])

def test_zero_variance():
    """Test standard deviation with a list of identical numbers."""
    assert calculate_standard_deviation([7, 7, 7, 7]) == 0

def test_negative_numbers():
    """Test standard deviation with negative numbers."""
    numbers = [-2, -4, -4, -4, -5, -5, -7, -9]
    expected = math.sqrt(sum((x + 5)**2 for x in numbers) / len(numbers))
    assert math.isclose(calculate_standard_deviation(numbers), expected, rel_tol=1e-10)