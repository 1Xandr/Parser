import requests
from bs4 import BeautifulSoup
import time


def get_each_url():
    site_url = f'https://eda.ru/wiki/ingredienty'
    gen_response = requests.get(site_url)
    soup = BeautifulSoup(gen_response.text, 'lxml')  # parsing html code
    data = soup.find_all("div", class_="emotion-1gwkmfw")

    for categories in data:
        url_categories = "https://eda.ru/wiki/" + categories.find("a").get("href")
        yield url_categories


for url in get_each_url():
    page = 1
    while True:  # for all page in categories
        time.sleep(3)  # pause code to not break site
        page += 1  # ?page=1 -> ?page=2
        response = requests.get(url + f"?page={page}")
        beautiful_soup = BeautifulSoup(response.text, 'lxml')  # parsing html code
        # which_categories = url.split("/")[-1]  # https://eda.ru/wiki/ingredienty/alkogol -> alkogol
        name = beautiful_soup.find_all("h2", class_="emotion-ogw7y8")
        image = beautiful_soup.find_all("img", alt="Изображение материала")
        if not name:
            break
        for count in range(len(name)):
            # image_url = image[count].get('src')
            # fill_all_ingredients(f'"{name[count].text}"')
            pass

