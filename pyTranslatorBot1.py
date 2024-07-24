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
