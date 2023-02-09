import requests
from bs4 import BeautifulSoup
import json
from time import sleep
import random
import datetime


from url_info import url_short


with open('file_path.txt') as file:
    # данные из файла сохраняем в список, предварительно обработав их методом strip
    # для удаления случайных начальных и конечных пробелов.
    lines = [line.strip() for line in file.readlines()]
    lines_count = len(lines)
    # список для всех данных
    data_dict = []
    # счетчик для отображения во время работы
    # на каждой итерации будет увеличен на 1 и выведен на экран.
    count = 0

    headers = {
        "accept": "*/*",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
    }

    for line in lines:
        url = line
        # пауза между итерациями
        sleep(random.randrange(2, 4))
        # используем headers, признаки accept и user-agent
        q = requests.get(url=url, headers=headers)
        result = q.content
        # создаем объект soup, используем библиотеку 'lxml'
        soup = BeautifulSoup(result, 'lxml')

        # получаем данные из soup
        # -enter-your-data-

        person_name = soup.find(class_='-enter-your-data-').find(class_='-enter-your-data-').text
        person_name = person_name.strip()

        person_surname = soup.find(class_='-enter-your-data-').find(class_='-enter-your-data-').text
        person_surname = person_surname.strip()

        person_name_ful = soup.find(class_='-enter-your-data-').find(class_='-enter-your-data-').find('h1').text
        person_name_ful = ' '.join(person_name_ful.split())

        job = soup.find(class_='-enter-your-data-').find(class_='-enter-your-data-').text
        job = job.strip()

        short_info = str(soup.find(class_='-enter-your-data-').find(class_='-enter-your-data-').find('p'))
        short_info = short_info.replace('<p>','')
        short_info = short_info.replace('</p>', '')
        short_info = short_info.strip()

        # дата записи данных
        info_date = datetime.datetime.today().strftime("%Y-%m-%d")

        # link_b
        for tag in soup.find(class_='-enter-your-data-').find_all('a'):
            if '-enter-your-data-' in tag.get('href'):
                link_b = url_short + tag.get('href')
                break

        link_photo = soup.find(class_='-enter-your-data-').find('img')
        img_link = link_photo.get('src')
        link_photo = url_short + '/' + img_link

        link_page = url

        link_m = 'no'

        # данные о группах
        groups = []
        groups_names = []
        for tag in soup.find(class_='-enter-your-data-').findAll(class_='-enter-your-data-'):
            group_name = tag.get('title').strip()

            if group_name not in groups_names:
                group_link_short = tag.get('href')
                group_link = url_short + group_link_short
                group_logo_link = 'no'

                group = {}
                group.update(group_name=group_name,
                             group_link=group_link,
                             group_logo_link=group_logo_link)

                groups.append(group)
                groups_names.append(group_name)

        # собираем полученные данные в словарь
        data = {
            'person_surname': person_surname,
            'person_name': person_name,
            'person_name_ful': person_name_ful,
            'job': job,
            'short_info': short_info,
            'info_date': info_date,
            'link_b': link_b,
            'link_photo': link_photo,
            'link_page': link_page,
            'link_m': link_m,
            'groups': groups,
        }

        # каждый словарь добавим в общий список всех данных
        data_dict.append(data)

        # сохраним в файл json (предварительно импортировав json)
        # используем функцию dump у объекта json для сохранения данных.
        # в режиме w перезапишет результирующий файл при повторном запуске скрипта.
        with open('data.json', 'w', encoding='utf-8') as json_file:
            json.dump(data_dict, json_file, ensure_ascii=False, indent=4)

        count += 1
        print(f'{count} out of {lines_count} lines are ready!')