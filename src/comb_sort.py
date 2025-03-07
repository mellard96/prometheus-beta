def comb_sort(arr):
    """
    Implement the Comb Sort algorithm for sorting a list in ascending order.
    
    Comb Sort is an improvement over bubble sort. It eliminates turtles, or small values 
    near the end of the list, by sweeping with a large gap and progressively reducing the gap.
    
    Args:
        arr (list): The input list to be sorted
    
    Returns:
        list: A new sorted list in ascending order
    
    Raises:
        TypeError: If the input is not a list
        ValueError: If list contains elements that cannot be compared
    """
    # Check input type
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Create a copy to avoid modifying the original list
    lst = arr.copy()
    
    # If list is empty or has only one element, return it
    if len(lst) <= 1:
        return lst
    
    # Initial gap is the length of the list
    gap = len(lst)
    
    # Initialize a flag to check if any swaps occurred
    swapped = True
    
    # Continue until no more swaps occur and gap becomes 1
    while gap > 1 or swapped:
        # Reduce gap using shrink factor of 1.3
        gap = max(1, int(gap / 1.3))
        
        # Reset swap flag
        swapped = False
        
        # Compare elements with current gap
        for i in range(len(lst) - gap):
            # If elements are out of order, swap them
            if lst[i] > lst[i + gap]:
                lst[i], lst[i + gap] = lst[i + gap], lst[i]
                swapped = True
    
    return lst