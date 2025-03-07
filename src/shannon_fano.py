from collections import Counter
from typing import Dict, List, Union

def shannon_fano_encode(data: Union[str, List[str]]) -> Dict[str, str]:
    """
    Implement Shannon-Fano coding for data compression.
    
    Args:
        data (str or List[str]): Input data to be encoded
    
    Returns:
        Dict[str, str]: A dictionary mapping each unique symbol to its Fano code
    
    Raises:
        ValueError: If input is empty or invalid
    """
    # Validate input
    if not data:
        raise ValueError("Input data cannot be empty")
    
    # Convert input to list of characters if it's a string
    if isinstance(data, str):
        data = list(data)
    
    # Special case for single character
    if len(set(data)) == 1:
        return {data[0]: '0'}
    
    # Count frequency of each symbol
    frequencies = Counter(data)
    
    # Sort symbols by frequency in descending order
    sorted_symbols = sorted(frequencies.items(), key=lambda x: x[1], reverse=True)
    
    # Recursive function to generate Fano codes
    def generate_fano_codes(symbols, code=''):
        if len(symbols) <= 1:
            return {symbols[0][0]: code} if symbols else {}
        
        # Find the optimal split point
        total_freq = sum(freq for _, freq in symbols)
        current_freq = 0
        split_index = 0
        min_diff = float('inf')
        
        for i in range(len(symbols)):
            current_freq += symbols[i][1]
            diff = abs(2 * current_freq - total_freq)
            if diff < min_diff:
                min_diff = diff
                split_index = i
        
        # Recursively generate codes for two groups
        left_codes = generate_fano_codes(symbols[:split_index+1], code + '0')
        right_codes = generate_fano_codes(symbols[split_index+1:], code + '1')
        
        return {**left_codes, **right_codes}
    
    # Generate and return the Fano codes
    return generate_fano_codes(sorted_symbols)

def shannon_fano_decode(codes: Dict[str, str], encoded_data: str) -> str:
    """
    Decode Shannon-Fano encoded data.
    
    Args:
        codes (Dict[str, str]): Mapping of symbols to their Fano codes
        encoded_data (str): Encoded binary string
    
    Returns:
        str: Decoded original data
    
    Raises:
        ValueError: If decoding fails or input is invalid
    """
    # Validate input
    if not codes:
        raise ValueError("Codes cannot be empty")
    
    # Special case for single character
    if len(codes) == 1:
        symbol = list(codes.keys())[0]
        return symbol * (len(encoded_data) if encoded_data else 1)
    
    # If no encoded data but multiple codes, raise error
    if not encoded_data:
        raise ValueError("Encoded data cannot be empty")
    
    # Create reverse mapping
    reverse_codes = {code: symbol for symbol, code in codes.items()}
    
    # Decode the data
    decoded = []
    current_code = ''
    for bit in encoded_data:
        current_code += bit
        if current_code in reverse_codes:
            decoded.append(reverse_codes[current_code])
            current_code = ''
    
    # Check if all bits were decoded
    if current_code:
        raise ValueError("Invalid encoded data: could not decode completely")
    
    return ''.join(decoded)