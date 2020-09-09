from bs4 import BeautifulSoup


def get_food_price(text):
    return text[text.index("(") + 1: -1]


def get_food_name(text):
    if text[0] not in "123":
        return text[text.index(" ") + 1:]
    return text[text.index(" ") + 1: text.index("(") - 1]


def get_menu(source_parser):
    html_data = source_parser.find("div", class_="col-lg-12 today")
    if html_data is None:
        return None

    soup_string = html_data.find("p").get_text()
    if soup_string != "":
        soup_name = get_food_name(soup_string)
        print(soup_name)

    html_meals = html_data.find_all("li")
    for html_meal in html_meals:
        meal_string = html_meal.get_text()

        if meal_string != "":
            meal_name = get_food_name(meal_string)
            meal_price = get_food_price(meal_string)
            print(f"{meal_price}\t{meal_name}")
    return None


with open("restaurant.html") as file:
    html_source_code = file.read()
    html_source_parser = BeautifulSoup(html_source_code, "lxml")
    get_menu(html_source_parser)
