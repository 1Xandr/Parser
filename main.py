import requests
from bs4 import BeautifulSoup
from time import sleep

list_card_url = []
# site = https://scrapingclub.com/
headers = {
    'User-Agent':
        'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5 (.NET ClR 3.5.30729)'}


def get_url():
    for count in range(1, 8):
        url = f'https://scrapingclub.com/exercise/list_basic/?page={count}'

        response = requests.get(url, headers=headers)

        soup = BeautifulSoup(response.text, 'lxml')

        data = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')

        for x in data:
            card_url = 'https://scrapingclub.com' + x.find('a').get('href')
            yield card_url


def array():
    for i in get_url():
        response = requests.get(i, headers=headers)
        sleep(3)
        soup = BeautifulSoup(response.text, 'lxml')

        data = soup.find('div', class_='card mt-4 my-4')

        name = data.find('h3', class_='card-title').text.replace('\n', '')
        price = data.find('h4').text
        url_img = 'https://scrapingclub.com' + data.find('img', class_='card-img-top img-fluid').get('src')
        description = data.find('p', class_='card-text').text
        yield name, price, url_img, description
