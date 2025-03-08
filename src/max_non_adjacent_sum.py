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
    
    # Compute maximum possible sum considering multiple strategies
    def max_non_adjacent_combinations(arr):
        n = len(arr)
        
        # Early return for short arrays
        if n <= 1:
            return max(arr) if arr else 0
        if n == 2:
            return max(arr[0], arr[1])
        
        # Compute all possible max sums
        max_sums = []
        
        # Strategy 1: First digits
        first_sum = arr[0] + arr[2] if n > 2 else arr[0]
        max_sums.append(first_sum)
        
        # Strategy 2: Second digits
        second_sum = arr[1] + arr[3] if n > 3 else arr[1]
        max_sums.append(second_sum)
        
        # Advanced combination strategies
        for stride in range(2, 4):  # Try different skipping patterns
            current_sum = 0
            for i in range(0, n, stride):
                current_sum += arr[i]
            max_sums.append(current_sum)
        
        # More advanced: iterative improvement
        for first_skip in range(n):
            temp_sum = 0
            for j in range(first_skip, n, 2):
                temp_sum += arr[j]
            max_sums.append(temp_sum)
        
        return max(max_sums)
    
    return max_non_adjacent_combinations(digits)