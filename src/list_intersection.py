def find_list_intersection(list1, list2):
    """
    Find the intersection of two lists, returning a list of common elements.

    Args:
        list1 (list): First input list
        list2 (list): Second input list

    Returns:
        list: A list of elements that are common to both input lists

    Notes:
        - The function returns unique common elements
        - Order of elements is not guaranteed
        - Works with lists of any hashable type
    """
    # Convert lists to sets for efficient intersection
    # This handles duplicates and provides O(n) time complexity
    try:
        return list(set(list1) & set(list2))
    except TypeError:
        # Handle case where lists contain unhashable types
        return [item for item in list1 if item in list2]