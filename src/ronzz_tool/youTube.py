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
    cookies=None,
    cookies_from_browser=None,
    js_runtimes=None,
    username=None,
    password=None,
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
                # Build format string safely: don't use 'height<=best' which is invalid
                if str(preferred_video_quality).lower() == "best":
                    format_str = "bestvideo+bestaudio/best"
                else:
                    format_str = f"bestvideo[height<={preferred_video_quality}]+bestaudio/best/best"

                ydl_opts = {
                    "format": format_str,
                    "outtmpl": f"{output_path}/%(title)s.%(ext)s",
                }
            elif format == "both":
                # Same safe construction for 'both' (video+audio)
                if str(preferred_video_quality).lower() == "best":
                    format_str = "bestvideo+bestaudio/best"
                else:
                    format_str = f"bestvideo[height<={preferred_video_quality}]+bestaudio/best/best"

                ydl_opts = {
                    "format": format_str,
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

            # Support pour cookies / connexion (utile pour vidéos nécessitant authentification)
            # - `cookies`: chemin vers un fichier cookies (exporté depuis le navigateur)
            # - `cookies_from_browser`: nom du navigateur à fournir à yt-dlp, ex: 'chrome' ou 'firefox'
            # - `username` / `password`: identifiants YouTube (si nécessaire)
            if cookies:
                ydl_opts.update({"cookiefile": cookies})

            if cookies_from_browser:
                ydl_opts.update({"cookiesfrombrowser": cookies_from_browser})

            if username and password:
                ydl_opts.update({"username": username, "password": password})

            # Passer un runtime JS si demandé (ex: 'node') — mappe l'option CLI --js-runtimes
            if js_runtimes:
                # Ajout de deux clés possibles pour compatibilité
                ydl_opts.update(
                    {"js_runtimes": js_runtimes, "js-runtimes": js_runtimes}
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
    # Si une vidéo requiert une vérification d'âge ou une connexion, fournissez:
    # - `cookies_file`: chemin vers un fichier cookies exporté (recommended)
    # - `cookies_from_browser_option`: ex: 'chrome' ou 'firefox' (utilise le navigateur pour extraire les cookies)
    # - `username_option` / `password_option`: identifiants YouTube si nécessaire
    cookies_file = None  # Exemple: '/home/ron/Downloads/youtube-cookies.txt'
    # Par défaut, utiliser l'extraction depuis le navigateur 'firefox' et un runtime JS 'node'
    cookies_from_browser_option = "firefox"  # Exemple: 'chrome' or 'firefox'
    js_runtimes_option = "node"  # Exemple: 'node', 'deno', 'quickjs', 'bun'
    username_option = None
    password_option = None
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
                    cookies=cookies_file,
                    cookies_from_browser=cookies_from_browser_option,
                    username=username_option,
                    password=password_option,
                    js_runtimes=js_runtimes_option,
                )
            else:
                print(f"Aucune URL trouvée dans {csv_file}")
        else:
            print(f"Le fichier {csv_file} n'existe pas")
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier CSV: {e}")
