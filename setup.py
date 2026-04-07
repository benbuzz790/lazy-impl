"""Setup configuration for lazy-impl package.
This package provides experimental LLM-powered code generation decorators
that generate Python implementations at runtime.
WARNING: This is experimental software that modifies your source files.
Use at your own risk.
"""
from setuptools import setup, find_packages
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
setup(
    name="lazy-impl",
    version="0.1.0",
    author="lazy-impl contributors",
    author_email="",
    description="Experimental LLM-powered code generation decorators (USE AT YOUR OWN RISK)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/your-org/lazy-impl",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Code Generators",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[
        "anthropic>=0.18.0",
        "openai>=1.0.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "black>=23.0.0",
            "flake8>=6.0.0",
        ],
    },
    keywords="llm code-generation experimental ai anthropic openai claude gpt",
    project_urls={
        "Bug Reports": "https://github.com/your-org/lazy-impl/issues",
        "Source": "https://github.com/your-org/lazy-impl",
    },
)
