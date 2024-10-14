import telebot

bot = telebot.TeleBot(token='7576183778:AAG9iVxm_iUGfFas0-7ToSvhEjqRRhYugeo')


@bot.message_handler(content_types=['text'])
def repear_all_messages(messages):
    bot.send_message(messages.chat.id, messages.text)


if __name__ == '__main__':
    bot.infinity_polling()
