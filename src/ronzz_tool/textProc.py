import re


class textProc:
    @staticmethod
    def __replace(match, replacements):
        return replacements[match.group(0)]

    @staticmethod
    def regex_sub(text: str, replacements: dict):
        """
        replacements = {r"bonjour": "hi", r"monde": "world", r"salut": "hey"}
        """
        pattern = re.compile("|".join(replacements.keys()))
        return pattern.sub(lambda match: textProc.__replace(match, replacements), text)

    @staticmethod
    def split_by_uppercase(text: str):
        """
        Splits a string by uppercase letters.
        Example: "HelloWorld" -> ["Hello", "World"]
        """
        return re.findall(r"[A-Z][^A-Z]*", text)

    @staticmethod
    def vtt_to_txt(path: str, txt_path: str = None):
        """
        Convertit un ou plusieurs fichiers .vtt en .txt sans time stamps ni séparations artificielles de lignes.
        - Si path est un fichier .vtt, convertit ce fichier.
        - Si path est un dossier, convertit tous les .vtt du dossier (et ignore les autres fichiers).
        Si txt_path n'est pas fourni, chaque .txt sera créé à côté du .vtt avec le même nom de base.
        Si plusieurs fichiers et txt_path est fourni, il doit s'agir d'un dossier de destination.
        Retourne la liste des chemins .txt créés.
        """
        import os

        txt_files = []
        if os.path.isdir(path):
            vtt_files = [
                os.path.join(path, f)
                for f in os.listdir(path)
                if f.lower().endswith(".vtt")
            ]
        else:
            vtt_files = [path]
        multi_files = len(vtt_files) > 1 or os.path.isdir(path)
        if multi_files and txt_path is not None and not os.path.isdir(txt_path):
            raise ValueError(
                "Si plusieurs fichiers, txt_path doit être un dossier existant ou à créer."
            )
        if multi_files and txt_path is not None and not os.path.exists(txt_path):
            os.makedirs(txt_path)
        for vtt_file in vtt_files:
            if txt_path is None:
                out_txt = vtt_file.rsplit(".", 1)[0] + ".txt"
            else:
                if multi_files:
                    # txt_path est un dossier de destination
                    base = os.path.splitext(os.path.basename(vtt_file))[0]
                    out_txt = os.path.join(txt_path, base + ".txt")
                else:
                    out_txt = txt_path
            lines = []
            with open(vtt_file, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if (
                        not line
                        or re.match(r"\d{2}:\d{2}:\d{2}\.\d{3} -->", line)
                        or line.isdigit()
                        or line == "WEBVTT"
                    ):
                        continue
                    lines.append(line)
            text = " ".join(lines)
            text = re.sub(r" +", " ", text)
            with open(out_txt, "w", encoding="utf-8") as f:
                f.write(text.strip())
            txt_files.append(out_txt)
        return txt_files
