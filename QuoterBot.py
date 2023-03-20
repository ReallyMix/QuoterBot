import telebot, requests
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

URL = "http://api.forismatic.com/api/1.0/"


def get_quote():

    payload = {'method': 'getQuote', 'format': 'json', 'lang': 'ru'}
    response = requests.get(URL, params=payload)

    data = response.json()

    return data["quoteText"] + "\n" + "\n" +data["quoteAuthor"] + data["senderName"]


TOKEN = "5993789607:AAGm4z_ryeLiRJ9DxleMtBYedRPZM0lIjDc"
bot = telebot.TeleBot(TOKEN)

keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(KeyboardButton("Получить цитату"))

@bot.message_handler(commands=['start'])
def send_welcome(message):

    bot.send_message(message.chat.id, "Добрый день, я Квотер - бот, позволяющий узнать изречения гениальных учёных, великих философов, а также авторов произведений, изменивших мышление поколений! \n \nЧтобы узнать одно из них нажмите на кнопку ниже ↓", reply_markup=keyboard)


@bot.message_handler(commands=['help'])
def send_help(message):
    bot.send_message(message.chat.id, 'Напишите "Получить цитату" или просто нажмите на кнопку ниже ↓', reply_markup=keyboard)


@bot.message_handler(func=lambda x: "Получить цитату" in x.text)
def send_quote(message):

    bot.send_message(message.chat.id, get_quote())

bot.infinity_polling()