from bs4 import BeautifulSoup
import requests
import lxml
import re
import random
import time
import json
import os

url = 'https://13.lordfilm-dc.com/filmy/'


# Получаем путь к директории текущего скрипта
script_dir = os.path.dirname(os.path.abspath(__file__))


# Переходим на уровень выше
parent_dir = os.path.dirname(script_dir)


# Получаем путь к JSON
path_to_json = os.path.join(script_dir, 'films.json')


def dict_list_to_json(dict_list, filename):
    """
    Преобразует список словарей в JSON-строку и сохраняет её в файл.

    :param dict_list: Список словарей
    :param filename: Имя файла для сохранения JSON-строки
    :return: JSON-строка или None в случае ошибки
    """
    try:
        json_str = json.dumps(dict_list, ensure_ascii=False)
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(json_str)
        return json_str
    except (TypeError, ValueError, IOError) as e:
        print(f"Ошибка при преобразовании списка словарей в JSON или записи в файл: {e}")
        return None


def json_to_dict_list(filename):
    """
    Преобразует JSON-строку из файла в список словарей.

    :param filename: Имя файла с JSON-строкой
    :return: Список словарей или None в случае ошибки
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            json_str = file.read()
            dict_list = json.loads(json_str)
        return dict_list
    except (TypeError, ValueError, IOError) as e:
        print(f"Ошибка при чтении JSON из файла или преобразовании в список словарей: {e}")
        return None


def pars(url, start_page, stop_page):
    stop_page += 1
    print(f'старт')
    new_list = []
    count_dict = 0

    for i in range(start_page, stop_page):
        try:
            response = requests.get(f'{url}page/{i}')

        except:
            print('Disconect..')
            count_dict += 1
            dict = {}
            dict['ID'] = count_dict
            dict['page'] = i
            dict['status'] = None
            new_list.append(dict)

        else:
            soup = BeautifulSoup(response.text, 'lxml')
            find = soup.find_all('div', class_="th-item")
            print(f'спарсили {i}')

            for item in find:
                count_dict += 1
                dict = {}
                dict['ID'] = count_dict
                dict['page'] = i
                dict['year'] = item.find('div', class_="th-year").text
                dict['title'] = item.find('div', class_="th-title").text
                dict['link'] = item.find('a', class_="th-in with-mask").get('href')
                dict['img'] = 'https://13.lordfilm-dc.com/'+item.find('img').get('src')
                new_list.append(dict)
            seconds = random.randint(1, 100) / random.randint(50, 100)
            time.sleep(seconds)
            print(f'спали {seconds}')
    return new_list



#dict_list_to_json(pars(url, 1, 240), path_to_json)