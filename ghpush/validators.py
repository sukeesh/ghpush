"""Validation utilities for GHPush."""
import os
import subprocess
from rich.console import Console
from .config import get_openai_api_key

console = Console()

def validate_openai_key():
    """Validate OpenAI API key is set."""
    api_key = get_openai_api_key()
    if not api_key:
        raise ValueError(
            "OpenAI API key not found.\n\n"
            "To fix this, set the OPENAI_API_KEY environment variable"
        )
    return api_key

def validate_github_auth():
    """Validate GitHub CLI authentication."""
    try:
        # Check if gh is installed
        result = subprocess.run(['gh', '--version'], 
                              capture_output=True, 
                              text=True)
        if result.returncode != 0:
            console.print("[red]Error: GitHub CLI (gh) is not installed.[/]")
            console.print("\nTo fix this:")
            console.print("1. Install GitHub CLI:")
            console.print("   brew install gh  # on macOS")
            console.print("   For other platforms, see: https://cli.github.com/")
            raise SystemExit(1)

        # Check if authenticated
        result = subprocess.run(['gh', 'auth', 'status'], 
                              capture_output=True, 
                              text=True)
        if result.returncode != 0:
            console.print("[red]Error: Not authenticated with GitHub.[/]")
            console.print("\nTo fix this:")
            console.print("1. Run: gh auth login")
            console.print("2. Follow the prompts to authenticate")
            raise SystemExit(1)
        
        return True
    except FileNotFoundError:
        console.print("[red]Error: GitHub CLI (gh) is not installed.[/]")
        console.print("\nTo fix this:")
        console.print("1. Install GitHub CLI:")
        console.print("   brew install gh  # on macOS")
        console.print("   For other platforms, see: https://cli.github.com/")
        raise SystemExit(1) 