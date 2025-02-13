# GPush

**GPush** is a command-line tool that automates the process of creating pull requests on GitHub. It leverages your local git diff, generates a PR title and description (using the OpenAI completions API optionally), pushes your branch, and then opens the GitHub PR creation page in your default browser. No GitHub token is required!

## Features

- **Automated PR Creation:** Push your branch and automatically open GitHub's PR page.
- **Diff Analysis:** Generate summaries of code changes by analyzing your local git diff.
- **AI-Powered Summaries (Optional):** If you provide an OpenAI API key, the tool uses GPT-3.5-turbo to create a more contextual and concise PR title and description.
- **Fallback Summarization:** In the absence of an API key or if the AI request fails, a basic summarization method is used.
- **Cross-Platform:** Designed to work seamlessly on Windows, macOS, and Linux.

## Installation

### Installation

#### Using Pipx (All Platforms)
```bash
# Install pipx if you haven't already
python3 -m pip install --user pipx
python3 -m pipx ensurepath

# Install gpush
pipx install gpush
```

That's it! You can now use `gpush` from anywhere.

### Alternative Installation Methods

#### Using Homebrew (macOS/Linux)
```bash
brew tap sukeesh/gpush
brew install gpush
```

### Binary Installation

Download the latest binary for your platform from our [releases page](https://github.com/sukeesh/gpush/releases).

#### Windows
1. Download `gpush-windows-latest.exe`
2. Rename to `gpush.exe`
3. Move to a directory in your PATH

#### macOS/Linux
1. Download the appropriate binary
2. Make it executable: `chmod +x gpush`
3. Move to a directory in your PATH: `sudo mv gpush /usr/local/bin/`

### Development Installation

```bash
git clone https://github.com/sukeesh/gpush.git
cd gpush
poetry install
```

## Configuration

### OpenAI API Key (Optional)

To enable AI-powered PR title and description generation:

1. Copy the example environment file:

   ```bash
   cp .env.example .env
   ```

2. Edit the `.env` file and replace the placeholder with your OpenAI API key:

   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   ```

If no OpenAI API key is set, GPush will automatically fall back to its basic summarization method.  
**Note:** The previous requirement for a GitHub token has been removed since GPush relies on local git operations to generate PR URLs.

## Usage

Run the tool from the command line as follows:

```bash
gpush --base main
```

This command does the following:

- Computes the git diff between your current branch and the base branch (`main` by default).
- Pushes your current branch to the remote repository.
- Generates a PR title and description using AI summarization (if available) or a basic method otherwise.
- Opens your default web browser with GitHub's PR creation page pre-filled with the generated title and description

## Dependencies

- **Python:** >=3.8.1, <4.0
- [**Click**](https://click.palletsprojects.com/) for building the command-line interface.
- [**GitPython**](https://gitpython.readthedocs.io/) for handling git operations.
- [**Rich**](https://rich.readthedocs.io/) for enhanced terminal output.
- [**OpenAI**](https://github.com/openai/openai-python) for integration with GPT models (optional).
- [**python-dotenv**](https://pypi.org/project/python-dotenv/) for loading environment variables from the `.env` file.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your enhancements.

## License

This project is licensed under the MIT License.

