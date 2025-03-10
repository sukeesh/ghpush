"""Configuration management for GHPush."""
import json
import os
from pathlib import Path

class Config:
    def __init__(self):
        self.config_dir = Path.home() / ".ghpush"
        self.config_file = self.config_dir / "config.json"
        self._ensure_config_dir()
        self.config = self._load_config()

    def _ensure_config_dir(self):
        """Ensure configuration directory exists."""
        self.config_dir.mkdir(exist_ok=True)

    def _load_config(self):
        """Load configuration from file."""
        if self.config_file.exists():
            with open(self.config_file, 'r') as f:
                return json.load(f)
        return {}

    def save_config(self):
        """Save configuration to file."""
        with open(self.config_file, 'w') as f:
            json.dump(self.config, f)

    def set_github_token(self, token: str):
        """Set GitHub token in configuration."""
        self.config['github_token'] = token
        self.save_config()

    def get_github_token(self) -> str:
        """Get GitHub token from configuration or environment."""
        return os.getenv('GITHUB_TOKEN') or self.config.get('github_token')

def get_openai_api_key():
    """Get OpenAI API key from environment."""
    return os.getenv('OPENAI_API_KEY') 