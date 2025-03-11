import pytest
from datetime import datetime, timedelta
from src.date_utils import add_days_to_date

def test_add_days_to_datetime():
    """Test adding days to a datetime object."""
    base_date = datetime(2023, 1, 1)
    result = add_days_to_date(base_date, 10)
    assert result == datetime(2023, 1, 11)

def test_add_days_to_string_date():
    """Test adding days to a date string."""
    result = add_days_to_date('2023-01-01', 10)
    assert result == datetime(2023, 1, 11)

def test_subtract_days():
    """Test subtracting days."""
    base_date = datetime(2023, 1, 15)
    result = add_days_to_date(base_date, -5)
    assert result == datetime(2023, 1, 10)

def test_zero_days():
    """Test adding zero days."""
    base_date = datetime(2023, 1, 1)
    result = add_days_to_date(base_date, 0)
    assert result == base_date

def test_invalid_days_type():
    """Test raising error for non-integer days."""
    with pytest.raises(ValueError, match="Days must be an integer"):
        add_days_to_date(datetime(2023, 1, 1), '10')

def test_invalid_date_string():
    """Test raising error for invalid date string format."""
    with pytest.raises(ValueError, match="Invalid date string"):
        add_days_to_date('01-01-2023', 10)

def test_invalid_date_type():
    """Test raising error for invalid date type."""
    with pytest.raises(TypeError, match="Date must be a datetime object"):
        add_days_to_date(12345, 10)

def test_leap_year():
    """Test adding days across a leap year boundary."""
    base_date = datetime(2020, 2, 28)
    result = add_days_to_date(base_date, 1)
    assert result == datetime(2020, 2, 29)

    result = add_days_to_date(base_date, 2)
    assert result == datetime(2020, 3, 1)