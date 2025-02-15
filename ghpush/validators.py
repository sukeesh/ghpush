"""Validation utilities for GHPush."""
import os
import subprocess
from rich.console import Console
from .config import get_openai_api_key

console = Console()

def validate_openai_key():
    """Check for OpenAI API key and return whether AI features are available."""
    api_key = get_openai_api_key()
    if not api_key:
        console.print("\n[yellow]╭─ Mode: Basic Summary ──────────────────────────╮[/]")
        console.print("[yellow]│[/]  🤖 AI features are currently disabled          [yellow]│[/]")
        console.print("[yellow]│[/]  ℹ️  Operating in basic summary mode           [yellow]│[/]")
        console.print("[yellow]╰──────────────────────────────────────────────╯[/]")
        console.print("\n[cyan]To enable AI-powered features:[/]")
        console.print("  🔑 Set the [bold]OPENAI_API_KEY[/] environment variable")
        console.print("  💡 Restart ghpush after setting the key\n")
        return None
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