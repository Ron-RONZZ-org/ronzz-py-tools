import argparse
import pdfplumber
import re
import os

# from PIL import Image


def clean_repeated_characters(text):
    """
    Nettoie les répétitions excessives de caractères dans une chaîne.
    Exemple : "Hhhhhooooowwwww" devient "How".
    """
    return re.sub(r"(.)\1{2,}", r"\1", text)


def detect_title(line, length_threshold: int):
    if line.isupper() and len(line.split()) <= length_threshold:
        return f"\n# {line.title()}\n"
    return None


def detect_list(line):
    if re.match(r"^[-*+•\d]\s+", line):
        return f"- {line[2:].strip()}"
    return None


def detect_link(line):
    # Détecte les liens entourés de parenthèses ou les liens bruts
    return re.sub(
        r"\(?https?://[^\s)]+\)?",
        lambda match: f"[{match.group(0).strip('()')}]({match.group(0).strip('()')})",
        line,
    )


def convert_page_text_to_md(text, title_length_threshold=15):
    # Remplace les caractères PS (Paragraph Separator) par des sauts de ligne pour marquer les paragraphes
    text = text.replace("\u2029", "\n")

    # Remplace les caractères LS (Line Separator) par des espaces pour indiquer une continuation de ligne
    text = text.replace("\u2028", " ")

    md_lines = []
    paragraph = []  # Liste temporaire pour regrouper les lignes d'un paragraphe

    for line in text.split("\n"):
        line = line.strip()  # Supprime les espaces en début et en fin de ligne
        if not line:  # Si la ligne est vide, cela marque la fin d'un paragraphe
            if paragraph:
                # Joindre les lignes du paragraphe en une seule ligne
                joined_paragraph = " ".join(paragraph)
                joined_paragraph = clean_repeated_characters(
                    joined_paragraph
                )  # Nettoie les répétitions
                # Gérer les mots divisés sur deux lignes
                joined_paragraph = re.sub(r"(\w+)-\s+(\w+)", r"\1\2", joined_paragraph)
                md_lines.append(joined_paragraph)
                paragraph = []  # Réinitialise le paragraphe
            continue

        # Si la ligne n'est pas vide, ajoute-la au paragraphe temporaire
        paragraph.append(line)

    # Ajouter le dernier paragraphe s'il existe
    if paragraph:
        joined_paragraph = " ".join(paragraph)
        joined_paragraph = clean_repeated_characters(joined_paragraph)
        # Gérer les mots divisés sur deux lignes
        joined_paragraph = re.sub(r"(\w+)-\s+(\w+)", r"\1\2", joined_paragraph)
        md_lines.append(joined_paragraph)

    return "\n".join(md_lines)


def extract_tables(page):
    tables_md = []
    tables = page.extract_tables()
    for table in tables:
        if not table:
            continue
        md_table = ""
        headers = table[0]
        md_table += "| " + " | ".join(headers) + " |\n"
        md_table += "| " + " | ".join(["---"] * len(headers)) + " |\n"
        for row in table[1:]:
            md_table += "| " + " | ".join(cell or "" for cell in row) + " |\n"
        tables_md.append(md_table)
    return "\n\n".join(tables_md)


def extract_images(page, output_folder, page_number=0):
    os.makedirs(output_folder, exist_ok=True)
    for i, image in enumerate(page.images):
        bbox = (image["x0"], image["top"], image["x1"], image["bottom"])
        cropped = page.crop(bbox).to_image(resolution=150)
        img_path = os.path.join(output_folder, f"page{page_number+1}_img{i+1}.png")
        cropped.save(img_path, format="PNG")
        print(f"🖼️ Image extraite : {img_path}")
        return f"![image]({img_path})"


def convert_pdf_to_markdown(
    pdf_path, output_md_path, extract_imgs=False, img_folder="images"
):
    final_md = ""
    with pdfplumber.open(pdf_path) as pdf:
        for i, page in enumerate(pdf.pages):
            final_md += f"<!-- Page {i+1} -->\n"

            if extract_imgs:
                final_md += extract_images(page, img_folder, i)

            text = page.extract_text()
            if text:
                final_md += convert_page_text_to_md(text) + "\n"

            tables_md = extract_tables(page)
            if tables_md:
                final_md += tables_md + "\n\n"

    with open(output_md_path, "w", encoding="utf-8") as f:
        f.write(final_md)
    print(f"✅ Markdown généré : {output_md_path}")


def main():
    parser = argparse.ArgumentParser(
        description="Convert PDF to Markdown with optional image extraction."
    )
    parser.add_argument(
        "--input", "-i", required=True, help="Chemin vers le fichier PDF d'entrée."
    )
    parser.add_argument(
        "--output", "-o", required=True, help="Chemin vers fichier Markdown de sortie."
    )
    parser.add_argument(
        "--extract-images", action="store_true", help="Extraire les images du PDF."
    )
    parser.add_argument(
        "--img-folder",
        help="Dossier pour stocker les images extraites. Par défaut, le dossier de sortie du Markdown sera utilisé.",
    )
    args = parser.parse_args()
    # Si --img-folder n'est pas spécifié, utiliser le dossier de sortie de --output
    img_folder = args.img_folder if args.img_folder else os.path.dirname(args.output)
    convert_pdf_to_markdown(
        args.input,
        args.output,
        extract_imgs=args.extract_images,
        img_folder=args.img_folder,
    )


if __name__ == "__main__":
    main()
