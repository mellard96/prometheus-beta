import pytest
import logging
import io
import sys
from src.warning_logger import log_warning

def test_log_warning_basic(caplog):
    """Test basic warning logging functionality."""
    caplog.set_level(logging.WARNING)
    log_warning("Test warning message")
    assert len(caplog.records) == 1
    assert caplog.records[0].levelname == "WARNING"
    assert "Test warning message" in caplog.text

def test_log_warning_input_types():
    """Test input validation for different types."""
    # Test with non-string input
    with pytest.raises(TypeError, match="Warning message must be a string"):
        log_warning(123)
    
    with pytest.raises(TypeError, match="Warning message must be a string"):
        log_warning(None)

def test_log_warning_empty_string():
    """Test handling of empty string input."""
    with pytest.raises(ValueError, match="Warning message cannot be empty"):
        log_warning("")
    
    with pytest.raises(ValueError, match="Warning message cannot be empty"):
        log_warning("   ")

def test_log_warning_whitespace_stripped(caplog):
    """Test that whitespace-only strings are considered empty."""
    caplog.set_level(logging.WARNING)
    with pytest.raises(ValueError, match="Warning message cannot be empty"):
        log_warning("\t\n ")
    assert len(caplog.records) == 0