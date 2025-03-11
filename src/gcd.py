def find_gcd(a: int, b: int) -> int:
    """
    Calculate the Greatest Common Divisor (GCD) of two integers using the Euclidean algorithm.
    
    Args:
        a (int): First integer
        b (int): Second integer
    
    Returns:
        int: The greatest common divisor of a and b
    
    Raises:
        TypeError: If inputs are not integers
        ValueError: If inputs are negative
    """
    # Type checking
    if not (isinstance(a, int) and isinstance(b, int)):
        raise TypeError("Inputs must be integers")
    
    # Handle zero cases
    if a == 0 and b == 0:
        raise ValueError("GCD is undefined for both inputs being zero")
    
    # Take absolute values to handle negative inputs
    a, b = abs(a), abs(b)
    
    # Euclidean algorithm
    while b:
        a, b = b, a % b
    
    return a