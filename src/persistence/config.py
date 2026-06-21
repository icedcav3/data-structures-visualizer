"""Configuration management."""

import json
from pathlib import Path


class Config:
    """Configuration manager for user preferences."""

    DEFAULT_CONFIG = {
        'theme': 'light',
        'animation_speed': 500,  # milliseconds
        'default_structure': 'stack',
        'window_width': 1200,
        'window_height': 800,
    }

    def __init__(self, config_file="data/config.json"):
        """Initialize the configuration manager.
        
        Args:
            config_file: Path to the configuration file.
        """
        self.config_file = Path(config_file)
        self.config_file.parent.mkdir(parents=True, exist_ok=True)
        self.config = self.DEFAULT_CONFIG.copy()
        self._load_config()

    def get(self, key, default=None):
        """Get a configuration value.
        
        Args:
            key: The configuration key.
            default: Default value if key not found.
            
        Returns:
            The configuration value.
        """
        return self.config.get(key, default)

    def set(self, key, value):
        """Set a configuration value.
        
        Args:
            key: The configuration key.
            value: The value to set.
        """
        self.config[key] = value
        self._save_config()

    def _load_config(self):
        """Load configuration from file."""
        if self.config_file.exists():
            try:
                with open(self.config_file, 'r') as f:
                    loaded = json.load(f)
                    self.config.update(loaded)
            except (json.JSONDecodeError, IOError):
                pass

    def _save_config(self):
        """Save configuration to file."""
        try:
            with open(self.config_file, 'w') as f:
                json.dump(self.config, f, indent=2)
        except IOError as e:
            print(f"Error saving config: {e}")
