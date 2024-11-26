import requests
from bs4 import BeautifulSoup as bs


def log_execution(func):
    def wrapper(*args, **kwargs):
        print(f"Викликається функція {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Функція {func.__name__} виконана")
        return result
    return wrapper


@log_execution
def parse_category_recipes(category_url):
    response = requests.get(category_url)
    soup = bs(response.text, 'html.parser')
    dishes = soup.find(
        'div', class_='col-sm-12 prl0 mih').find_all('a', class_='cooking-recipe__title')
    recipe_list = []

    for dish in dishes:
        recipe_list.append((dish.text.strip(), dish['href']))
    return recipe_list
