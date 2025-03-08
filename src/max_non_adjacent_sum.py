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
    
    # Dynamic programming approach
    # dp[i] represents the max sum up to index i
    dp = [0] * len(digits)
    
    # Initialize first two elements
    dp[0] = digits[0]
    dp[1] = max(digits[0], digits[1])
    
    # Compute max sum for each step
    for i in range(2, len(digits)):
        # Two choices at each step:
        # 1. Include current digit and max sum from two steps back
        # 2. Exclude current digit and take max from previous step
        dp[i] = max(digits[i] + dp[i-2], dp[i-1])
    
    return dp[-1]