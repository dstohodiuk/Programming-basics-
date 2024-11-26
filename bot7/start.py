import os
from telebot import TeleBot
from handlers import register_handlers

from dotenv import load_dotenv

load_dotenv()
API_TOKEN = os.getenv("TOKEN")
bot = TeleBot(API_TOKEN)


def main():
    register_handlers(bot)
    print("Бот розпочав свою роботу...")
    bot.infinity_polling()


if __name__ == "__main__":
    main()
