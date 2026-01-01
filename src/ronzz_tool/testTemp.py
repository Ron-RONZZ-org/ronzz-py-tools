from googletrans import Translator
import asyncio

translator = Translator()
# print(Translator)
# print(asyncio.run(Translator.translate("안녕하세요.", dest="ja")))


async def translateBlock(
    block: list, translator: object, src_lang="auto", dest_lang="fr"
):
    joined_block: str = "\n".join(block)
    print("joined_block:", joined_block)
    translated_block_obj: object = await translator.translate(
        joined_block, src=src_lang, dest=dest_lang
    )
    return translated_block_obj.text


block = ["hello world", "how are you", "yes!"]
print(asyncio.run(translateBlock(block, translator, dest_lang="fr")))
