def compute_lps_array(pattern):
    """
    Compute the Longest Proper Prefix which is also Suffix (LPS) array.
    
    Args:
        pattern (str): The pattern string to compute LPS for.
    
    Returns:
        list: LPS array representing the longest proper prefix which is also a suffix.
    """
    # Length of the previous longest prefix suffix
    lps = [0] * len(pattern)
    length = 0  # Length of the current longest prefix suffix
    i = 1

    # The first element is always 0
    while i < len(pattern):
        # If characters match, extend the prefix
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            # If characters don't match
            if length != 0:
                # Go back to the previous longest prefix suffix
                length = lps[length - 1]
            else:
                # If length is 0, set LPS for current index to 0
                lps[i] = 0
                i += 1
    
    return lps

def kmp_search(text, pattern):
    """
    Implement Knuth-Morris-Pratt (KMP) string matching algorithm.
    
    Args:
        text (str): The main text to search in.
        pattern (str): The pattern to search for.
    
    Returns:
        list: Indices where the pattern is found in the text.
    
    Raises:
        TypeError: If inputs are not strings.
        ValueError: If either input is empty.
    """
    # Input validation
    if not isinstance(text, str) or not isinstance(pattern, str):
        raise TypeError("Both text and pattern must be strings")
    
    if not text or not pattern:
        raise ValueError("Text and pattern cannot be empty")
    
    # Compute the LPS array
    lps = compute_lps_array(pattern)
    
    # List to store found indices
    matches = []
    
    # Pointers for text and pattern
    i = 0  # index for text
    j = 0  # index for pattern
    
    while i < len(text):
        # If characters match, move both pointers
        if text[i] == pattern[j]:
            i += 1
            j += 1
        
        # Pattern found
        if j == len(pattern):
            matches.append(i - j)
            # Reset j to continue searching
            j = lps[j-1]
        
        # Mismatch after some matches
        elif i < len(text) and text[i] != pattern[j]:
            # If j is not 0, use LPS array to determine next position
            if j != 0:
                j = lps[j-1]
            else:
                # If j is 0, move to next character in text
                i += 1
    
    return matches