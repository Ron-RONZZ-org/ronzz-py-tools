from pydub import AudioSegment
import os


def trim_audio_bulk(
    input_path: str, time_ranges: list, output_dir: str, clip_names: list = None
):
    """
    Coupe un fichier audio en plusieurs clips selon les plages de temps spécifiées.

    :param input_path: Chemin du fichier audio d'entrée.
    :param time_ranges: Liste de tuples (start_time, end_time) en format (min:sec).
    :param output_dir: Répertoire pour sauvegarder les clips audio.
    :param clip_names: Liste des noms pour chaque clip (optionnel).
    """
    # Charger le fichier audio
    audio = AudioSegment.from_file(input_path)

    for i, (start_time_str, end_time_str) in enumerate(time_ranges):
        # Convertir les temps en millisecondes
        start_time = time_to_milliseconds(time_str=start_time_str)
        end_time = time_to_milliseconds(time_str=end_time_str)

        # Vérifier que les temps sont valides
        if start_time >= end_time:
            print(
                f"Erreur : le temps de début doit être inférieur au temps de fin pour le clip {i + 1}."
            )
            continue

        # Couper l'audio
        audio_clip = audio[start_time:end_time]

        # Créer le répertoire de sortie s'il n'existe pas
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # Générer le chemin de sortie pour le clip
        clip_name = (
            clip_names[i] if clip_names and i < len(clip_names) else f"clip_{i + 1}"
        )
        output_path = f"{output_dir}/{clip_name}.mp3"

        # Exporter le clip audio
        audio_clip.export(output_path, format="mp3")
        print(f"Clip {i + 1} sauvegardé dans {output_path}")


def time_to_milliseconds(time_str):
    minutes, seconds = map(int, time_str.split(":"))
    return (minutes * 60 + seconds) * 1000


def audio_convert(input_path: str, output_path: str):
    """
    Convertit un fichier audio en format ogg.

    :param input_path: Chemin du fichier audio d'entrée.
    :param output_path: Chemin du fichier audio de sortie (doit se terminer par .ogg).
    """
    # Vérifier que le fichier de sortie a l'extension .ogg
    if not output_path.lower().endswith(".ogg"):
        raise ValueError("Le fichier de sortie doit avoir l'extension .ogg")

    # Charger le fichier audio
    audio = AudioSegment.from_file(input_path)

    # Exporter le fichier audio en format ogg
    audio.export(output_path, format="ogg")
    print(f"Fichier converti sauvegardé dans {output_path}")


def audio_convert_bulk(input_dir: str, output_dir: str):
    """
    Convertit tous les fichiers audio d'un répertoire en format ogg et les exporte dans un répertoire spécifié.

    :param input_dir: Chemin du répertoire contenant les fichiers audio d'entrée.
    :param output_dir: Répertoire pour sauvegarder les fichiers convertis.
    """
    # Vérifier que le répertoire d'entrée existe
    if not os.path.exists(input_dir):
        raise ValueError(f"Le répertoire d'entrée {input_dir} n'existe pas.")

    # Créer le répertoire de sortie s'il n'existe pas
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Parcourir tous les fichiers dans le répertoire d'entrée
    for file_name in os.listdir(input_dir):
        input_path = os.path.join(input_dir, file_name)

        # Vérifier que c'est un fichier
        if os.path.isfile(input_path):
            # Générer le nom de fichier de sortie
            base_name = os.path.splitext(file_name)[0]
            output_path = os.path.join(output_dir, f"{base_name}.ogg")

            # Convertir et exporter le fichier audio
            try:
                audio_convert(input_path, output_path)
            except Exception as e:
                print(f"Erreur lors de la conversion de {input_path}: {e}")
