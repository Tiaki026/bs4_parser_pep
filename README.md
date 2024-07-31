# PEP Parser

# Оглавление
- [:page_with_curl: Описание](https://github.com/Tiaki026/bs4_parser_pep#page_with_curl-описание)
- [Процесс разработки, особенности и трудности](https://github.com/Tiaki026/bs4_parser_pep#процесс-разработки-особенности-и-трудности)
  - [Было изучено](https://github.com/Tiaki026/bs4_parser_pep#было-изучено)
  - [Трудности возникшие в работе](https://github.com/Tiaki026/bs4_parser_pep#трудности-возникшие-в-работе)
- [:computer: Стек технологий](https://github.com/Tiaki026/bs4_parser_pep#computer-стек-технологий)
- [:page_with_curl: Как воспользоваться проектом](https://github.com/Tiaki026/bs4_parser_pep#page_with_curl-как-воспользоваться-проектом)
  - [Подготовка проекта](https://github.com/Tiaki026/bs4_parser_pep#подготовка-проекта)
  - [Работа с проектом](https://github.com/Tiaki026/bs4_parser_pep?tab=readme-ov-file#работа-с-проектом)
- [Автор](https://github.com/Tiaki026/bs4_parser_pep#автор)

## :page_with_curl: Описание
PEP Parser — это инструмент для парсинга PEP (Python Enhancement Proposals) с [официального сайта](https://peps.python.org/) и версий python c [официального сайта](https://docs.python.org/3/). Скрипт позволяет анализировать статусы PEP и выводить результаты в виде количества каждого статуса, собирать версии python и выводить результат с номером версии, статуса и ее авторов.

## Процесс разработки, особенности и трудности
Первый проект парсинга по курсу "**Python-разработчик+**" [Яндекс Практикума](https://github.com/yandex-praktikum).
### Было изучено:
- Библиотека BeautifulSoup4. Как с её помощью "вытащить" из HTML-кода нужное и работать с этим.
- Библиотека requests_cache для кеширования сессии.
- Библиотека tqdm для отображения прогресс-бара в терминале.
- Библиотека PrettyTable для вывода данных в таблицу.
- Работа с регулярными выражениями.
- Вывод данных в файлы csv и zip.

### Трудности возникшие в работе
Самое сложное для меня это HTML-код. Можно долго его разглядывать и искать нужное соблюдая иерархию. 
Оптимизация производительности - парсинг большого количества данных может занимать много времени.

## :computer: Стек технологий
- ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) Python: Язык программирования
- ![HTML](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white) HTML: Стандартизированный язык гипертекстовой разметки документов для просмотра веб-страниц в браузере
- ![BS4](https://camo.githubusercontent.com/8a2aab0d5a7f5ce7d12bbb8f908e7786bcad6c7dd255bdc6aa5fe667f61ae625/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f2d42656175746966756c536f7570342d3436343634363f7374796c653d666c6174266c6f676f3d42656175746966756c536f757034266c6f676f436f6c6f723d66666666666626636f6c6f723d303433413642) BeautifulSoup4: библиотека для парсинга HTML и XML документов в Python
- ![](https://camo.githubusercontent.com/743f11984a5735008002ac2d2b146517e0b53a5788c4f07b0291ef5883ae9f34/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f616374696f6e732f776f726b666c6f772f7374617475732f7471646d2f7471646d2f746573742e796d6c3f6272616e63683d6d6173746572266c6162656c3d7471646d266c6f676f3d476974487562) tqdm: библиотека отображения прогресс-бара
- ![PT](https://camo.githubusercontent.com/fd87112e437d5861ab358398eefda2c12a17dd29154d0a4ec888e4da4cc31ffa/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f2d5072657474797461626c652d3436343634363f7374796c653d666c6174266c6f676f3d5072657474797461626c65266c6f676f436f6c6f723d66666666666626636f6c6f723d303433413642) PrettyTable:  библиотека вывода данных в таблицу
- ![rq](https://camo.githubusercontent.com/25c089f154cd5dd784ac64a1e48848c86304eba36c90eb7d6f3dd89765e5ecb3/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f52657175657374732d322e32372d333737364142) requests_cache: Библиотека кеширования сессии


## :page_with_curl: Как воспользоваться проектом
### Подготовка проекта
1. Клонирование проекта с GitHub
```
git@github.com:Tiaki026/bs4_parser_pep.git
```
2.	Создайте виртуальное окружение.

Linux
```
python3 -m venv venv
```
Windows
```
python -m venv venv
```
3.	Активируйте виртуальное окружение.

Linux
```
source venv/bin/activate
```
Windows
```
source venv/Scripts/activate
```
4.	Установите зависимости.
```
pip install -r requirements.txt
```
### Работа с проектом
- Вызов справки
```
$ python src/main.py -h

"31.07.2024 14:46:21 - [INFO] - Парсер запущен!"
usage: main.py [-h] [-c] [-o {pretty,file}] {whats-new,latest-versions,download,pep}

Парсер документации Python

positional arguments:
  {whats-new,latest-versions,download,pep}
                        Режимы работы парсера

options:
  -h, --help            show this help message and exit
  -c, --clear-cache     Очистка кеша
  -o {pretty,file}, --output {pretty,file}
                        Дополнительные способы вывода данных
```
- Вызов whats-new,latest-versions,download,pep c доступными опциями.

  -с или --clear-cache очищает кеш и заставляет парсить сайт вновь
  
  :warning: Предупреждение :warning:: парсинг pep без кеша занимает время около 5 минут.
```
$ python src/main.py -o pretty -c pep

"31.07.2024 15:31:06 - [INFO] - Парсер запущен!"
"31.07.2024 15:31:06 - [INFO] - Аргументы командной строки: Namespace(mode='pep', clear_cache=True, output='pretty')"
"31.07.2024 15:31:06 - [INFO] - Clearing all items from the cache"
100%|███████████████████████████████████████████████████████████████████████████████████████████████████| 649/649 [04:05<00:00,  2.64it/s]
"31.07.2024 15:35:20 - [WARNING] -
 Статус не совпадает:  https://peps.python.org/pep-0401/

      Полученный статус: April Fool!
      Ожидаемый статус: Rejected
"
+-------------+------------+
| Статус      | Количество |
+-------------+------------+
| Active      | 33         |
| Withdrawn   | 61         |
| Superseded  | 23         |
| Final       | 315        |
| Rejected    | 124        |
| Deferred    | 36         |
| April Fool! | 1          |
| Accepted    | 22         |
| Draft       | 32         |
| Provisional | 2          |
| Total       | 649        |
+-------------+------------+
"31.07.2024 15:35:20 - [INFO] -  Парсер завершил работу."
```

  -o или --output вызываются с дополнительными методами pretty или file
  
  pretty выведет в терминал таблицу
  
  file скачает все в файл [src\result\ваш_файл.csv](https://github.com/Tiaki026/bs4_parser_pep/tree/master/src/results)
```
$ python src/main.py -o pretty latest-versions

"31.07.2024 14:49:15 - [INFO] - Парсер запущен!"
"31.07.2024 14:49:15 - [INFO] - Аргументы командной строки: Namespace(mode='latest-versions', clear_cache=False, output='pretty')"
+-------------------------------+--------+----------------+
| Ссылка на документацию        | Версия | Статус         |
+-------------------------------+--------+----------------+
| https://docs.python.org/3.14/ | 3.14   | in development |
| https://docs.python.org/3.13/ | 3.13   | pre-release    |
| https://docs.python.org/3.12/ | 3.12   | stable         |
| https://docs.python.org/3.11/ | 3.11   | security-fixes |
| https://docs.python.org/3.10/ | 3.10   | security-fixes |
| https://docs.python.org/3.9/  | 3.9    | security-fixes |
| https://docs.python.org/3.8/  | 3.8    | security-fixes |
| https://docs.python.org/3.7/  | 3.7    | EOL            |
| https://docs.python.org/3.6/  | 3.6    | EOL            |
| https://docs.python.org/3.5/  | 3.5    | EOL            |
| https://docs.python.org/3.4/  | 3.4    | EOL            |
| https://docs.python.org/3.3/  | 3.3    | EOL            |
| https://docs.python.org/3.2/  | 3.2    | EOL            |
| https://docs.python.org/3.1/  | 3.1    | EOL            |
| https://docs.python.org/3.0/  | 3.0    | EOL            |
| https://docs.python.org/2.7/  | 2.7    | EOL            |
| https://docs.python.org/2.6/  | 2.6    | EOL            |
+-------------------------------+--------+----------------+
"31.07.2024 14:49:15 - [INFO] -  Парсер завершил работу."
```
```
$ python src/main.py -o file latest-versions

"31.07.2024 14:56:22 - [INFO] - Парсер запущен!"
"31.07.2024 14:56:22 - [INFO] - Аргументы командной строки: Namespace(mode='latest-versions', clear_cache=False, output='file')"
"31.07.2024 14:56:22 - [INFO] -  Файл с результатами был сохранён: E:\Dev\bs4_parser_pep\src\results\latest-versions_2024-07-31_14-56-22.csv"
"31.07.2024 14:56:22 - [INFO] -  Парсер завершил работу."
```
- download скачивает в папку src\downloads архив со всей документацией
```
$ python src/main.py download
"31.07.2024 15:01:44 - [INFO] - Парсер запущен!"
"31.07.2024 15:01:44 - [INFO] - Аргументы командной строки: Namespace(mode='download', clear_cache=False, output=None)"
"31.07.2024 15:01:44 - [INFO] -  Архив был загружен и сохранён: E:\Dev\bs4_parser_pep\src\downloads\python-3.12.4-docs-pdf-a4.zip"
"31.07.2024 15:01:44 - [INFO] -  Парсер завершил работу."
```

## Автор:
  - [Колотиков Евгений](https://github.com/Tiaki026)
## 


  ## [:top: Путь наверх :top:](https://github.com/Tiaki026/bs4_parser_pep?tab=readme-ov-file#pep-parser)
