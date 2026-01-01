import yt_dlp
import csv
import os


def download_youtube(
    youtube_url_list,
    output_path=".",
    format="audio",
    preferred_audio_quality="192",
    preferred_video_quality="best",
    subtitle=False,  # Ajout de l'option
):
    for url in youtube_url_list:
        try:
            ydl_opts = {}
            if format == "audio":
                ydl_opts = {
                    "format": "bestaudio/best",
                    "outtmpl": f"{output_path}/%(title)s.%(ext)s",
                    "postprocessors": [
                        {
                            "key": "FFmpegExtractAudio",
                            "preferredcodec": "mp3",
                            "preferredquality": preferred_audio_quality,
                        }
                    ],
                }
            elif format == "video":
                ydl_opts = {
                    "format": f"bestvideo[height<={preferred_video_quality}]+bestaudio/best/best",
                    "outtmpl": f"{output_path}/%(title)s.%(ext)s",
                }
            elif format == "both":
                ydl_opts = {
                    "format": f"bestvideo[height<={preferred_video_quality}]+bestaudio/best/best",
                    "outtmpl": f"{output_path}/%(title)s.%(ext)s",
                }
            elif format == "subtitle_only":
                ydl_opts = {
                    "skip_download": True,
                    "writesubtitles": True,
                    "writeautomaticsub": True,
                    "subtitleslangs": ["fr", "en"],  # à adapter selon besoin
                    "subtitlesformat": "best",
                    "outtmpl": f"{output_path}/%(title)s.%(ext)s",
                }
            else:
                raise ValueError(
                    "Le paramètre format doit être 'audio', 'video', 'both' ou 'subtitle_only'."
                )

            # Ajout des options pour les sous-titres si demandé (hors subtitle_only)
            if subtitle and format != "subtitle_only":
                ydl_opts.update(
                    {
                        "writesubtitles": True,
                        "writeautomaticsub": True,
                        "subtitleslangs": ["fr"],  # à adapter selon besoin
                        "subtitlesformat": "best",
                    }
                )

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                print(f"Téléchargement ({format}) depuis: {url}")
                ydl.download([url])
                print("Téléchargement terminé!")
        except Exception as e:
            print(f"Erreur lors du téléchargement de {url}: {e}")


if __name__ == "__main__":
    # Specifier le chemin de sortie, le csv contenant les liens youTube et les paramètres

    output_dir = "/home/ron/Musique/classiquesFrancaises"
    csv_file = "/media/ron/Ronzz_Core/nextCloudSync/mindiverse-life/YouTubeUrl.csv"
    format_option = "audio"
    audio_quality_option = "192"
    video_quality_option = "720"
    subtitle_option = False
    # Créer le répertoire de sortie s'il n'existe pas
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Répertoire de sortie créé: {output_dir}")

    # Charger les URLs depuis le fichier CSV
    youtube_urls = []

    try:
        if os.path.exists(csv_file):
            with open(csv_file, "r", encoding="utf-8") as file:
                csv_reader = csv.reader(file)
                # Lire la première ligne pour récupérer les en-têtes
                headers = next(csv_reader, None)
                print(f"En-têtes du fichier CSV: {headers}")
                if headers:
                    try:
                        url_index = next(
                            i
                            for i, header in enumerate(headers)
                            if header.strip().lower() == "url"
                        )
                    except StopIteration:
                        raise ValueError(
                            "Aucune colonne avec l'en-tête 'url' trouvée dans le fichier CSV."
                        )

                    for row in csv_reader:
                        if (
                            row and len(row) > url_index
                        ):  # Vérifier que la ligne a assez de colonnes
                            youtube_urls.append(
                                row[url_index].strip()
                            )  # Extraire l'URL depuis la colonne "url"

            if youtube_urls:
                print(f"Chargement de {len(youtube_urls)} URLs depuis {csv_file}")
                download_youtube(
                    youtube_urls,
                    output_dir,
                    format=format_option,
                    preferred_audio_quality=audio_quality_option,
                    preferred_video_quality=video_quality_option,
                    subtitle=subtitle_option,  # Activation du téléchargement des sous-titres
                )
            else:
                print(f"Aucune URL trouvée dans {csv_file}")
        else:
            print(f"Le fichier {csv_file} n'existe pas")
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier CSV: {e}")
