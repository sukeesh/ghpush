"""Analyze git diff to generate PR title and description."""
import re
from typing import Tuple, List
from pathlib import Path
from .ai_summarizer import AISummarizer

class DiffAnalyzer:
    MAX_TOKENS = 10000
    
    def __init__(self):
        self.ai_summarizer = AISummarizer()
    
    @staticmethod
    def estimate_tokens(text: str) -> int:
        """Rough estimation of tokens in text."""
        return len(text.split())
    
    def analyze_diff(self, diff_text: str, commit_messages: List[str]) -> Tuple[str, str]:
        """Analyze diff and generate PR title and description."""
        if self.estimate_tokens(diff_text) > self.MAX_TOKENS:
            return self._generate_large_diff_pr()
        
        # Try AI summarization first
        ai_title, ai_description = self.ai_summarizer.generate_summary(diff_text, commit_messages)
        if ai_title and ai_description:
            return ai_title, ai_description
            
        # Fall back to basic summarization if AI fails
        return self._generate_pr_content(diff_text, commit_messages)
    
    def _generate_pr_content(self, diff_text: str, commit_messages: List[str]) -> Tuple[str, str]:
        """Generate PR title and description from diff and commits."""
        # Get changed files
        changed_files = self._analyze_changed_files(diff_text)
        
        # Generate title
        title = self._generate_title(commit_messages, changed_files)
        
        # Generate description
        description = self._generate_description(commit_messages, changed_files, diff_text)
        
        return title, description
    
    def _analyze_changed_files(self, diff_text: str) -> List[dict]:
        """Analyze which files were changed and how."""
        files = []
        current_file = None
        
        for line in diff_text.split('\n'):
            if line.startswith('diff --git'):
                if current_file:
                    files.append(current_file)
                file_path = line.split(' b/')[-1]
                current_file = {
                    'path': file_path,
                    'extension': Path(file_path).suffix,
                    'additions': 0,
                    'deletions': 0
                }
            elif current_file and line.startswith('+') and not line.startswith('+++'):
                current_file['additions'] += 1
            elif current_file and line.startswith('-') and not line.startswith('---'):
                current_file['deletions'] += 1
        
        if current_file:
            files.append(current_file)
        
        return files
    
    def _generate_title(self, commit_messages: List[str], changed_files: List[dict]) -> str:
        """Generate PR title based on commits and changes."""
        if commit_messages:
            # Use the first commit message as base for the title
            title = commit_messages[0].split('\n')[0]  # First line of first commit
            # Remove any issue numbers, e.g., "#123: "
            title = re.sub(r'^#\d+:\s*', '', title)
            return title
        
        # Fallback: Generate title based on changes
        main_extensions = {f['extension'] for f in changed_files if f['extension']}
        if len(main_extensions) == 1:
            ext = main_extensions.pop().lstrip('.')
            return f"Update {ext} files"
        elif len(changed_files) == 1:
            return f"Update {Path(changed_files[0]['path']).name}"
        else:
            return f"Update {len(changed_files)} files"
    
    def _generate_description(self, commit_messages: List[str], 
                            changed_files: List[dict], diff_text: str) -> str:
        """Generate detailed PR description."""
        description = []
        
        # Add summary of changes
        if commit_messages:
            description.append("## Commit Summary")
            description.extend(f"* {msg.splitlines()[0]}" for msg in commit_messages)
            description.append("")
        
        # Add file changes section
        description.append("## Changes")
        for file in changed_files:
            changes = []
            if file['additions'] > 0:
                changes.append(f"{file['additions']} addition{'s' if file['additions'] > 1 else ''}")
            if file['deletions'] > 0:
                changes.append(f"{file['deletions']} deletion{'s' if file['deletions'] > 1 else ''}")
            
            description.append(f"* {file['path']} ({', '.join(changes)})")
        
        # Add statistics
        total_additions = sum(f['additions'] for f in changed_files)
        total_deletions = sum(f['deletions'] for f in changed_files)
        description.append("")
        description.append("## Statistics")
        description.append(f"* Files changed: {len(changed_files)}")
        description.append(f"* Lines added: {total_additions}")
        description.append(f"* Lines removed: {total_deletions}")
        
        return "\n".join(description)
    
    def _generate_large_diff_pr(self) -> Tuple[str, str]:
        """Generate generic PR content for large diffs."""
        return (
            "Large code change",
            "This PR contains extensive changes. Please review carefully."
        ) 