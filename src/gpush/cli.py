"""Command line interface for GPush."""
import click
from pathlib import Path
import webbrowser
from rich.console import Console
from rich.panel import Panel

from .git_operations import GitOperations
from .diff_analyzer import DiffAnalyzer
from .validators import validate_openai_key, validate_github_auth

console = Console()

@click.command()
@click.option('--base', default='main', help='Base branch name')
def main(base):
    """GPush - Automated GitHub PR creation tool."""
    try:
        # Validate prerequisites
        validate_openai_key()
        validate_github_auth()

        git_ops = GitOperations()
        diff_analyzer = DiffAnalyzer()

        # Get the diff
        diff_text = git_ops.get_diff(base)
        commit_messages = git_ops.get_commit_messages()

        # Analyze diff and generate PR content
        title, description = diff_analyzer.analyze_diff(diff_text, commit_messages)

        # Push branch
        current_branch = git_ops.repo.active_branch.name
        git_ops.push_branch(current_branch, base)

        # Create PR URL with the generated title and description
        pr_url = git_ops.create_pr_url(base)
        # Add title and description as URL parameters
        if title and description:
            from urllib.parse import quote
            pr_url += f"&title={quote(title)}&body={quote(description)}"

        # Open in browser
        webbrowser.open(pr_url)
        
        console.print(Panel(
            f"Branch pushed and PR page opened in browser!\n"
            f"Title: {title}\n"
            f"Description preview: {description[:100]}...", 
            style="green"
        ))

    except Exception as e:
        console.print(Panel(f"Error: {str(e)}", style="red"))

if __name__ == "__main__":
    main()