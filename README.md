# GHPush

**GHPush** is an AI-powered command-line tool that automates the process of creating pull requests on GitHub. It leverages your local git diff, generates a PR title and description (using the OpenAI completions API optionally), pushes your branch, and then opens the GitHub PR creation page in your default browser. No GitHub token is required!

## Features

- **Automated PR Creation:** Push your branch and automatically open GitHub's PR page.
- **Diff Analysis:** Generate summaries of code changes by analyzing your local git diff.
- **AI-Powered Summaries (Optional):** If you provide an OpenAI API key, the tool uses GPT-3.5-turbo to create a more contextual and concise PR title and description.
- **Fallback Summarization:** In the absence of an API key or if the AI request fails, a basic summarization method is used.
- **Cross-Platform:** Designed to work seamlessly on Windows, macOS, and Linux.

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/sukeesh/ghpush.git
   cd ghpush
   ```

2. **Install Poetry** (if you haven't already):

   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   ```

3. **(Optional) Create and Activate a Virtual Environment Using pyenv**

   ```bash
   pyenv virtualenv 3.11.9 gpush
   pyenv activate gpush
   ```

4. **Install Dependencies with Poetry**

   ```bash
   poetry install
   ```

5. **Install pipx if you haven't already**

   ```bash
   python3 -m pip install --user pipx
   python3 -m pipx ensurepath
   ```

6. **Install ghpush**

   ```bash
   pipx install ghpush
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
ghpush --base main
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

