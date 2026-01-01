import requests
from bs4 import BeautifulSoup
import os
import time
import csv


def download_french_sentences_with_audio(
    output_dir="tatoeba_fr_audio", max_sentences=100
):
    base_url = "https://tatoeba.org"
    search_url = f"{base_url}/fr/audio/index/fra"
    os.makedirs(output_dir, exist_ok=True)
    session = requests.Session()
    downloaded = 0
    page = 1
    csv_path = os.path.join(output_dir, "sentences.csv")
    write_header = not os.path.exists(csv_path)

    # Charger les sentence_id déjà présents
    existing_ids = set()
    if os.path.exists(csv_path):
        with open(csv_path, "r", encoding="utf-8") as checkfile:
            reader = csv.DictReader(checkfile, delimiter=",")
            for row in reader:
                if row and "sentence_id" in row and row["sentence_id"]:
                    existing_ids.add(row["sentence_id"])

    with open(csv_path, "a", encoding="utf-8", newline="") as csvfile:
        writer = csv.writer(csvfile, delimiter=",")
        if write_header:
            writer.writerow(["sentence_id", "filename", "sentence"])
        while downloaded < max_sentences:
            print(f"Scraping page {page}...")
            resp = session.get(search_url + f"?page={page}")
            soup = BeautifulSoup(resp.text, "html.parser")
            sentences = soup.select("div.sentence.mainSentence")
            for s in sentences:
                if downloaded >= max_sentences:
                    break
                sentence_id = s.get("data-sentence-id")
                if sentence_id in existing_ids:
                    continue
                text_tag = s.select_one("div.text[lang='fr']")
                audio_tag = s.select_one("a.audioButton.audioAvailable")

                if text_tag and audio_tag:
                    sentence = text_tag.text.strip()
                    audio_url = audio_tag.get("href")
                    if not audio_url.startswith("http"):
                        audio_url = base_url + audio_url
                    safe_sentence = "".join(
                        c if c.isalnum() or c in (" ", "_") else "_"
                        for c in sentence[:20]
                    ).replace(" ", "_")
                    file_name = f"{safe_sentence}.mp3"
                    audio_filename = os.path.join(output_dir, file_name)
                    audio_resp = session.get(audio_url)
                    with open(audio_filename, "wb") as f:
                        f.write(audio_resp.content)
                    writer.writerow([sentence_id, file_name, sentence])
                    print(f"Downloaded: {audio_filename}")
                    downloaded += 1
                    time.sleep(0.5)  # pour éviter de surcharger le serveur
            page += 1
            time.sleep(1)
    print(f"Terminé. {downloaded} phrases téléchargées.")


if __name__ == "__main__":
    download_french_sentences_with_audio(
        output_dir="tatoeba_fr_audio", max_sentences=10000
    )
