"""Helper functions and utilities."""

from datetime import datetime, timedelta


def format_time(seconds):
    """Format seconds into human-readable time string.
    
    Args:
        seconds: Number of seconds.
        
    Returns:
        Formatted time string.
    """
    td = timedelta(seconds=seconds)
    hours, remainder = divmod(int(td.total_seconds()), 3600)
    minutes, seconds = divmod(remainder, 60)
    
    if hours > 0:
        return f"{hours}h {minutes}m {seconds}s"
    elif minutes > 0:
        return f"{minutes}m {seconds}s"
    else:
        return f"{seconds}s"


def validate_input(value, input_type=None):
    """Validate user input.
    
    Args:
        value: The input value to validate.
        input_type: Expected type ('int', 'float', 'str').
        
    Returns:
        Tuple of (is_valid, converted_value, error_message).
    """
    if not value or not str(value).strip():
        return False, None, "Value cannot be empty"
    
    value = str(value).strip()
    
    if input_type == 'int':
        try:
            return True, int(value), None
        except ValueError:
            return False, None, f"'{value}' is not a valid integer"
    
    elif input_type == 'float':
        try:
            return True, float(value), None
        except ValueError:
            return False, None, f"'{value}' is not a valid number"
    
    elif input_type == 'str':
        return True, value, None
    
    else:
        # Try to convert to int first, then float, then keep as string
        try:
            return True, int(value), None
        except ValueError:
            try:
                return True, float(value), None
            except ValueError:
                return True, value, None


def sanitize_value(value):
    """Sanitize a value for display.
    
    Args:
        value: The value to sanitize.
        
    Returns:
        Sanitized string representation.
    """
    return str(value)[:50]  # Limit to 50 characters
