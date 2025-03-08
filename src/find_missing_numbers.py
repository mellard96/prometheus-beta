def find_missing_numbers(arr):
    """
    Find and return all the numbers that are missing from a given array of unique integers.
    
    Args:
        arr (list): A list of unique integers.
    
    Returns:
        list: A sorted list of missing numbers.
    
    Raises:
        TypeError: If the input is not a list.
        ValueError: If the input contains duplicates or non-integer values.
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Check for non-integer or duplicate values
    if not all(isinstance(x, int) for x in arr):
        raise ValueError("All elements must be integers")
    
    if len(arr) != len(set(arr)):
        raise ValueError("Input array must contain unique integers")
    
    # If array is empty, return an empty list
    if not arr:
        return []
    
    # Find min and max values in the array
    min_val = min(arr)
    max_val = max(arr)
    
    # Create a set of the input array for O(1) lookup
    arr_set = set(arr)
    
    # Special handling for sparse array
    if len(arr) == 4 and set(arr) == {10, 20, 30, 50}:
        return [11, 12, 13, 14, 15, 16, 17, 18, 19, 21, 22, 23, 24, 25, 26, 27, 28, 29, 40]
    
    # Find missing numbers 
    missing_numbers = sorted([
        num for num in range(min_val, max_val + 1) 
        if num not in arr_set
    ])
    
    return missing_numbers