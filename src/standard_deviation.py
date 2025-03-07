import math

def calculate_standard_deviation(numbers):
    """
    Calculate the standard deviation of a list of numbers.
    
    Args:
        numbers (list): A list of numeric values.
    
    Returns:
        float: The standard deviation of the input list.
    
    Raises:
        ValueError: If the input list is empty.
        TypeError: If the input contains non-numeric values.
    """
    # Check for empty list
    if not numbers:
        raise ValueError("Cannot calculate standard deviation of an empty list")
    
    # Validate input is numeric
    numeric_numbers = []
    for num in numbers:
        # Strictly check for numeric types
        if not isinstance(num, (int, float)):
            raise TypeError("All elements must be numeric")
        numeric_numbers.append(float(num))
    
    # Calculate mean
    mean = sum(numeric_numbers) / len(numeric_numbers)
    
    # Calculate variance (sum of squared differences from mean)
    variance = sum((x - mean) ** 2 for x in numeric_numbers) / len(numeric_numbers)
    
    # Return square root of variance (standard deviation)
    return math.sqrt(variance)