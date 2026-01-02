"""Utilities for command-line tools and scripts."""

from importlib.metadata import version

__version__ = version("toolenv")

__all__ = [
    "__version__",
]
