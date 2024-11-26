from telebot.types import ReplyKeyboardMarkup, KeyboardButton


def keyboard_reply():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = KeyboardButton('Категорії страв!')
    keyboard.add(button1)
    return keyboard


def categories_menu():
    from categories import categories
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    for category in categories:
        keyboard.add(KeyboardButton(category))
    button6 = KeyboardButton('Назад')
    keyboard.add(button6)
    return keyboard


def back_to_categories():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(KeyboardButton("Категорії страв!"))
    return keyboard
