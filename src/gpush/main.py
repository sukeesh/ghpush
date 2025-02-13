import os

def create_pr(summarizer, diff_text, commit_messages):
    title, description = summarizer.generate_summary(diff_text, commit_messages)
    
    if title and description:
        # Escape quotes in title and description to prevent command injection
        title = title.replace('"', '\\"')
        description = description.replace('"', '\\"')
        
        # Create PR with generated title and description
        os.system(f'gh pr create --title "{title}" --body "{description}"')
    else:
        # Fallback to basic PR creation
        os.system('gh pr create') 