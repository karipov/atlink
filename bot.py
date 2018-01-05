import telebot
import config
import time

bot = telebot.TeleBot(token=config.token)

def findat(msg):
    for i in msg:
        if '@' in i:
            return i

def check_if_active(): # TODO: create a function that will determine if an instagram account exists
    pass

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, '(placeholder text)')

@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, 'ALPHA = FEATURES MAY NOT WORK')

@bot.message_handler(func=lambda msg: msg.text is not None and '@' in msg.text)
def at_converter(message):
    texts = message.text.split()
    at_text = findat(texts)
    if at_text == '@':
        pass
    else:
        bot.reply_to(message, "https://instagram.com/{}".format(at_text[1:]))

while True:
    try:
        bot.polling(none_stop=True)

    # ConnectionError and ReadTimeout because of possible timout of the requests library

    # TypeError for moviepy errors

    # maybe there are others, therefore Exception

    except Exception:
        time.sleep(15)
