# GitHub Copilot Instructions for ronzz-py-tools

## Project Overview

ronzz-py-tools is a Python package providing miscellaneous tools for PDF, audio, video, and text processing. It includes utilities for document conversion, media downloading, audio processing, text manipulation, and translation.

## Project Structure

```
ronzz-py-tools/
├── src/
│   └── ronzz_tool/
│       ├── __init__.py          # Package initialization
│       ├── audio.py             # Audio trimming and conversion tools
│       ├── epub2md.py           # EPUB to Markdown converter
│       ├── img2SVG.py           # Image to SVG converter
│       ├── pdf2md.py            # PDF to Markdown converter
│       ├── pdf2png.py           # PDF image extraction
│       ├── textProc.py          # Text processing utilities
│       ├── translate.py         # Translation tools
│       └── youTube.py           # YouTube downloader
├── tests/                       # Test files and test data
│   ├── testInput/               # Test input files
│   └── testOutput/              # Test output files
├── pyproject.toml               # Project metadata and dependencies
├── README.md                    # Project documentation
└── .github/
    └── copilot-instructions.md  # This file
```

## Code Style and Conventions

### General Guidelines

1. **Python Version**: This project requires Python >= 3.12, < 3.14
2. **Code Style**: Follow PEP 8 guidelines for Python code
3. **Type Hints**: Use type hints where appropriate for function parameters and return values
4. **Docstrings**: Use clear docstrings for modules, classes, and functions (currently mix of French and English - prefer English for new code)
5. **File Organization**: Keep each tool in its own module file

### Naming Conventions

- **Functions**: Use `snake_case` for function names (e.g., `convert_pdf_to_markdown`)
- **Classes**: Use `PascalCase` for class names (e.g., `textProc`)
- **Variables**: Use `snake_case` for variable names
- **Constants**: Use `UPPER_SNAKE_CASE` for constants

### Module-Specific Patterns

#### PDF Processing (`pdf2md.py`)
- Functions return converted markdown as strings or write to files
- Support for extracting images alongside text
- CLI support via argparse
- Use pdfplumber for PDF operations

#### Audio Processing (`audio.py`)
- Time format: "MM:SS" string format converted to milliseconds
- Bulk operations support directory processing
- Default output format is MP3 for trimming, OGG for conversion
- Use pydub library for audio manipulation

#### Text Processing (`textProc.py`)
- Static methods in `textProc` class
- Support for regex-based text transformations
- VTT to TXT conversion preserves content but removes timestamps

#### YouTube Downloads (`youTube.py`)
- Support multiple formats: audio, video, both, subtitle_only
- Use yt-dlp library
- Support bulk downloads from URL lists
- Handle CSV input for batch operations

#### Translation (`translate.py`)
- Async operations using asyncio
- Block-based translation to respect API limits (4000 chars)
- Markdown-aware with syntax restoration
- Use googletrans library

## Dependencies

### Core Dependencies
- `pdfplumber`: PDF text and table extraction
- `markdownify`: HTML to Markdown conversion
- `googletrans`: Google Translate API
- `pydub`: Audio manipulation
- `yt-dlp`: YouTube video/audio downloading
- `ebooklib`: EPUB file reading
- `beautifulsoup4`: HTML parsing
- `requests`: HTTP requests
- `pyside6`: Qt GUI framework
- `pyperclip`: Clipboard operations

### External Tools
- **FFmpeg**: Required for audio/video processing
- **Inkscape**: Optional, required for SVG conversion

## Testing

### Test Structure
- Tests are located in the `tests/` directory
- Test input files go in `tests/testInput/`
- Test output files go in `tests/testOutput/`
- Temporary test files should not be committed to the source directory

### Writing Tests
When adding tests:
1. Place test files in the `tests/` directory
2. Use meaningful test file names
3. Clean up test outputs after test completion when appropriate
4. Do not commit test artifacts to version control

## Building and Publishing

### Building the Package
```bash
# Install build tools
pip install build

# Build the package
python -m build
```

### Publishing to PyPI
```bash
# Install twine
pip install twine

# Upload to PyPI
python -m twine upload dist/*
```

## Common Tasks

### Adding a New Tool
1. Create a new module file in `src/ronzz_tool/`
2. Implement the tool's functionality
3. Add appropriate docstrings and type hints
4. Support CLI usage with argparse if applicable
5. Update README.md with usage examples
6. Add tests if test infrastructure exists

### Updating Dependencies
1. Update version constraints in `pyproject.toml`
2. Test compatibility with updated versions
3. Update documentation if API changes

### Adding Documentation
1. Update README.md with clear usage examples
2. Include both programmatic and CLI usage when applicable
3. Document required external dependencies
4. Provide example code that can be run directly

## File Handling Patterns

### Input/Output Paths
- Accept both file paths and directory paths where appropriate
- Create output directories if they don't exist
- Use `os.path` or `pathlib` for path operations
- Handle encoding explicitly (typically UTF-8)

### Error Handling
- Provide meaningful error messages
- Validate input parameters
- Handle file I/O errors gracefully
- Print status messages for long-running operations

## Multi-language Support

Currently, the codebase contains a mix of French and English:
- Comments and docstrings: Mix of French and English
- User-facing messages: Some in French
- For new code: Prefer English for consistency with the broader Python community
- When modifying existing code: Match the existing style of that module

## Security Considerations

- Validate file paths to prevent path traversal attacks
- Sanitize user input before processing
- Be cautious with external command execution
- Handle credentials securely (never commit secrets)

## Performance Considerations

- Support bulk operations for file processing
- Use streaming for large files when possible
- Provide progress feedback for long-running operations
- Consider memory usage when processing large media files

## Git Workflow

### Files to Ignore
The following should NOT be committed:
- Test files in source directory (test.py, testTemp.py)
- Temporary files (temp.txt, scrap.txt)
- Build artifacts (dist/, build/, *.egg-info/)
- Virtual environments (.venv/, venv/)
- Cache files (__pycache__/, *.pyc)
- Editor/IDE settings (.vscode/, .idea/)

### Commit Guidelines
- Write clear, descriptive commit messages
- Keep commits focused on a single change
- Update tests when changing functionality
- Update documentation when changing APIs

## Resources

- PyPI: https://pypi.org/
- Project Repository: https://github.com/Ron-RONZZ-org/ronzz-py-tools
- Author Website: https://ronzz.org

## Questions or Issues?

For questions about the codebase or to report issues:
- Open an issue on GitHub: https://github.com/Ron-RONZZ-org/ronzz-py-tools/issues
- Contact: ron@ronzz.org
