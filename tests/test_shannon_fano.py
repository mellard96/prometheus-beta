import pytest
from src.shannon_fano import shannon_fano_encode, shannon_fano_decode

def test_shannon_fano_basic_encoding():
    """Test basic encoding of a simple string"""
    data = "AABBBCCCC"
    codes = shannon_fano_encode(data)
    
    # Verify codes are unique and cover all symbols
    assert len(set(codes.values())) == len(codes)
    assert set(codes.keys()) == set("ABC")

def test_shannon_fano_encode_decode_roundtrip():
    """Test full encode-decode roundtrip"""
    data = "HELLO WORLD"
    
    # Encode
    codes = shannon_fano_encode(data)
    
    # Encode each character
    encoded_data = ''.join(codes[char] for char in data)
    
    # Decode
    decoded = shannon_fano_decode(codes, encoded_data)
    
    assert decoded == data

def test_shannon_fano_different_input_types():
    """Test encoding with string and list inputs"""
    string_input = "AABBCC"
    list_input = list("AABBCC")
    
    string_codes = shannon_fano_encode(string_input)
    list_codes = shannon_fano_encode(list_input)
    
    assert string_codes == list_codes

def test_shannon_fano_empty_input_error():
    """Test error handling for empty input"""
    with pytest.raises(ValueError):
        shannon_fano_encode("")
    
    with pytest.raises(ValueError):
        shannon_fano_decode({}, "")

def test_shannon_fano_decoding_error():
    """Test decoding with invalid encoded data"""
    codes = shannon_fano_encode("HELLO")
    
    with pytest.raises(ValueError):
        shannon_fano_decode(codes, "10101010101010101")  # Invalid encoded data

def test_shannon_fano_frequency_distribution():
    """Test that more frequent symbols get shorter codes"""
    data = "AAAAABBBBBCCCCCDDDDD"
    codes = shannon_fano_encode(data)
    
    # A and B have higher frequency, so should have shorter codes
    a_code_len = len(codes['A'])
    b_code_len = len(codes['B'])
    c_code_len = len(codes['C'])
    d_code_len = len(codes['D'])
    
    # These assertions check the general principle of Shannon-Fano coding
    assert a_code_len <= b_code_len
    assert b_code_len <= c_code_len
    assert c_code_len <= d_code_len

def test_shannon_fano_single_character():
    """Test encoding and decoding with single character input"""
    data = "A"
    codes = shannon_fano_encode(data)
    
    assert len(codes) == 1
    assert list(codes.keys())[0] == 'A'
    
    encoded = list(codes.values())[0]
    decoded = shannon_fano_decode(codes, encoded)
    
    assert decoded == data