import telebot
import config

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(content_types=['text'])
def lalala(message):
    # bot.send_message(message.chat.id, message.text)
    bot.send_message(message.chat.id, 'Test1')

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, 'adasdsadasd')

def start_bot():
    bot.polling(none_stop=True)

# bot.polling(none_stop=True)

