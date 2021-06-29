import requests
from bs4 import BeautifulSoup

def get_yandex_news(target):
	"""Функция принимает в качестве аргумента ссылку на яндекс новости, парсит страницу возвращает  словарь Текст новости /// ссылка на новость"""
	res = requests.get(target)
	soup = BeautifulSoup(res.text, 'lxml')
	print(soup.title.text)
	data = { 
		news.text : a.get('href') 
		for news in soup.find_all(attrs = {'class' : 'mg-card mg-card_single mg-card_type_image mg-grid__item mg-grid__item_type_card'})
		for a in news.find_all('a')
		} # генератор словаря 
	for k,v in data.items():
		print(f'///{k} /// {v}') # выводим получившийся словарь


target = input('Для того чтобы посмотреть новости на странице яндекса в формате "НОВОСТЬ /// ССЫЛКА НА НОВОСТЬ", введите ссылку на страницу, с которой необходимо спарсить новости:')
get_yandex_news(target)