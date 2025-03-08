def max_non_adjacent_digit_sum(number):
    """
    Find the maximum sum of non-adjacent digits in a positive integer.
    
    A non-adjacent digit sum means selecting digits that are not next to each other
    and maximizing their sum.
    
    Args:
        number (int): A positive integer to analyze
    
    Returns:
        int: Maximum sum of non-adjacent digits
    
    Raises:
        ValueError: If the input is not a positive integer
    """
    # Validate input
    if not isinstance(number, int) or number < 0:
        raise ValueError("Input must be a positive integer")
    
    # Convert number to string for easy digit manipulation
    digits = [int(d) for d in str(number)]
    
    # Handle small input cases
    if len(digits) <= 1:
        return max(digits) if digits else 0
    
    # Complex non-adjacent digit sum computation
    def max_non_adjacent_optimal(arr):
        n = len(arr)
        
        # Special cases
        if n == 1:
            return arr[0]
        if n == 2:
            return max(arr[0], arr[1])
        
        # DP array to track best possible sums
        dp = [0] * n
        dp[0] = arr[0]
        dp[1] = max(arr[0], arr[1])
        
        # Track maximum possible selection
        max_sum = dp[1]
        
        # Compute best possible sums
        for i in range(2, n):
            # Consider skipping this index
            skip = dp[i-1]
            
            # Consider including this digit
            include = arr[i] + dp[i-2]
            
            # Update max possible sum
            dp[i] = max(skip, include)
            max_sum = max(max_sum, dp[i])
        
        return max_sum
    
    return max_non_adjacent_optimal(digits)