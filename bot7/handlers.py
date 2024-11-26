from keyboards import keyboard_reply, categories_menu, back_to_categories
from parser import parse_category_recipes
from categories import categories


def register_handlers(bot):
    @bot.message_handler(commands=['start'])
    def start(message):
        keyboard1 = keyboard_reply()
        bot.send_message(
            message.chat.id, "Привіт! Вибери категорію страв, яка вас цікавить!", reply_markup=keyboard1)

    @bot.message_handler(func=lambda message: message.text in categories)
    def handle_category(message):
        category_name = message.text
        category_url = categories[category_name]

        dishes = parse_category_recipes(category_url)

        if dishes:
            dish_names = "\n".join(
                [f"{i+1}. {dish[0]}" for i, dish in enumerate(dishes)])
            bot.send_message(message.chat.id, f"Ось страви в категорії {category_name}:\n\n{
                             dish_names}", reply_markup=back_to_categories())
            bot.register_next_step_handler(
                message, handle_dish_selection, dishes)
        else:
            bot.send_message(message.chat.id, f"Не вдалося знайти страви для категорії {
                             category_name}. Спробуйте іншу категорію.")

    def handle_dish_selection(message, dishes):
        try:
            choice = int(message.text) - 1
            if 0 <= choice < len(dishes):
                dish_name, dish_link = dishes[choice]
                bot.send_message(message.chat.id, f"Ось рецепт страви {
                                 dish_name}:\n{dish_link}")
            else:
                bot.send_message(
                    message.chat.id, "Неправильний вибір. Спробуйте ще раз.")
                bot.register_next_step_handler(
                    message, handle_dish_selection, dishes)
        except ValueError:
            bot.send_message(
                message.chat.id, "Будь ласка, виберіть номер страви.")
            bot.register_next_step_handler(
                message, handle_dish_selection, dishes)

    @bot.message_handler(func=lambda message: message.text == "Категорії страв!")
    def show_categories(message):
        bot.send_message(
            message.chat.id, "Оберіть категорію страви:", reply_markup=categories_menu())

    @bot.message_handler(func=lambda message: message.text == 'Назад')
    def go_back(message):
        bot.send_message(
            message.chat.id, "Повертаємося до головного меню:", reply_markup=keyboard_reply())
