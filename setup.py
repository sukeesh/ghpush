from setuptools import setup, find_packages
import os
import re

def get_version():
    init = open(os.path.join("ghpush", "__init__.py")).read()
    return re.search(r"""__version__ = ["']{1,3}(.+?)["']{1,3}""", init).group(1)

setup(
    name="ghpush",
    version=get_version(),
    packages=find_packages(),
    install_requires=[
        "click",
        "gitpython",
        "rich",
        "openai",
        "python-dotenv",
    ],
    entry_points={
        "console_scripts": [
            "ghpush=ghpush.cli:main",
        ],
    },
    author="Sukeesh",
    author_email="vsukeeshbabu@gmail.com",
    description="An AI tool to push files to GitHub repositories",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/sukeesh/ghpush",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
) 