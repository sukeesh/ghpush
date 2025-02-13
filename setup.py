from setuptools import setup, find_packages

setup(
    name="ghpush",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests",
        "click",
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