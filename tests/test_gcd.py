import pytest
from src.gcd import euclidean_gcd

def test_basic_gcd():
    """Test basic GCD calculations."""
    assert euclidean_gcd(48, 18) == 6
    assert euclidean_gcd(54, 24) == 6
    assert euclidean_gcd(17, 5) == 1
    assert euclidean_gcd(100, 75) == 25

def test_same_number():
    """Test GCD when both numbers are the same."""
    assert euclidean_gcd(7, 7) == 7
    assert euclidean_gcd(11, 11) == 11

def test_one_is_multiple():
    """Test GCD when one number is a multiple of the other."""
    assert euclidean_gcd(12, 3) == 3
    assert euclidean_gcd(3, 12) == 3

def test_coprime_numbers():
    """Test GCD of coprime numbers."""
    assert euclidean_gcd(17, 22) == 1
    assert euclidean_gcd(14, 25) == 1

def test_large_numbers():
    """Test GCD with larger numbers."""
    assert euclidean_gcd(1071, 462) == 21
    assert euclidean_gcd(461952, 116298) == 18

def test_invalid_inputs():
    """Test error handling for invalid inputs."""
    # Test non-integer inputs
    with pytest.raises(TypeError):
        euclidean_gcd("48", 18)
    with pytest.raises(TypeError):
        euclidean_gcd(48, "18")
    with pytest.raises(TypeError):
        euclidean_gcd(3.14, 2)

def test_non_positive_inputs():
    """Test error handling for non-positive inputs."""
    with pytest.raises(ValueError):
        euclidean_gcd(0, 5)
    with pytest.raises(ValueError):
        euclidean_gcd(5, 0)
    with pytest.raises(ValueError):
        euclidean_gcd(-5, 10)
    with pytest.raises(ValueError):
        euclidean_gcd(10, -5)