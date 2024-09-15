from translate import Translator
translator=Translator(from_lang="russian", to_lang="english")
translation=translator.translate("Вчера я забронировал у вас номер в отеле.")
print(translation)