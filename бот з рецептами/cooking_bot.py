import telebot
import requests
from bs4 import BeautifulSoup as bs

url = 'https://www.unian.ua/recipes'

bot = telebot.TeleBot('TOKEN')

categories = {
    'Святкові меню': 'https://www.unian.ua/recipes/holiday-menus',
    'Перші страви': 'https://www.unian.ua/recipes/first-courses',
    'Другі страви': 'https://www.unian.ua/recipes/second-courses',
    'Салати': 'https://www.unian.ua/recipes/salads',
    'Десерти': 'https://www.unian.ua/recipes/desserts',
    }

def parse_category_recipes(category_url):
    response = requests.get(category_url)
    soup = bs(response.text, 'html.parser')
    dishes = soup.find('div', class_='col-sm-12 prl0 mih').find_all('a', class_='cooking-recipe__title')
    recipe_list = []

    for dish in dishes:
       recipe_list.append((dish.text.strip(), dish['href']))
    return recipe_list

@bot.message_handler(commands=['start'])
def start(message):
    keyboard1 = keyboard_reply()
    bot.send_message(message.chat.id, "Привіт! Вибери категорію страв, яка вас цікавить!", reply_markup=keyboard1)


def keyboard_reply():
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = telebot.types.KeyboardButton('Категорії страв!')
    keyboard.add(button1)
    return keyboard

def categories_menu():
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    for category in categories:
        keyboard.add(telebot.types.KeyboardButton(category))
    button6 = telebot.types.KeyboardButton('Назад')
    keyboard.add(button6)
    return keyboard

@bot.message_handler(func=lambda message: message.text in categories)
def handle_category(message):
    category_name = message.text
    category_url = categories[category_name]
    
    dishes = parse_category_recipes(category_url)
    
    if dishes:
        dish_names = "\n".join([f"{i+1}. {dish[0]}" for i, dish in enumerate(dishes)])
        bot.send_message(message.chat.id, f"Ось страви в категорії {category_name}:\n\n{dish_names}", reply_markup=back_to_categories())
        bot.register_next_step_handler(message, handle_dish_selection, dishes)
    else:
        bot.send_message(message.chat.id, f"Не вдалося знайти страви для категорії {category_name}. Спробуйте іншу категорію.")

def back_to_categories():
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(telebot.types.KeyboardButton("Категорії страв!"))
    return keyboard

def handle_dish_selection(message, dishes):
    try:
        choice = int(message.text) - 1
        if 0 <= choice < len(dishes):
            dish_name, dish_link = dishes[choice]
            bot.send_message(message.chat.id, f"Ось рецепт страви {dish_name}:\n{dish_link}")
        else:
            bot.send_message(message.chat.id, "Неправильний вибір. Спробуйте ще раз.")
            bot.register_next_step_handler(message, handle_dish_selection, dishes)
    except ValueError:
        bot.send_message(message.chat.id, "Будь ласка, виберіть номер страви.")
        bot.register_next_step_handler(message, handle_dish_selection, dishes)

@bot.message_handler(func=lambda message: message.text == "Категорії страв!")
def show_categories(message):
    bot.send_message(message.chat.id, "Оберіть категорію страви:", reply_markup=categories_menu())

@bot.message_handler(func=lambda message: message.text == 'Назад')
def go_back(message):
    bot.send_message(message.chat.id, "Повертаємося до головного меню:", reply_markup=keyboard_reply())

bot.infinity_polling() 
