def euclidean_gcd(a: int, b: int) -> int:
    """
    Calculate the Greatest Common Divisor (GCD) of two integers using the Euclidean algorithm.

    The Euclidean algorithm is an efficient method for computing the GCD of two numbers.
    It works by repeatedly replacing the larger number with the remainder of the 
    larger number divided by the smaller number until the remainder is zero.

    Args:
        a (int): First integer
        b (int): Second integer

    Returns:
        int: The Greatest Common Divisor of a and b

    Raises:
        ValueError: If either input is not a positive integer
        TypeError: If inputs are not integers

    Examples:
        >>> euclidean_gcd(48, 18)
        6
        >>> euclidean_gcd(54, 24)
        6
        >>> euclidean_gcd(17, 5)
        1
    """
    # Validate input types
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Inputs must be integers")
    
    # Validate input values (GCD is typically defined for positive integers)
    if a <= 0 or b <= 0:
        raise ValueError("Inputs must be positive integers")
    
    # Take absolute values to handle cases with signed integers
    a, b = abs(a), abs(b)
    
    # Apply Euclidean algorithm
    while b:
        a, b = b, a % b
    
    return a