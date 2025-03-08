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
    
    # More comprehensive search strategy
    def max_nonadjacent_exhaustive(arr):
        # If fewer than 2 elements, return best possible sum
        if len(arr) < 2:
            return max(arr) if arr else 0
        
        # Track all possible maximums
        max_sums = []
        
        # Try all possible first selections
        for first_idx in range(len(arr)):
            first_value = arr[first_idx]
            
            # Find best possible second selection
            local_max = first_value
            local_max_sum = first_value
            
            # Check rest of the digits, skipping direct neighbors
            for j in range(len(arr)):
                # Ensure not adjacent in original order
                if abs(j - first_idx) > 1:
                    local_max = max(local_max, arr[j])
                    local_max_sum = max(local_max_sum, first_value + arr[j])
            
            max_sums.append(local_max_sum)
        
        return max(max_sums)
    
    return max_nonadjacent_exhaustive(digits)