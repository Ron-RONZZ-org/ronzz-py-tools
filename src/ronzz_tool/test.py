import pdf2md
import translate
import asyncio
import pdf2png


def pdf2mdTest():
    testPDF_path = "../../tests/testInput/testPDF1.pdf"
    outputMD_path = "../../tests/testOutput/testMD1.md"
    pdf2md.convert_pdf_to_markdown(testPDF_path, outputMD_path)


def SVGTest():
    import img2SVG

    testPNG_path = "../../tests/testInput/testPNG1.png"
    outputSVG_path = "../../tests/testOutput/testSVG.svg"
    img2SVG.image_to_svg_inkscape(testPNG_path, outputSVG_path)


def translateTest():
    testMD_path = "../../tests/testOutput/testMD1.md"
    outputMD_path = "../../tests/testOutput/testMD1_fr.md"
    asyncio.run(
        translate.translate_text_file(
            testMD_path, outputMD_path, src_lang="en", dest_lang="fr"
        )
    )


def pdf_2_img_test():
    testPDF_path = "/media/ron/Ronzz_Core/nextCloudSync/lib/leMondeEnLesCartes/assets/images/OpenScan 20250419 131235734737 11.pdf"
    output_dir = (
        "/media/ron/Ronzz_Core/nextCloudSync/lib/leMondeEnLesCartes/assets/images"
    )
    pdf2png.extract_images_from_pdf(testPDF_path, output_dir)


class text_proc_test:
    @staticmethod
    def regexSubTest():
        import textProc

        replacements = {r"bonjour": "hi", r"monde": "world", r"salut": "hey"}
        output_text = textProc.textProc.regex_sub(
            "salut! bonjour tout le monde", replacements
        )
        print("expected: hey! hi tout le world", "\nactual:", output_text)

    @staticmethod
    def textSeparationTest(output_file_path="scrap.txt"):
        import textProc

        textOriginal = "PerceuseLe tuyauIl est apteÉclaireurUn suiveurUn hélicoptèreScandaleuxEnterrementSurpriseInhumationSépultureMon neveuma nièceRéarrangerExciterce n'est pas très clair d'après l'apparencenous avons une toute petite cave à vin iciSobreUn drap de litDéçuBanane mûreBannièreRoséeLes récessionsMoustiquesUn clips'agit-il d'une statue ?Une fourmiPlus vous restez debout, plus vous donnez aux masquitos le temps de se rassembler autour de vous.J'ai essayé de freiner mais j'allais trop viteJe conduis la motoPrétenduPétrifiéTerrifiéMoustiqueFlotteurLéthargiqueÉcorceContournerRequinsLe tour du mondeRelier àBaleineTon eauIrriguerGrenouilleUn maraisLézardPeau épaisseVignoblePigeonSerpentGorgeLeurs sabots vous piétinentDégusterLes saveursnanteuil saacyChausséeSavourer"
        return textProc.textProc.split_by_uppercase(textOriginal)
        # with open("temp.txt", "w") as temp_file:
        #     result = text_proc_test.textSeparationTest()
        #     for item in result:
        #         temp_file.write(item + "\n")

    @staticmethod
    def vtt_to_txt_test():
        import textProc

        vtt_path = "/home/ron/Vidéos/l'histoire/Transcripts/Conversion"
        txt_path = "/home/ron/Vidéos/l'histoire/Transcripts/Conversion"
        print(textProc.textProc.vtt_to_txt(vtt_path, txt_path))


class audio_test:
    @staticmethod
    def audio_trim_bulk_test():
        import audio

        # Exemple d'utilisation de trim_audio_bulk()
        input_audio_path = "example_audio.mp3"
        output_directory = "output_clips"
        time_ranges = [("0:00", "0:30"), ("0:30", "1:00"), ("1:00", "1:30")]
        clip_names = ["intro", "middle", "outro"]

        # Appeler la fonction pour découper l'audio
        audio.trim_audio_bulk(
            input_audio_path, time_ranges, output_directory, clip_names
        )

    @staticmethod
    def audio_convert_test():
        import audio

        # Exemple d'utilisation de la fonction audio_convert_bulk
        input_dir = "/media/ron/Ronzz_Core/nextCloudSync/mindiverse-life/coucou/coucou/assets/audio_effects/original"
        output_directory = "/media/ron/Ronzz_Core/nextCloudSync/mindiverse-life/coucou/coucou/assets/audio_effects/"
        audio.audio_convert_bulk(input_dir, output_directory)


if __name__ == "__main__":
    # pdf2mdTest()
    # SVGTest()
    # translateTest()
    # text_proc_test.regexSubTest()
    # pdf_2_img_test()
    # textSeparationTest()
    # audio_test.audio_convert_test()
    text_proc_test.vtt_to_txt_test()
