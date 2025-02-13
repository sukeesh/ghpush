"""Command line interface for GPush."""
import click
from pathlib import Path
import webbrowser
import time
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TimeElapsedColumn
from rich.live import Live
from rich.table import Table
from rich import box

from .git_operations import GitOperations
from .diff_analyzer import DiffAnalyzer
from .validators import validate_openai_key, validate_github_auth

console = Console()

def create_status_table() -> Table:
    """Create a status table for progress display."""
    table = Table(box=box.ROUNDED, expand=True, show_header=False)
    table.add_column("Status", style="bold cyan")
    table.add_column("Description")
    return table

@click.command()
@click.option('--base', default='main', help='Base branch name')
def main(base):
    """GPush - Automated GitHub PR creation tool."""
    try:
        # Create status table
        status_table = create_status_table()
        
        with Live(status_table, refresh_per_second=4) as live:
            # Validate prerequisites
            status_table.add_row("🔍", "Validating prerequisites...")
            live.refresh()
            
            validate_openai_key()
            status_table.add_row("✅", "OpenAI API key validated")
            live.refresh()
            
            validate_github_auth()
            status_table.add_row("✅", "GitHub CLI authentication validated")
            live.refresh()

            # Initialize git operations
            status_table.add_row("🔄", "Initializing git operations...")
            live.refresh()
            git_ops = GitOperations()
            diff_analyzer = DiffAnalyzer()

            # Get the diff
            status_table.add_row("📝", f"Analyzing diff against {base} branch...")
            live.refresh()
            diff_text = git_ops.get_diff(base)
            commit_messages = git_ops.get_commit_messages()

            # Generate PR content
            status_table.add_row("🤖", "Generating PR content using AI...")
            live.refresh()
            title, description = diff_analyzer.analyze_diff(diff_text, commit_messages)

            # Push branch
            current_branch = git_ops.repo.active_branch.name
            status_table.add_row("⬆️ ", f"Pushing branch '{current_branch}' to remote...")
            live.refresh()
            git_ops.push_branch(current_branch, base)

            # Create PR URL
            status_table.add_row("🔗", "Preparing PR URL...")
            live.refresh()
            pr_url = git_ops.create_pr_url(base)
            if title and description:
                from urllib.parse import quote
                pr_url += f"&title={quote(title)}&body={quote(description)}"

            # Final steps
            status_table.add_row("🌐", "Opening PR creation page in browser...")
            live.refresh()
            webbrowser.open(pr_url)

            # Success message
            status_table.add_row("✨", "All done!")
            live.refresh()

        # Show final summary
        console.print("\n")
        console.print(Panel(
            f"[bold green]Success![/]\n\n"
            f"[cyan]Branch:[/] {current_branch}\n"
            f"[cyan]Title:[/] {title}\n"
            f"[cyan]Description preview:[/] {description[:100]}...\n\n"
            f"[cyan]PR URL:[/] {pr_url}",
            title="📦 Pull Request Ready",
            border_style="green"
        ))

    except Exception as e:
        console.print("\n")
        console.print(Panel(
            f"[bold red]Error:[/] {str(e)}",
            title="❌ Error",
            border_style="red"
        ))
        raise SystemExit(1)

if __name__ == "__main__":
    main()