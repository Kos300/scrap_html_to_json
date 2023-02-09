# scrap_html_to_json

## Возможности
<ul>
<li>сбор всех ссылок url на страницах каталога сайта с постраничным выводом (пагинацией)</li>
<li>выбор уникальных ссылок, с учетом старого списка ссылок если он есть, фильтр ссыылок по вхождению в url заданной подстроки</li>
<li>сбор требуемых данных со страниц сайта и запись их в json файл с заданной структурой:</li>
</ul>
<p></p>
<p></p>
<pre>[<br />    {<br />        "person_surname": "-",<br />        "person_name": "-",<br />        "person_name_ful": "-",<br />        "job": "-",<br />        "short_info": "-",<br />        "info_date": "2023-04-08",<br />        "link_b": "-",<br />        "link_photo": "-",<br />        "link_page": "-",<br />        "link_m": "-",<br />        "groups": [<br />            {<br />                "group_name": "-",<br />                "group_link": "-",<br />                "group_logo_link": "-"<br />            },<br />            {<br />                "group_name": "-",<br />                "group_link": "-",<br />                "group_logo_link": "-"<br />            }<br />        ]<br />    },<br />]</pre>

## Python и использованные библиотеки
Python 3.10.5 
<ul>
<li>requests==2.28.2 - получение данных с сайта</li>
<li>bs4==0.0.1 - beautifulsoup - для разбора файлов HTML</li>
<li>lxml==4.9.2 - библиотека парсера для разбора HTML </li>
</ul>


## Применение
<ul>
<li>urls_get.py - получение всех ссылок на страницах каталога с постраничным выводом, запись полученных url в файл urls_new.txt</li>
<li>urls_select.py - получение списка уникальных ссылок с применением фильтра по вхождению в url заданной подстроки, запись или добавление полученных url в файл urls_uniq_final.txt </li>
<li>main.py - получение данных со страниц сайта (по списку url из файла urls_uniq_final.txt) запись данных в файл .json (data.json)</li>
</ul>