import pytest
from src.kmp_string_matcher import kmp_search, compute_lps_array

def test_compute_lps_array():
    """Test the LPS array computation."""
    assert compute_lps_array("AAAA") == [0, 1, 2, 3]
    assert compute_lps_array("ABCDE") == [0, 0, 0, 0, 0]
    assert compute_lps_array("ABABCABAB") == [0, 0, 1, 2, 0, 1, 2, 3, 4]

def test_kmp_search_basic():
    """Test basic string matching scenarios."""
    assert kmp_search("ABABDABACDABABCABAB", "ABABCABAB") == [10]
    assert kmp_search("AABAACAADAABAABA", "AABA") == [0, 9, 12]
    assert kmp_search("ABXABXABXAB", "ABXAB") == [0, 3, 6]

def test_kmp_search_multiple_occurrences():
    """Test scenarios with multiple pattern occurrences."""
    assert kmp_search("AAAAAA", "AA") == [0, 1, 2, 3, 4]
    assert kmp_search("ABABABAB", "ABAB") == [0, 2, 4]

def test_kmp_search_no_matches():
    """Test scenarios with no matches."""
    assert kmp_search("ABCDEF", "XYZ") == []
    assert kmp_search("HELLO", "WORLD") == []

def test_kmp_search_edge_cases():
    """Test edge cases for KMP search."""
    # Pattern longer than text
    assert kmp_search("SHORT", "VERYLONGPATTERN") == []
    
    # Single character matching
    assert kmp_search("ABCDEFG", "C") == [2]

def test_kmp_search_input_validation():
    """Test input validation."""
    # Non-string inputs
    with pytest.raises(TypeError):
        kmp_search(123, "pattern")
    with pytest.raises(TypeError):
        kmp_search("text", 456)
    
    # Empty inputs
    with pytest.raises(ValueError):
        kmp_search("", "pattern")
    with pytest.raises(ValueError):
        kmp_search("text", "")