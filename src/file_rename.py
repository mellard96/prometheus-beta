import os
import shutil

def rename_file(source_path, new_name):
    """
    Rename a file to a new name while preserving its original directory.

    Args:
        source_path (str): The full path to the existing file.
        new_name (str): The new filename (without path).

    Returns:
        str: The full path to the new file.

    Raises:
        FileNotFoundError: If the source file does not exist.
        ValueError: If the new name is invalid or empty.
        PermissionError: If there are insufficient permissions to rename the file.
        OSError: For other OS-related errors during file renaming.
    """
    # Validate inputs
    if not source_path or not isinstance(source_path, str):
        raise ValueError("Source path must be a non-empty string")
    
    if not new_name or not isinstance(new_name, str):
        raise ValueError("New name must be a non-empty string")
    
    # Normalize paths to handle different separators
    source_path = os.path.normpath(source_path)
    
    # Check if source file exists
    if not os.path.exists(source_path):
        raise FileNotFoundError(f"Source file not found: {source_path}")
    
    # Check if source is a file, not a directory
    if not os.path.isfile(source_path):
        raise ValueError(f"Source path is not a file: {source_path}")
    
    # Get the directory of the source file
    directory = os.path.dirname(source_path)
    
    # Create the new file path
    new_path = os.path.join(directory, new_name)
    
    # Check if new path already exists
    if os.path.exists(new_path):
        raise FileExistsError(f"Destination file already exists: {new_path}")
    
    try:
        # Rename the file
        os.rename(source_path, new_path)
        return new_path
    except PermissionError:
        raise PermissionError(f"Permission denied when renaming file: {source_path}")
    except OSError as e:
        raise OSError(f"Error renaming file: {e}")