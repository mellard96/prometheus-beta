from datetime import datetime, timedelta

def add_days_to_date(date, days):
    """
    Add a specified number of days to a given date.

    Args:
        date (datetime or str): The starting date. 
            If str, expected format is 'YYYY-MM-DD'.
        days (int): Number of days to add. Can be positive or negative.

    Returns:
        datetime: A new datetime object representing the date after adding days.

    Raises:
        TypeError: If date is not a datetime or valid date string.
        ValueError: If days is not an integer.
    """
    # Validate input type for days
    if not isinstance(days, int):
        raise ValueError("Days must be an integer")

    # Convert string to datetime if needed
    if isinstance(date, str):
        try:
            date = datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Invalid date string. Use format 'YYYY-MM-DD'")
    
    # Validate input type for date
    if not isinstance(date, datetime):
        raise TypeError("Date must be a datetime object or a string in 'YYYY-MM-DD' format")

    # Add days and return new date
    return date + timedelta(days=days)