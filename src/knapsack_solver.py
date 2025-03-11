def solve_knapsack(weights, values, capacity):
    """
    Solve the 0/1 Knapsack problem using dynamic programming.
    
    Args:
        weights (list): List of item weights
        values (list): List of item values 
        capacity (int): Maximum weight capacity of the knapsack
    
    Returns:
        tuple: A tuple containing:
            - Maximum total value that can be achieved
            - List of items selected (indices)
    
    Raises:
        ValueError: If input lists have different lengths or invalid inputs
    """
    # Input validation
    if not (isinstance(weights, list) and isinstance(values, list)):
        raise ValueError("Weights and values must be lists")
    
    if len(weights) != len(values):
        raise ValueError("Weights and values lists must have the same length")
    
    if not all(isinstance(w, (int, float)) and w >= 0 for w in weights):
        raise ValueError("Weights must be non-negative numbers")
    
    if not all(isinstance(v, (int, float)) and v >= 0 for v in values):
        raise ValueError("Values must be non-negative numbers")
    
    if not isinstance(capacity, (int, float)) or capacity < 0:
        raise ValueError("Capacity must be a non-negative number")
    
    # Number of items
    n = len(weights)
    
    # Initialize the dynamic programming table
    # dp[i][w] represents the maximum value achievable with first i items 
    # and weight limit w
    dp = [[0 for _ in range(int(capacity) + 1)] for _ in range(n + 1)]
    
    # Build the table bottom-up
    for i in range(1, n + 1):
        for w in range(int(capacity) + 1):
            # Current item's weight and value (adjust index)
            current_weight = weights[i-1]
            current_value = values[i-1]
            
            # If current item can be included
            if current_weight <= w:
                # Max of including or excluding current item
                dp[i][w] = max(
                    dp[i-1][w],  # exclude current item
                    dp[i-1][w-int(current_weight)] + current_value  # include current item
                )
            else:
                # Cannot include current item
                dp[i][w] = dp[i-1][w]
    
    # Backtrack to find selected items
    selected_items = []
    w = int(capacity)
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            # This item was included
            selected_items.append(i-1)
            w -= int(weights[i-1])
    
    # Return max value and list of selected item indices (in reverse order)
    return dp[n][int(capacity)], list(reversed(selected_items))