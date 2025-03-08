import pytest
from src.palindrome_checker import is_palindrome

def test_simple_palindromes():
    assert is_palindrome("racecar") == True
    assert is_palindrome("radar") == True
    assert is_palindrome("level") == True

def test_palindrome_with_spaces():
    assert is_palindrome("a man a plan a canal panama") == True
    assert is_palindrome("Was it a car or a cat I saw?") == True

def test_non_palindromes():
    assert is_palindrome("hello") == False
    assert is_palindrome("python") == False
    assert is_palindrome("race a car") == False

def test_mixed_case_palindromes():
    assert is_palindrome("Able was I ere I saw Elba") == True
    assert is_palindrome("A Santa at NASA") == True

def test_palindrome_with_punctuation():
    assert is_palindrome("A man, a plan, a canal: Panama") == True
    assert is_palindrome("race: a car") == False

def test_edge_cases():
    # Empty string
    assert is_palindrome("") == True
    
    # Single character
    assert is_palindrome("a") == True
    assert is_palindrome("1") == True
    
    # Numbers and symbols
    assert is_palindrome("12321") == True
    assert is_palindrome("123 321") == True
    assert is_palindrome("123 421") == False

def test_unicode_characters():
    # Basic Unicode palindromes
    assert is_palindrome("レベル") == True  # 'level' in Japanese
    assert is_palindrome("こんにちは") == False  # 'hello' in Japanese

def test_non_string_input():
    with pytest.raises(TypeError):
        is_palindrome(12321)
    with pytest.raises(TypeError):
        is_palindrome(None)