from googletrans import Translator
import argparse


def restore_syntax(text: str):
    """
    Corrige les erreurs courantes de traduction de .md
    - Des commentaires Markdown <!-- -->
    """
    replacements = {
        r"\n<!\s-": "\n<!--",
        r"\s->": "-->",
    }  # remplacer tout les mistraduction systèmatique
    return textProc.textProc.regex_sub(text, replacements)


async def translate_block(block: list, translator: object, src_lang, dest_lang):
    joined_block: str = "\n".join(block)
    translated_block_obj: object = await translator.translate(
        joined_block, src=src_lang, dest=dest_lang
    )
    return restore_syntax(translated_block_obj.text)


async def translate_text_file(
    input_file_path: str, output_file_path: str, src_lang="auto", dest_lang="fr"
):
    """
    Traduit le contenu d'un fichier Markdown par blocs pour respecter les limites de l'API.
    """
    translator = Translator()

    # Lecture du fichier d'entrée
    with open(input_file_path, "r", encoding="utf-8") as infile:
        lines = infile.readlines()

    translated_file_lines = []
    block = []  # Liste temporaire pour regrouper les lignes en blocs
    current_block_size = 0  # Taille actuelle du bloc en caractères

    for line in lines:
        if line.strip():  # Si la ligne n'est pas vide
            # Si ajouter cette ligne dépasse la limite, traduire le bloc actuel
            if current_block_size > 4000:
                translated_file_lines.append(
                    await translate_block(block, translator, src_lang, dest_lang)
                )
                block = []  # Réinitialiser le bloc
                current_block_size = 0
            block.append(line.strip())
            current_block_size += len(line)
    # Traduire le dernier bloc s'il existe
    if block:
        translated_file_lines.append(
            await translate_block(block, translator, src_lang, dest_lang)
        )

    # Écriture du fichier de sortie
    with open(output_file_path, "w", encoding="utf-8") as outfile:
        outfile.writelines(translated_file_lines)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Traduire un fichier Markdown dans une langue spécifiée."
    )
    parser.add_argument(
        "input_file_path", help="Chemin vers le fichier Markdown d'entrée."
    )
    parser.add_argument(
        "output_file_path", help="Chemin vers le fichier Markdown traduit en sortie."
    )
    parser.add_argument(
        "--src_lang",
        default="auto",
        help="Langue source (par défaut : détection automatique).",
    )
    parser.add_argument(
        "--dest_lang", default="fr", help="Langue cible (par défaut : français)."
    )

    args = parser.parse_args()

    translate_text_file(
        args.input_file_path,
        args.output_file_path,
        src_lang=args.src_lang,
        dest_lang=args.dest_lang,
    )
