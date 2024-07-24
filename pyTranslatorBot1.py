import telebot
from telebot import types

from googletrans import Translator
translator = Translator()
src = 'en'
dest = 'ru'

TOKEN='TOKEN'

bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands=["start"])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("translator")
    item2 = types.KeyboardButton("dictionary")
    item3 = types.KeyboardButton("translate1")
    markup.add(item1, item2)
    bot.send_message(
        message.chat.id,
        "Привет, {0.first_name}! Я тестовый бот. Выбери программу, которую ты хочешь выполнить".format(
            message.from_user
        ),
        reply_markup=markup,
    )
@bot.message_handler(content_types=["text"])
def bot_message(message):
    if message.chat.type == "private":
        if message.text == "translator":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("translate")
            back = types.KeyboardButton("back")
            markup.add(item1, back)
            bot.send_message(
                message.chat.id, "Что именно нужно сделать", reply_markup=markup
            )
        elif message.text == "dictionary":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("list")
            item2 = types.KeyboardButton("term")
            back = types.KeyboardButton("back")
            markup.add(item1, item2, back)
            bot.send_message(
                message.chat.id, "Что именно нужно сделать", reply_markup=markup
            )
        elif message.text == "translate":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            translated_text = translator.translate(message.text, src=src, dest=dest).text
            bot.send_message(
                message.chat.id, translated_text
            )
        elif message.text == "back":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("translator")
            item2 = types.KeyboardButton("dictionary")
            markup.add(item1, item2)
            bot.send_message(
                message.chat.id, "Вы вернулись на главное меню", reply_markup=markup
            )


#@bot.message_handler(func=lambda m: True)
#def translate_message(message):
#    # Берем полученное сообщение и переводим его
#    translated_text = translator.translate(message.text, src=src, dest=dest).text
#

    # Отправляем переведенное сообщение
#    bot.send_message(message.chat.id, translated_text)

bot.polling(none_stop=True)








Ошибка:
Traceback (most recent call last):
  File "/TelegramBotDictionary/pyTranslatorBot1.py", line 70, in <module>
    bot.polling(none_stop=True)
  File "/TelegramBotDictionary/tenv/lib/python3.10/site-packages/telebot/__init__.py", line 1178, in polling
    self.__threaded_polling(non_stop=non_stop, interval=interval, timeout=timeout, long_polling_timeout=long_polling_timeout,
  File "/TelegramBotDictionary/tenv/lib/python3.10/site-packages/telebot/__init__.py", line 1253, in __threaded_polling
    raise e
  File "/TelegramBotDictionary/tenv/lib/python3.10/site-packages/telebot/__init__.py", line 1215, in __threaded_polling
    self.worker_pool.raise_exceptions()
  File "/TelegramBotDictionary/tenv/lib/python3.10/site-packages/telebot/util.py", line 150, in raise_exceptions
    raise self.exception_info
  File "/TelegramBotDictionary/tenv/lib/python3.10/site-packages/telebot/util.py", line 93, in run
    task(*args, **kwargs)
  File "/TelegramBotDictionary/tenv/lib/python3.10/site-packages/telebot/__init__.py", line 8707, in _run_middlewares_and_handler       
    result = handler['function'](message)
  File "/TelegramBotDictionary/pyTranslatorBot1.py", line 57, in bot_message
    translated_text = translator.translate(message.text, src=src, dest=dest).text
  File "/TelegramBotDictionary/tenv/lib/python3.10/site-packages/googletrans/client.py", line 182, in translate
    data = self._translate(text, dest, src, kwargs)
  File "/TelegramBotDictionary/tenv/lib/python3.10/site-packages/googletrans/client.py", line 78, in _translate
    token = self.token_acquirer.do(text)
  File "/TelegramBotDictionary/tenv/lib/python3.10/site-packages/googletrans/gtoken.py", line 194, in do
    self._update()
  File "/TelegramBotDictionary/tenv/lib/python3.10/site-packages/googletrans/gtoken.py", line 62, in _update
    code = self.RE_TKK.search(r.text).group(1).replace('var ', '')
AttributeError: 'NoneType' object has no attribute 'group'
(tenv) dato@Windows-Asus:~/TelegramBotDictionary$ python pyTranslatorBot1.py
Traceback (most recent call last):
  File "/TelegramBotDictionary/pyTranslatorBot1.py", line 73, in <module>
    bot.polling(none_stop=True)
  File "/TelegramBotDictionary/tenv/lib/python3.10/site-packages/telebot/__init__.py", line 1178, in polling
    self.__threaded_polling(non_stop=non_stop, interval=interval, timeout=timeout, long_polling_timeout=long_polling_timeout,
  File "/TelegramBotDictionary/tenv/lib/python3.10/site-packages/telebot/__init__.py", line 1253, in __threaded_polling
    raise e
  File "/TelegramBotDictionary/tenv/lib/python3.10/site-packages/telebot/__init__.py", line 1215, in __threaded_polling
    self.worker_pool.raise_exceptions()
  File "/TelegramBotDictionary/tenv/lib/python3.10/site-packages/telebot/util.py", line 150, in raise_exceptions
    raise self.exception_info
  File "/TelegramBotDictionary/tenv/lib/python3.10/site-packages/telebot/util.py", line 93, in run
    task(*args, **kwargs)
  File "/TelegramBotDictionary/tenv/lib/python3.10/site-packages/telebot/__init__.py", line 8707, in _run_middlewares_and_handler       
    result = handler['function'](message)
  File "/TelegramBotDictionary/pyTranslatorBot1.py", line 50, in bot_message
    translated_text = translator.translate(message.text, src=src, dest=dest).text
  File "/TelegramBotDictionary/tenv/lib/python3.10/site-packages/googletrans/client.py", line 182, in translate
    data = self._translate(text, dest, src, kwargs)
  File "/TelegramBotDictionary/tenv/lib/python3.10/site-packages/googletrans/client.py", line 78, in _translate
    token = self.token_acquirer.do(text)
  File "/TelegramBotDictionary/tenv/lib/python3.10/site-packages/googletrans/gtoken.py", line 194, in do
    self._update()
  File "/TelegramBotDictionary/tenv/lib/python3.10/site-packages/googletrans/gtoken.py", line 62, in _update
    code = self.RE_TKK.search(r.text).group(1).replace('var ', '')
AttributeError: 'NoneType' object has no attribute 'group'
