import requests
from bs4 import BeautifulSoup
import smtplib
import json

def the_latest_news():
	"""Функция добывает последние новости с сайта www.lenta.ru и возвращает результат в виде НОВОСТЬ : ССЫЛКА"""
	url = 'https://lenta.ru/parts/news/'
	res = requests.get(url, verify = False)
	get_data = res.text
	with open('index.html', 'w', encoding = 'utf-8') as f:
		f.write(get_data)
	with open('index.html', 'r', encoding = 'utf-8') as fp:
		contents = fp.read()
	soup = BeautifulSoup(contents, 'lxml')
	print(soup.title.text)
	url_for_news = []
	for news in soup.find_all('h3'):
		for link in news.find_all('a'):
			url_for_news.append(f"lenta.ru{link.get('href')}")
	text_news = []
	for value in soup.find_all('h3'):
		text_news.append(value.get_text())

	news_with_url = dict(zip(text_news, url_for_news))
	for value, key in news_with_url.items():
		print(f'{value} /// ссылка на новость: {key}')


def weather(city='Arkhangelsk, RU'):
	"""weather in the city name"""

	city_name = city
	API_KEY = '4e5b5dde34d27aa16bd7f6ecb74a977c'
	url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&units=metric&appid={API_KEY}'

	res = requests.get(url)
	weather = f"\n-=== ПОГОДА В АРХАНГЕЛЬСКЕ===-\n{res.json()['weather'][0]['main']}, {res.json()['weather'][0]['description']}\nТемпература: {res.json()['main']['temp']}C,\nОщущается как: {res.json()['main']['feels_like']}C,\nМинимальная температура сегодня: {res.json()['main']['temp_min']}C,\nМаксимальная температура сегодня: {res.json()['main']['temp_max']}C,\nСкорость ветра: {res.json()['wind']['speed']} метров в секунду"
	return weather

weater_right_now = weather()

the_latest_news()
print(weater_right_now)