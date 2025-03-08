import pytest
from src.lcs import longest_common_subsequence

def test_basic_lcs():
    """Test basic longest common subsequence scenarios."""
    assert longest_common_subsequence("ABCDGH", "AEDFHR") == "ADH"
    assert longest_common_subsequence("AGGTAB", "GXTXAYB") == "GTAB"

def test_empty_strings():
    """Test edge cases with empty strings."""
    assert longest_common_subsequence("", "") == ""
    assert longest_common_subsequence("test", "") == ""
    assert longest_common_subsequence("", "test") == ""

def test_no_common_subsequence():
    """Test strings with no common subsequence."""
    assert longest_common_subsequence("abc", "xyz") == ""

def test_identical_strings():
    """Test when strings are identical."""
    assert longest_common_subsequence("hello", "hello") == "hello"

def test_partial_match():
    """Test partial matches."""
    assert longest_common_subsequence("abcde", "ace") == "ace"

def test_case_sensitivity():
    """Test case sensitivity."""
    assert longest_common_subsequence("Hello", "hello") == ""
    assert longest_common_subsequence("HELLO", "hello") == ""
    assert longest_common_subsequence("hello", "HELLO") == ""

def test_unicode_strings():
    """Test strings with non-ASCII characters."""
    # Note: This test may change based on specific normalization requirements
    assert longest_common_subsequence("résumé", "resume") == "rsum"

def test_long_strings():
    """Test longer strings with multiple common subsequences."""
    str1 = "ABCBDAB"
    str2 = "BDCABA"
    result = longest_common_subsequence(str1, str2)
    assert result in ["BCBA", "BDAB"]  # Could be multiple valid LCS

def test_input_types():
    """Ensure function handles different input types."""
    with pytest.raises(TypeError):
        longest_common_subsequence(123, "test")
    with pytest.raises(TypeError):
        longest_common_subsequence("test", 456)