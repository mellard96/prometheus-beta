import os
import pytest
import tempfile

from src.file_exists import file_exists

def test_existing_file():
    """Test that file_exists returns True for an existing file."""
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file_path = temp_file.name
    
    try:
        assert file_exists(temp_file_path) is True
    finally:
        # Clean up the temporary file
        os.unlink(temp_file_path)

def test_non_existing_file():
    """Test that file_exists returns False for a non-existing file."""
    # Use a path that is extremely unlikely to exist
    assert file_exists('/path/to/definitely/nonexistent/file.txt') is False

def test_directory():
    """Test that file_exists returns False for a directory."""
    with tempfile.TemporaryDirectory() as temp_dir:
        assert file_exists(temp_dir) is False

def test_invalid_input_type():
    """Test that TypeError is raised for non-string inputs."""
    with pytest.raises(TypeError, match="File path must be a string"):
        file_exists(None)
    
    with pytest.raises(TypeError, match="File path must be a string"):
        file_exists(123)
    
    with pytest.raises(TypeError, match="File path must be a string"):
        file_exists(["file.txt"])

def test_empty_string():
    """Test behavior with an empty string path."""
    assert file_exists('') is False