from googletrans import Translator
from langdetect import detect
translator = Translator()
cmd3 = input("Введите текст, который вы хотите перевести: ")
translation = translator.translate(cmd3, src=detect(cmd3), dest='en').text
print(translation.encode('utf-8', 'replace').decode())
