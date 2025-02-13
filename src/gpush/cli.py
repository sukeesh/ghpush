"""Command line interface for GPush."""
import click
from pathlib import Path
import webbrowser
import time
from rich.console import Console
from rich.panel import Panel
from rich.progress import (
    Progress, SpinnerColumn, TextColumn, 
    BarColumn, TimeElapsedColumn, TaskProgressColumn
)
from rich.live import Live
from rich.table import Table
from rich import box
from rich.style import Style
from rich.text import Text

from .git_operations import GitOperations
from .diff_analyzer import DiffAnalyzer
from .validators import validate_openai_key, validate_github_auth

console = Console()

class StatusProgress:
    def __init__(self):
        self.progress = Progress(
            SpinnerColumn(),
            TextColumn("[bold blue]{task.description}"),
            BarColumn(complete_style="green", finished_style="green"),
            TaskProgressColumn(),
            TimeElapsedColumn(),
            expand=True
        )
        self.tasks = {}

    def add_task(self, description: str) -> str:
        """Add a new task and return its ID."""
        return self.progress.add_task(description, total=100)

    def start_task(self, task_id: str, description: str):
        """Start a task with initial progress."""
        self.progress.update(task_id, completed=0, description=description)

    def update_task(self, task_id: str, advance: int, description: str = None):
        """Update task progress."""
        if description:
            self.progress.update(task_id, description=description)
        self.progress.update(task_id, advance=advance)

    def complete_task(self, task_id: str, success: bool = True):
        """Complete a task with success or failure indication."""
        status = "✅" if success else "❌"
        description = self.progress.tasks[task_id].description
        self.progress.update(
            task_id, 
            completed=100,
            description=f"{status} {description}"
        )

def create_status_table() -> Table:
    """Create a status table for progress display."""
    table = Table(
        box=box.ROUNDED,
        expand=True,
        show_header=False,
        border_style="blue",
        padding=(0, 1)
    )
    table.add_column("Status", style="bold cyan")
    table.add_column("Progress", ratio=2)
    return table

@click.command()
@click.option('--base', default='main', help='Base branch name')
def main(base):
    """GPush - Automated GitHub PR creation tool."""
    try:
        console.print(Panel.fit(
            "[bold blue]GPush[/] - GitHub PR Creation Tool",
            style="bold white on blue"
        ))
        console.print()

        status_progress = StatusProgress()
        
        with status_progress.progress:
            # Validation phase
            validate_task = status_progress.add_task("Validating prerequisites...")
            
            try:
                validate_openai_key()
                status_progress.update_task(validate_task, 50, "Validating GitHub CLI...")
                validate_github_auth()
                status_progress.complete_task(validate_task)
            except Exception as e:
                status_progress.complete_task(validate_task, success=False)
                raise e

            # Git operations phase
            git_task = status_progress.add_task("Initializing git operations...")
            git_ops = GitOperations()
            diff_analyzer = DiffAnalyzer()
            status_progress.complete_task(git_task)

            # Diff analysis phase
            diff_task = status_progress.add_task(f"Analyzing diff against {base} branch...")
            diff_text = git_ops.get_diff(base)
            status_progress.update_task(diff_task, 50)
            commit_messages = git_ops.get_commit_messages()
            status_progress.complete_task(diff_task)

            # AI generation phase
            ai_task = status_progress.add_task("Generating PR content using AI...")
            title, description = diff_analyzer.analyze_diff(diff_text, commit_messages)
            status_progress.complete_task(ai_task)

            # Push phase
            current_branch = git_ops.repo.active_branch.name
            push_task = status_progress.add_task(f"Pushing branch '{current_branch}'...")
            git_ops.push_branch(current_branch, base)
            status_progress.complete_task(push_task)

            # PR creation phase
            pr_task = status_progress.add_task("Preparing PR...")
            pr_url = git_ops.create_pr_url(base)
            if title and description:
                from urllib.parse import quote
                pr_url += f"&title={quote(title)}&body={quote(description)}"
            
            webbrowser.open(pr_url)
            status_progress.complete_task(pr_task)

        # Show final summary
        console.print()
        console.print(Panel(
            Text.from_markup(
                f"[bold green]✨ Success![/]\n\n"
                f"[cyan]Branch:[/] {current_branch}\n"
                f"[cyan]Title:[/] {title}\n"
                f"[cyan]Description preview:[/] {description[:100]}...\n\n"
                f"[cyan]PR URL:[/] {pr_url}"
            ),
            title="📦 Pull Request Ready",
            border_style="green",
            padding=(1, 2)
        ))

    except Exception as e:
        console.print()
        console.print(Panel(
            Text.from_markup(f"[bold red]Error:[/] {str(e)}"),
            title="❌ Error",
            border_style="red",
            padding=(1, 2)
        ))
        raise SystemExit(1)

if __name__ == "__main__":
    main()