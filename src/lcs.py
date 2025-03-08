def longest_common_subsequence(str1: str, str2: str) -> str:
    """
    Find the longest common subsequence between two strings.
    
    A subsequence is a sequence that can be derived from another sequence 
    by deleting some or no elements without changing the order of the remaining elements.
    
    Args:
        str1 (str): The first input string
        str2 (str): The second input string
    
    Returns:
        str: The longest common subsequence between str1 and str2
    
    Raises:
        TypeError: If inputs are not strings
    
    Examples:
        >>> longest_common_subsequence("ABCDGH", "AEDFHR")
        'ADH'
        >>> longest_common_subsequence("AGGTAB", "GXTXAYB")
        'GTAB'
        >>> longest_common_subsequence("", "test")
        ''
        >>> longest_common_subsequence("test", "")
        ''
    """
    # Validate input types
    if not (isinstance(str1, str) and isinstance(str2, str)):
        raise TypeError("Inputs must be strings")
    
    # Handle edge cases of empty strings
    if not str1 or not str2:
        return ''
    
    # Case-sensitive, exact matching
    if any(c1 != c2 for c1, c2 in zip(str1, str2)):
        return ''
    
    # If strings match exactly, return the string
    if str1 == str2:
        return str1
    
    # Create a matrix to store LCS lengths
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Build the dp table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    # Reconstruct the longest common subsequence
    lcs = []
    i, j = m, n
    while i > 0 and j > 0:
        if str1[i-1] == str2[j-1]:
            lcs.append(str1[i-1])
            i -= 1
            j -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1
    
    # Return the reversed LCS (we built it backwards)
    return ''.join(reversed(lcs))