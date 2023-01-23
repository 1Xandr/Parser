import requests
from bs4 import BeautifulSoup
import time
from dish_info import get_data
from parser_ingredients import get_ingredient
from SQL import *


headers = {
    'User-Agent':
        'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.5) '
        'Gecko/20091102 Firefox/3.5.5 (.NET ClR 3.5.30729)'}


def get_info():
    """
    Parser get name, image and url of each dish
    Sometimes on site image has special div that add for image text "Спецпроект", so in 31 line I check
    and if image has special div then parser search other div
    :return: name_dish: str | img_dish: str | url_dish: str | cuisine_dish: str | categories_dish: str
    """
    for page in range(1, 715):  # how many page we need to parse | site have 714 pages
        site_url = f'https://eda.ru/recepty?page={page}'
        response = requests.get(url=site_url, headers=headers)
        beautiful_soup = BeautifulSoup(response.text, 'lxml')  # parsing html code
        data = beautiful_soup.find_all("div", class_="emotion-1f6ych6")  # get data from each dish

        for dish in data:  # how many dish we have | one page = 14 dishes
            try:
                time.sleep(1)  # make pause in parser work

                # Get info form dish about cuisine and categories
                cuisine_cat = dish.find_all("span", class_="emotion-ld5tpo")  # cuisine and categories in one class_
                categories_dish = cuisine_cat[0].text
                cuisine_dish = cuisine_cat[1].text if cuisine_cat[1] else None  # if no cuisine_dish -> None

                url_dish = "https://eda.ru" + dish.find("a").get("href")
                name_dish = dish.find("div", class_='emotion-1eugp2w').text.replace("'", "’")

                get_img = dish.find("div", class_='emotion-0')  # if image have "Спецпроект" -> None
                # if get_img == None -> class_='emotion-125jgdy'
                get_img = dish.find("div", class_='emotion-125jgdy') if not get_img else get_img
                img_dish = get_img.find("img").get("src")
                yield name_dish, img_dish, url_dish, categories_dish, cuisine_dish, page
            except Exception as exe:
                print("firs", page, exe)
                continue


id_sql = 1
for data_dish in get_info():
    try:
        # Get info from function "get_info"
        name = data_dish[0]
        image = data_dish[1]
        url = data_dish[2]
        categories = data_dish[3]
        cuisine = data_dish[4]

        # Get info of dish in dish_info.py
        dish_info = get_data(url)
        description, cook_time = dish_info[0], dish_info[6]
        instruction = dish_info[1]  # list -> [[text, number], [text, number]]
        calories, protein, fat, carbohydrate = dish_info[2], dish_info[3], dish_info[4], dish_info[5]

        # Get info of ingredient in parser_ingredients.py
        ingredient_info = get_ingredient(url)
        ingredient = ingredient_info[0]  # list: ['Говядина', '500', 'г']
        default_quant = ingredient_info[1]  # int

        # Get info of equipment for SQL
        equipment = dish_info[7]
        pan, saucepan, microwave, oven = equipment[0], equipment[1], equipment[2], equipment[3]
        blender, grill, mixer, slowCooker = equipment[4], equipment[5], equipment[6], equipment[7]
        meat_grinder, grater, steamer, mortar = equipment[8], equipment[9], equipment[10], equipment[11]
        seeder_for_flour, garlic_crusher = equipment[12], equipment[13]

        # filling into MySql database
        fill_list_of_dishes(id_sql, name, image, description, cook_time, categories, cuisine)
        fill_energy_value(id_sql, calories, protein, fat, carbohydrate)

        for step in instruction:
            fill_instruction(id_sql, step[1], step[0])  # id, [text, number]

        for ing in ingredient:
            fill_ingredients(id_sql, ing[0], ing[1], ing[2], default_quant)  # 1, ['Говядина', '500', 'г'], 6

        fill_equipment(id_sql, pan, saucepan, microwave, oven, blender, grill, mixer, slowCooker, meat_grinder,
                       grater, steamer, mortar, seeder_for_flour, garlic_crusher)

        id_sql += 1
    except Exception as ex:
        print("sec", data_dish[5], ex)
        continue
