from ebooklib import epub
from bs4 import BeautifulSoup
from markdownify import markdownify as md
import argparse

"""
Ce script transforme un fichier EPUB en Markdown.
Utilise la bibliothèque `ebooklib` pour lire l'EPUB et `markdownify` pour convertir le HTML en Markdown.
"""


def epub_to_markdown(epub_path, output_md_path):
    # Charger le fichier EPUB
    book = epub.read_epub(epub_path)
    markdown_content = ""

    # Parcourir les items du livre
    for item in book.get_items():
        if item.get_type() == epub.ITEM_DOCUMENT:
            # Convertir le contenu HTML en Markdown
            soup = BeautifulSoup(item.get_content(), "html.parser")
            markdown_content += md(soup.prettify()) + "\n\n"

    # Écrire le contenu Markdown dans un fichier
    with open(output_md_path, "w", encoding="utf-8") as md_file:
        md_file.write(markdown_content)


# Exemple d'utilisation
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert an EPUB file to Markdown.")
    parser.add_argument("epub_path", help="Path to the input EPUB file")
    parser.add_argument("output_md_path", help="Path to the output Markdown file")
    args = parser.parse_args()

    epub_to_markdown(args.epub_path, args.output_md_path)
    print(f"✅ Markdown généré : {args.output_md_path}")
