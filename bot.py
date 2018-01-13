import time
import telebot
import requests
from bs4 import BeautifulSoup
import config # file with the key


bot = telebot.TeleBot(token=config.token)

def findat(msg):
    # from a list of texts, it finds the one with the '@' sign
    for i in msg:
        if '@' in i:
            return i

def check_if_active(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    if 'Page Not Found' in soup.title.text:
        # soup.title.text gives the text of the <title> tag
        return False
    else:
        return True

@bot.message_handler(commands=['start']) # welcome message handler
def send_welcome(message):
    bot.reply_to(message, '(placeholder text)')

@bot.message_handler(commands=['help']) # help message handler
def send_welcome(message):
    bot.reply_to(message, 'ALPHA = FEATURES MAY NOT WORK')

@bot.message_handler(func=lambda msg: msg.text is not None and '@' in msg.text)
# lambda function finds messages with the '@' sign in them
# in case msg.text doesn't exist, the handler doesn't process it
def at_converter(message):
    texts = message.text.split()
    at_text = findat(texts)
    if at_text == '@': # in case it's just the '@', skip
        pass
    else:
        insta_link = "https://instagram.com/{}".format(at_text[1:])
        if check_if_active(insta_link) == True:
            # the funcion should return True if the account on the link exists
            bot.reply_to(message, insta_link)
        else:
            pass

while True:
    try:
        bot.polling(none_stop=True)
        # ConnectionError and ReadTimeout because of possible timout of the requests library
        # maybe there are others, therefore Exception
    except Exception:
        time.sleep(15)
