import unicodedata

def is_palindrome(s: str) -> bool:
    """
    Determine if the given string is a palindrome.
    
    A palindrome reads the same forward and backward, ignoring spaces, 
    punctuation, and case sensitivity.
    
    Args:
        s (str): The input string to check.
    
    Returns:
        bool: True if the string is a palindrome, False otherwise.
    
    Raises:
        TypeError: If input is not a string.
    
    Examples:
        >>> is_palindrome("A man, a plan, a canal: Panama")
        True
        >>> is_palindrome("race a car")
        False
        >>> is_palindrome("Was it a car or a cat I saw?")
        True
    """
    # Validate input is a string
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    
    # Normalize Unicode and remove diacritical marks
    normalized_str = unicodedata.normalize('NFKD', s)
    
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned_str = ''.join(
        char.lower() for char in normalized_str 
        if unicodedata.category(char)[0] not in ['M', 'P', 'Z']  # Remove marks, punctuation, and separators
    )
    
    # Check if the cleaned string is equal to its reverse
    return cleaned_str == cleaned_str[::-1]