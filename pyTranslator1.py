from translate import Translator
ru_letters = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
en_letters = "abcdefghijklmnopqrstuvwxyz"
cmd3 = input("Введите текст, который вы хотите перевести: ")
if cmd3[0].lower() in ru_letters:
    translator = Translator(from_lang="russian", to_lang="english")
elif cmd3[0].lower() in en_letters:
    translator = Translator(from_lang="english", to_lang="russian")
else:
    print('Я тебя не понимаю')
translation = translator.translate(cmd3)
print(translation)