import subprocess
import argparse


def image_to_svg_inkscape(image_path, svg_path):
    # Utiliser Inkscape pour convertir une image (PNG, JPG, etc.) en SVG
    subprocess.run(["inkscape", image_path, "--export-type=svg", "-o", svg_path])
    print(f"SVG créé avec Inkscape : {svg_path}")


if __name__ == "__main__":

    # Création d'un parser pour les arguments de la ligne de commande
    parser = argparse.ArgumentParser(
        description="Convertir un fichier PNG en SVG en utilisant Inkscape."
    )
    parser.add_argument("png_path", help="Chemin vers le fichier PNG d'entrée.")
    parser.add_argument("svg_path", help="Chemin vers le fichier SVG de sortie.")
    args = parser.parse_args()

    # Appel de la fonction pour effectuer la conversion
    print(f"Conversion du fichier PNG '{args.png_path}' en SVG '{args.svg_path}'...")
    image_to_svg_inkscape(args.png_path, args.svg_path)
    print("Conversion terminée avec succès.")
