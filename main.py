from urllib import response
import requests
from bs4 import BeautifulSoup
import sqlite3
from url_list import list
from fake_useragent import UserAgent

ua = UserAgent()
print(ua.random)


# Создаем базу

db = sqlite3.connect('faience_parser.db')

cursor = db.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS urls (
    product_url text
)""")

db.commit()

baseURL = 'https://www.santehnika-room.ru'

# Начинаем итерировать наши урлы и выполнять основную логику

soup = BeautifulSoup(response.text, 'lxml')
cards = soup.find('a', class_='catalog-body__prod-card_img').a['href']

for card in cards:
    # product_url = card.find(a['href'])
    # product_url = card
    # print(product_url)
    product_url = baseURL + card.find('div', class_='ci-title').a['href']
    product_price = card.find('div', class_='ci-price').text.replace(' ₽', '')
    cursor.execute(f"INSERT INTO urls VALUES (?)", (product_url))
    db.commit()

i = i+1
print(i)
    

print('Вроде как всё.')
db.close()