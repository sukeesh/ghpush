"""Git operations handler."""
import subprocess
from typing import List, Tuple
from git import Repo
from pathlib import Path
import webbrowser

class GitOperations:
    def __init__(self, repo_path: Path = None):
        self.repo_path = repo_path or Path.cwd()
        self.repo = Repo(self.repo_path)

    def create_branch(self, branch_name: str):
        """Create and checkout a new branch."""
        current = self.repo.active_branch
        new_branch = self.repo.create_head(branch_name)
        new_branch.checkout()
        return current.name

    def get_diff(self, base_branch: str) -> str:
        """Get git diff between current branch and base branch."""
        return self.repo.git.diff(base_branch)

    def push_branch(self, branch_name: str, base_branch: str):
        """Push branch to remote with upstream tracking."""
        remote = self.repo.remote()
        remote.push(refspec=f'{branch_name}:refs/heads/{branch_name}', set_upstream=True)

    def get_commit_messages(self) -> List[str]:
        """Get commit messages since branching from base."""
        base_branch = self.repo.active_branch.tracking_branch()
        if not base_branch:
            return []
        commits = list(self.repo.iter_commits(f'{base_branch.name}..HEAD'))
        return [commit.message.strip() for commit in commits]

    def get_remote_url(self) -> str:
        """Get the remote URL and convert to HTTPS if needed."""
        remote_url = self.repo.remotes.origin.url
        if remote_url.startswith('git@github.com:'):
            # Convert SSH URL to HTTPS URL
            remote_url = remote_url.replace('git@github.com:', 'https://github.com/')
        if remote_url.endswith('.git'):
            remote_url = remote_url[:-4]
        return remote_url

    def create_pr_url(self, base_branch: str) -> str:
        """Create the URL for opening a new PR on GitHub."""
        remote_url = self.get_remote_url()
        current_branch = self.repo.active_branch.name
        return f"{remote_url}/compare/{base_branch}...{current_branch}?expand=1"

    def open_pr_in_browser(self, base_branch: str):
        """Open the PR creation page in the default browser."""
        pr_url = self.create_pr_url(base_branch)
        webbrowser.open(pr_url) 