"""Operation logger for recording operations to file."""

import json
from pathlib import Path
from datetime import datetime


class OperationLogger:
    """Logger for recording operations to JSON file."""

    def __init__(self, log_file="data/logs/operations.log.json"):
        """Initialize the operation logger.
        
        Args:
            log_file: Path to the log file.
        """
        self.log_file = Path(log_file)
        self.log_file.parent.mkdir(parents=True, exist_ok=True)
        self.operations = []
        self._load_log()

    def log_operation(self, operation, value=None, result=None):
        """Log an operation.
        
        Args:
            operation: The operation performed.
            value: The value used (if applicable).
            result: The result of the operation.
        """
        entry = {
            'timestamp': datetime.now().isoformat(),
            'operation': operation,
            'value': value,
            'result': result
        }
        self.operations.append(entry)
        self._save_log()

    def _load_log(self):
        """Load operations from log file."""
        if self.log_file.exists():
            try:
                with open(self.log_file, 'r') as f:
                    self.operations = json.load(f)
            except (json.JSONDecodeError, IOError):
                self.operations = []

    def _save_log(self):
        """Save operations to log file."""
        try:
            with open(self.log_file, 'w') as f:
                json.dump(self.operations, f, indent=2)
        except IOError as e:
            print(f"Error saving log: {e}")

    def clear_log(self):
        """Clear the log file."""
        self.operations = []
        self._save_log()

    def get_operations(self):
        """Get all logged operations.
        
        Returns:
            A list of operation dictionaries.
        """
        return self.operations.copy()
