# ronzz-py-tools

A collection of miscellaneous Python tools for PDF, audio, video, and text processing. This package provides utilities for converting documents, downloading YouTube videos, processing audio files, and more.

## Features

- **PDF Processing**: Convert PDF files to Markdown, extract images from PDFs
- **EPUB Processing**: Convert EPUB files to Markdown
- **Audio Processing**: Trim and convert audio files in bulk
- **Video Processing**: Download YouTube videos and audio with subtitles
- **Text Processing**: Process and transform text, convert VTT to TXT
- **Translation**: Translate Markdown files using Google Translate
- **Image Processing**: Convert images to SVG format

## Installation

Install from PyPI (once published):

```bash
pip install ronzz-tool
```

Or install from source:

```bash
git clone https://github.com/Ron-RONZZ-org/ronzz-py-tools.git
cd ronzz-py-tools
pip install -e .
```

## Requirements

- Python >= 3.12, < 3.14
- Dependencies are automatically installed with the package

### External Dependencies

Some features require external tools:
- **FFmpeg**: Required for audio and video processing
- **Inkscape**: Required for SVG conversion (optional)

## Usage

### PDF to Markdown Conversion

```python
from ronzz_tool.pdf2md import convert_pdf_to_markdown

# Convert PDF to Markdown
convert_pdf_to_markdown(
    pdf_path="input.pdf",
    output_md_path="output.md",
    extract_imgs=True,  # Extract images
    img_folder="images"  # Folder for images
)
```

**CLI Usage:**
```bash
python -m ronzz_tool.pdf2md --input input.pdf --output output.md --extract-images
```

### EPUB to Markdown Conversion

```python
from ronzz_tool.epub2md import epub_to_markdown

# Convert EPUB to Markdown
epub_to_markdown("input.epub", "output.md")
```

**CLI Usage:**
```bash
python -m ronzz_tool.epub2md input.epub output.md
```

### Audio Processing

```python
from ronzz_tool.audio import trim_audio_bulk, audio_convert_bulk

# Trim audio into multiple clips
trim_audio_bulk(
    input_path="audio.mp3",
    time_ranges=[("0:00", "0:30"), ("0:30", "1:00")],
    output_dir="clips",
    clip_names=["intro", "main"]
)

# Convert multiple audio files to OGG format
audio_convert_bulk(input_dir="input_audio", output_dir="output_audio")
```

### YouTube Download

```python
from ronzz_tool.youTube import download_youtube

# Download YouTube videos
youtube_urls = ["https://youtube.com/watch?v=..."]
download_youtube(
    youtube_url_list=youtube_urls,
    output_path="./downloads",
    format="audio",  # or "video", "both", "subtitle_only"
    preferred_audio_quality="192",
    subtitle=True
)
```

### Text Processing

```python
from ronzz_tool.textProc import textProc

# Convert VTT subtitle files to plain text
txt_files = textProc.vtt_to_txt(
    path="subtitles.vtt",  # or directory path
    txt_path="output.txt"
)

# Regex-based text substitution
replacements = {"hello": "hi", "world": "earth"}
result = textProc.regex_sub("hello world", replacements)

# Split text by uppercase letters
words = textProc.split_by_uppercase("HelloWorld")  # ["Hello", "World"]
```

### Translation

```python
from ronzz_tool.translate import translate_text_file
import asyncio

# Translate a Markdown file
asyncio.run(translate_text_file(
    input_file_path="input.md",
    output_file_path="output_fr.md",
    src_lang="en",
    dest_lang="fr"
))
```

**CLI Usage:**
```bash
python -m ronzz_tool.translate input.md output_fr.md --src_lang en --dest_lang fr
```

### Image to SVG Conversion

```python
from ronzz_tool.img2SVG import image_to_svg_inkscape

# Convert image to SVG (requires Inkscape)
image_to_svg_inkscape("input.png", "output.svg")
```

### PDF to PNG Conversion

```python
from ronzz_tool.pdf2png import extract_images_from_pdf

# Extract images from PDF
extract_images_from_pdf("input.pdf", "output_directory")
```

## Development

### Setting up Development Environment

```bash
# Clone the repository
git clone https://github.com/Ron-RONZZ-org/ronzz-py-tools.git
cd ronzz-py-tools

# Install in development mode
pip install -e .
```

### Running Tests

```bash
# Run tests (if available)
python -m pytest tests/
```

## License

This project is licensed under the GNU Affero General Public License v3.0 (AGPL-3.0).

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Author

**Ron Chou**
- Email: ron@ronzz.org
- Website: https://ronzz.org

## Acknowledgments

This package uses several open-source libraries including pdfplumber, markdownify, pydub, yt-dlp, and more.