import misc
import telebot
from telebot import apihelper

token = misc.token
URL = 'https://api.telegram.org/bot' + token +'/'

ip = '195.201.137.246'
port = '1080'

apihelper.proxy = {
  'https': 'socks5://{}:{}'.format(ip, port)
}

apihelper.proxy = {'http':'http://x.x.x.x:port'}
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(m):
    msg = bot.send_message(m.chat.id, 'Привет!' )

bot.polling()
