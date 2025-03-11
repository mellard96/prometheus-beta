import os
import pytest
import tempfile
import shutil

from src.file_rename import rename_file

def test_rename_file_success():
    """Test successful file renaming."""
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create a test file
        original_path = os.path.join(temp_dir, 'original.txt')
        with open(original_path, 'w') as f:
            f.write('Test content')
        
        # Rename the file
        new_path = rename_file(original_path, 'renamed.txt')
        
        # Check the new file exists and the old one doesn't
        assert os.path.exists(new_path)
        assert not os.path.exists(original_path)
        assert new_path.endswith('renamed.txt')

def test_rename_file_invalid_source():
    """Test renaming a non-existent file raises FileNotFoundError."""
    with pytest.raises(FileNotFoundError):
        rename_file('/path/to/nonexistent/file.txt', 'new_name.txt')

def test_rename_file_invalid_inputs():
    """Test invalid input handling."""
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create a test file
        test_file = os.path.join(temp_dir, 'test.txt')
        with open(test_file, 'w') as f:
            f.write('Test content')
        
        # Test empty source path
        with pytest.raises(ValueError):
            rename_file('', 'new_name.txt')
        
        # Test empty new name
        with pytest.raises(ValueError):
            rename_file(test_file, '')
        
        # Test non-string inputs
        with pytest.raises(ValueError):
            rename_file(None, 'new_name.txt')
        with pytest.raises(ValueError):
            rename_file(test_file, None)

def test_rename_file_directory_not_allowed():
    """Test that renaming a directory is not allowed."""
    with tempfile.TemporaryDirectory() as temp_dir:
        with pytest.raises(ValueError):
            rename_file(temp_dir, 'new_dir_name')

def test_rename_file_destination_exists():
    """Test renaming to an existing file raises an error."""
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create two test files
        file1_path = os.path.join(temp_dir, 'file1.txt')
        file2_path = os.path.join(temp_dir, 'file2.txt')
        
        with open(file1_path, 'w') as f:
            f.write('Test content 1')
        with open(file2_path, 'w') as f:
            f.write('Test content 2')
        
        # Try to rename file1 to file2's name
        with pytest.raises(FileExistsError):
            rename_file(file1_path, 'file2.txt')