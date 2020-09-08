from bs4 import BeautifulSoup
from requests import get


def get_food_price(text):
    return text[text.index("(") + 1: -1]


def get_food_name(text):
    if text[0] not in "01234":
        return text[text.index(":") + 2:]
    return text[text.index(")") + 1: text.index("(") - 1]


def get_menu(source_parser):
    html_data = source_parser.find("div", class_="jumbotron-fluid jumbotron bg-none pt-0").find("div", class_="row") \
        .find("div", class_="col-lg-12 today")
    if html_data is None:
        return None

    soup_string = html_data.find("p").get_text()
    if soup_string != "":
        soup_name = get_food_name(soup_string)
        print(soup_name)

    html_meals = html_data.find_all("li")
    for menu_index in range(3):
        meal_string = html_meals[menu_index].get_text()

        if meal_string != "":
            meal_name = get_food_name(meal_string)
            meal_price = get_food_price(meal_string)
            print(f"{meal_price}\t{meal_name}")
    return None


def scrape():
    url = "https://www.elementsrestaurant.sk/denne-menu/en/"
    html_source_code = get(url).text
    html_source_parser = BeautifulSoup(html_source_code, "html.parser")
    get_menu(html_source_parser)
    return None


scrape()
