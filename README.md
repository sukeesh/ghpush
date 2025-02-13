<div align="center">

# 🚀 GHPush

### AI-Powered GitHub Pull Request Creation Tool

[![PyPI version](https://badge.fury.io/py/ghpush.svg)](https://badge.fury.io/py/ghpush)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Downloads](https://pepy.tech/badge/ghpush)](https://pepy.tech/project/ghpush)

</div>

---

## 🌟 Overview

**GHPush** is an intelligent command-line tool that revolutionizes your GitHub workflow by automating pull request creation. Using the power of AI, it analyzes your changes, generates meaningful PR titles and descriptions, and streamlines your contribution process - all without requiring a GitHub token!

## ✨ Features

- 🤖 **AI-Powered Summaries:** Leverages OpenAI's GPT models to create contextual PR titles and descriptions
- 🔄 **Automated Workflow:** Push your branch and open GitHub's PR page in one command
- 📊 **Smart Diff Analysis:** Intelligent analysis of your code changes
- 🔒 **No GitHub Token Needed:** Works with your local git configuration
- 🌐 **Cross-Platform:** Seamless experience on Windows, macOS, and Linux
- ⚡ **Fallback Mode:** Basic summarization when AI is not configured

## 🚀 Quick Start

### Installation Options

#### 📦 Using pip (Recommended)
```bash
pip install ghpush
```

## 💫 Usage

```bash
ghpush --base main
```

That's it! GHPush will:
1. 📝 Analyze your changes
2. 🤖 Generate a PR title and description
3. 🔄 Push your branch
4. 🌐 Open the PR creation page

## ⚙️ Configuration

### OpenAI Integration (Required)

Set your OpenAI API key as an environment variable:

```bash
# Linux/macOS
export OPENAI_API_KEY=your-api-key-here

# Windows (PowerShell)
$env:OPENAI_API_KEY="your-api-key-here"
```

## 🛠 Technical Requirements

- Python ≥ 3.8.1
- Dependencies:
  - [Click](https://click.palletsprojects.com/) - CLI interface
  - [GitPython](https://gitpython.readthedocs.io/) - Git operations
  - [Rich](https://rich.readthedocs.io/) - Beautiful terminal output
  - [OpenAI](https://github.com/openai/openai-python) - AI integration
  - [python-dotenv](https://pypi.org/project/python-dotenv/) - Environment management

## 🤝 Contributing

We love contributions! Here's how you can help:

1. 🍴 Fork the repository
2. 🌿 Create your feature branch
3. 💻 Make your changes
4. 🔄 Create a pull request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🌟 Show Your Support

If you find GHPush useful, please consider:
- ⭐ Starring the repository
- 🐛 Reporting issues
- 🤝 Contributing to the code
- 📢 Spreading the word

---

<div align="center">
Made with ❤️ by <a href="https://github.com/sukeesh">Sukeesh</a>
</div>
