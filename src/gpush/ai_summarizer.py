"""OpenAI integration for PR summary generation."""
import os
from typing import Tuple
from openai import OpenAI
from dotenv import load_dotenv
from rich.console import Console

# Load environment variables from .env file
load_dotenv()

console = Console()

class AISummarizer:
    def __init__(self):
        self.api_key = os.getenv('OPENAI_API_KEY')
        if not self.api_key:
            console.print("[yellow]Warning: OPENAI_API_KEY not found. Will use basic summarization.[/]")
        self.client = OpenAI(api_key=self.api_key)

    def generate_summary(self, diff_text: str, commit_messages: list[str]) -> Tuple[str, str]:
        """Generate PR title and description using OpenAI."""
        if not self.api_key:
            return None, None

        try:
            # Prepare the prompt
            prompt = self._create_prompt(diff_text, commit_messages)

            # Get completion from OpenAI using ChatCompletion API
            response = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant that generates clear and concise PR titles and descriptions based on git diffs and commit messages."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=1000
            )

            # Parse the response
            content = response.choices[0].message.content
            title, description = self._parse_ai_response(content)
            return title, description

        except Exception as e:
            console.print(f"[yellow]Warning: AI summarization failed ({str(e)}). Using basic summarization.[/]")
            return None, None

    def _create_prompt(self, diff_text: str, commit_messages: list[str]) -> str:
        """Create the prompt for OpenAI."""
        prompt = "Please generate a Pull Request title and description based on the following information:\n\n"

        if commit_messages:
            prompt += "Commit Messages:\n"
            for msg in commit_messages:
                prompt += f"- {msg}\n"
            prompt += "\n"

        prompt += "Git Diff Summary:\n"
        prompt += diff_text[:3000] + ("..." if len(diff_text) > 3000 else "")

        prompt += "\n\nPlease provide your response in the following format:\n"
        prompt += "TITLE: <concise title>\n"
        prompt += "DESCRIPTION:\n<detailed description with markdown formatting>"

        return prompt

    def _parse_ai_response(self, response: str) -> Tuple[str, str]:
        """Parse the AI response into title and description."""
        try:
            # Split into title and description
            parts = response.split('DESCRIPTION:', 1)
            title = parts[0].replace('TITLE:', '').strip()
            description = parts[1].strip() if len(parts) > 1 else ""

            return title, description
        except Exception:
            return None, None 