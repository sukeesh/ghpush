<div align="center">

# 🚀 GHPush

### AI-Powered GitHub Pull Request Creation Tool

[![PyPI version](https://img.shields.io/pypi/v/ghpush)](https://pypi.org/project/ghpush/)
[![PyPI downloads](https://img.shields.io/pypi/dm/ghpush)](https://pypi.org/project/ghpush/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

</div>

---

## 🌟 Overview

**GHPush** is an intelligent command-line tool that revolutionizes your GitHub workflow by automating pull request creation. It operates in two modes:

- 🤖 **AI Mode**: Generates detailed, context-aware PR titles and descriptions using OpenAI
- 📝 **Basic Mode**: Creates simple, effective summaries based on file changes

## ✨ Features

- 🔄 **Dual Operation Modes:**
  - **AI-Powered Mode:** Rich, contextual PR summaries using OpenAI
  - **Basic Mode:** Simple, effective change summaries
- 🚀 **Automated Workflow:** Push your branch and open GitHub's PR page in one command
- 📊 **Smart Diff Analysis:** Intelligent analysis of your code changes
- 🔒 **No GitHub Token Needed:** Works with your local git configuration
- 🌐 **Cross-Platform:** Seamless experience on Windows, macOS, and Linux

## 🚀 Quick Start

### Installation

```bash
pip install ghpush
```

> 💡 **Check out [ghpush on PyPI](https://pypi.org/project/ghpush/) for the latest version and release notes.**

### Basic Usage

```bash
ghpush --base main
```

That's it! GHPush will:
1. 📝 Analyze your changes
2. 🤖 Generate a PR title and description (AI or Basic mode)
3. 🔄 Push your branch
4. 🌐 Open the PR creation page

## ⚙️ Configuration

### Operating Modes

#### 🤖 AI Mode (Optional)
To enable AI-powered summaries:
```bash
# Linux/macOS
export OPENAI_API_KEY=your-api-key-here

# Windows (PowerShell)
$env:OPENAI_API_KEY="your-api-key-here"
```

#### 📝 Basic Mode
- Automatically used when OpenAI API key is not set
- No configuration needed
- Provides simple summaries based on changed files

## 🛠 Technical Requirements

- Python ≥ 3.8.1
- Dependencies:
  - [Click](https://click.palletsprojects.com/) - CLI interface
  - [GitPython](https://gitpython.readthedocs.io/) - Git operations
  - [Rich](https://rich.readthedocs.io/) - Beautiful terminal output
  - [OpenAI](https://github.com/openai/openai-python) - AI integration (optional)

## 🤝 Contributing

We love contributions! Here's how you can help:

### 🛠️ Development Setup

1. Clone the repository:
```bash
git clone https://github.com/sukeesh/ghpush
cd ghpush
```

2. Set up Python environment:

#### Using pyenv (Recommended)
```bash
# Install Python 3.8 or later
pyenv install 3.8.1

# Create a virtual environment
pyenv virtualenv 3.8.1 ghpush-dev

# Activate the environment
pyenv activate ghpush-dev
```

#### Using venv (Alternative)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -e .
```

4. Run locally:
```bash
# Using Python module directly (recommended for development)
python -m ghpush.cli --base main

# Or after installing in development mode
ghpush --base main
```

> 💡 **Note:** Using pyenv is recommended as it provides better Python version management and isolation.

### 🔄 Contribution Steps

1. 🍴 Fork the repository
2. 🌿 Create your feature branch (`git checkout -b feature/amazing-feature`)
3. 💻 Make your changes
4. ✅ Ensure tests pass
5. 📝 Update documentation if needed
6. 🔄 Create a pull request

### 🧪 Testing

```bash
# Install test dependencies
pip install pytest

# Run tests
pytest
```

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
Made by <a href="https://github.com/sukeesh">Sukeesh</a>
</div>
