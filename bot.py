import telebot
import requests

bot = telebot.TeleBot('')

@bot.message_handler(content_types = ['text'])
def send_random_photo(message):
    if message.text == 'Хочу фотку котика':
        url_1 = 'http://thecatapi.com/api/images/get?format=src'
        res = requests.get(url=url_1)
        url_2 = res.url
        bot.send_photo(message.chat.id, url_2)
    else:
        bot.send_message(message.chat.id, 'Придурок, посмотри моё описание')
    
bot.polling(non_stop = True)
