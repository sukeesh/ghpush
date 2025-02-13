"""Validation utilities for GHPush."""
import os
import subprocess
from rich.console import Console

console = Console()

def validate_openai_key():
    """Validate OpenAI API key is set."""
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        console.print("[red]Error: OPENAI_API_KEY environment variable is not set.[/]")
        console.print("\nTo fix this:")
        console.print("1. Copy .env.example to .env:")
        console.print("   cp .env.example .env")
        console.print("2. Edit .env and add your OpenAI API key")
        raise SystemExit(1)
    return True

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