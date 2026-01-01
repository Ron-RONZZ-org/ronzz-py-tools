"""
ronzz-tool: A collection of miscellaneous Python tools.

This package provides utilities for:
- PDF processing (conversion, extraction)
- EPUB to Markdown conversion
- Audio processing (trimming, conversion)
- Video downloading (YouTube)
- Text processing and translation
- Image conversion

For detailed usage examples, see the README.md file.
"""

__version__ = "0.1.0"
__author__ = "Ron Chou"
__email__ = "ron@ronzz.org"
__license__ = "AGPL-3.0"

# Export main modules for easier imports
__all__ = [
    "audio",
    "epub2md",
    "img2SVG",
    "pdf2md",
    "pdf2png",
    "textProc",
    "translate",
    "youTube",
]
