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
    
    # Dynamic programming approach with more flexible non-adjacency
    def max_non_adjacent(arr):
        if not arr:
            return 0
        if len(arr) == 1:
            return arr[0]
        
        # Initialize DP array to track best possible sums
        dp = [0] * len(arr)
        dp[0] = arr[0]
        dp[1] = max(arr[0], arr[1])
        
        # Dynamic programming computation
        for i in range(2, len(arr)):
            # At each step, consider:
            # 1. Skipping this digit (previous best sum)
            # 2. Including this digit and the best sum from at least 2 steps back
            dp[i] = max(dp[i-1], arr[i] + dp[i-2])
        
        return dp[-1]
    
    return max_non_adjacent(digits)