
"""
== OpenWeatherMap ==

OpenWeatherMap — онлайн-сервис, который предоставляет бесплатный API
 для доступа к данным о текущей погоде, прогнозам, для web-сервисов
 и мобильных приложений. Архивные данные доступны только на коммерческой основе.
 В качестве источника данных используются официальные метеорологические службы
 данные из метеостанций аэропортов, и данные с частных метеостанций.

Необходимо решить следующие задачи:

== Получение APPID ==
    Чтобы получать данные о погоде необходимо получить бесплатный APPID.

    Предлагается 2 варианта (по желанию):
    - получить APPID вручную
    - автоматизировать процесс получения APPID,
    используя дополнительную библиотеку GRAB (pip install grab)

        Необходимо зарегистрироваться на сайте openweathermap.org:
        https://home.openweathermap.org/users/sign_up

        Войти на сайт по ссылке:
        https://home.openweathermap.org/users/sign_in

        Свой ключ "вытащить" со страницы отсюда:
        https://home.openweathermap.org/api_keys

        Ключ имеет смысл сохранить в локальный файл, например, "app.id"


== Получение списка городов ==
    Список городов может быть получен по ссылке:
    http://bulk.openweathermap.org/sample/city.list.json.gz

    Далее снова есть несколько вариантов (по желанию):
    - скачать и распаковать список вручную
    - автоматизировать скачивание (ulrlib) и распаковку списка
     (воспользоваться модулем gzip
      или распаковать внешним архиватором, воспользовавшись модулем subprocess)

    Список достаточно большой. Представляет собой JSON-строки:
{"_id":707860,"name":"Hurzuf","country":"UA","coord":{"lon":34.283333,"lat":44.549999}}
{"_id":519188,"name":"Novinki","country":"RU","coord":{"lon":37.666668,"lat":55.683334}}


== Получение погоды ==
    На основе списка городов можно делать запрос к сервису по id города. И тут как раз понадобится APPID.
        By city ID
        Examples of API calls:
        http://api.openweathermap.org/data/2.5/weather?id=2172797&appid=b1b15e88fa797225412429c1c50c122a

    Для получения температуры по Цельсию:
    http://api.openweathermap.org/data/2.5/weather?id=520068&units=metric&appid=b1b15e88fa797225412429c1c50c122a

    Для запроса по нескольким городам сразу:
    http://api.openweathermap.org/data/2.5/group?id=524901,703448,2643743&units=metric&appid=b1b15e88fa797225412429c1c50c122a


    Данные о погоде выдаются в JSON-формате
    {"coord":{"lon":38.44,"lat":55.87},
    "weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04n"}],
    "base":"cmc stations","main":{"temp":280.03,"pressure":1006,"humidity":83,
    "temp_min":273.15,"temp_max":284.55},"wind":{"speed":3.08,"deg":265,"gust":7.2},
    "rain":{"3h":0.015},"clouds":{"all":76},"dt":1465156452,
    "sys":{"type":3,"id":57233,"message":0.0024,"country":"RU","sunrise":1465087473,
    "sunset":1465149961},"id":520068,"name":"Noginsk","cod":200}


== Сохранение данных в локальную БД ==
Программа должна позволять:
1. Создавать файл базы данных SQLite со следующей структурой данных
   (если файла базы данных не существует):

    Погода
        id_города           INTEGER PRIMARY KEY
        Город               VARCHAR(255)
        Дата                DATE
        Температура         INTEGER
        id_погоды           INTEGER                 # weather.id из JSON-данных

2. Выводить список стран из файла и предлагать пользователю выбрать страну
(ввиду того, что список городов и стран весьма велик
 имеет смысл запрашивать у пользователя имя города или страны
 и искать данные в списке доступных городов/стран (регуляркой))

3. Скачивать JSON (XML) файлы погоды в городах выбранной страны
4. Парсить последовательно каждый из файлов и добавлять данные о погоде в базу
   данных. Если данные для данного города и данного дня есть в базе - обновить
   температуру в существующей записи.


При повторном запуске скрипта:
- используется уже скачанный файл с городами;
- используется созданная база данных, новые данные добавляются и обновляются.


При работе с XML-файлами:

Доступ к данным в XML-файлах происходит через пространство имен:
<forecast ... xmlns="http://weather.yandex.ru/forecast ...>

Чтобы работать с пространствами имен удобно пользоваться такими функциями:

    # Получим пространство имен из первого тега:
    def gen_ns(tag):
        if tag.startswith('{'):
            ns, tag = tag.split('}')
            return ns[1:]
        else:
            return ''

    tree = ET.parse(f)
    root = tree.getroot()

    # Определим словарь с namespace
    namespaces = {'ns': gen_ns(root.tag)}

    # Ищем по дереву тегов
    for day in root.iterfind('ns:day', namespaces=namespaces):
        ...

"""

import json
import sqlite3
import urllib.request
import io
import gzip
import os


# App_id:
id_file = open("app.id", "r", encoding="UTF-8")
app_id = id_file.readline() # app_id = f8961adb73646d76c00bd49e4a9074bd

print("App id is: {}".format(app_id))

# Automate download and unpacking json file:
file_url = "http://bulk.openweathermap.org/sample/city.list.json.gz"
file_name = file_url.split("/")[-1] # city.list.json.gz
outfile_path = file_name[:-3] # city.list.json

if outfile_path not in os.listdir():
    print("Download and read json file. It may take a while.")
    response = urllib.request.urlopen(file_url)
    compressed_file = io.BytesIO(response.read())
    decompressed_file = gzip.GzipFile(fileobj=compressed_file)

    with open(outfile_path, "wb") as outfile:
        outfile.write(decompressed_file.read())
else:
    print("File {} already exists.".format(outfile_path))

json_file = outfile_path

with open(json_file) as file:
    jason_data = json.load(file)

print("Making city_list from json file. It may take a while.")

city_list = []
counter = 0
for i in jason_data:
    if i.get("name") in city_list:
        pass
    else:
        append_item = {"name": i.get("name"), "id": i.get("id")}
        city_list.append(append_item)
        counter += 1

def user_city(city_list):
    user_city = input("Enter city (e.g. London): ")
    user_city_id = ""
    for i in city_list:
        if user_city == i.get("name"):
            user_city_id += str(i.get("id"))
            return user_city_id

user_city_id = user_city(city_list)
print("User city id: {}".format(user_city_id))


def weather_request(id, app_id):
    from urllib import request
    url = "http://api.openweathermap.org/data/2.5/weather?" + "id=" + id + "&appid=" + app_id
    response = request.urlopen(url)
    return response.read()


my_bytes = weather_request(user_city_id, app_id) # request in bytes
my_json = my_bytes.decode("utf-8")
data = json.loads(my_json)

print("My json request is: {}".format(data))

# Make class Weather:
class Weather:
    def __init__(self, city_id, data):
        self.city_id = city_id
        self.data = data
        self.__city = self.data.get("name")
        self.__date = self.data.get("dt")

    def get_temperature(self):
        self.get_main = self.data.get("main")
        return self.get_main.get("temp")

    def get_weather_id(self):
        self.get_weather = self.data.get("weather")
        return self.get_weather[0].get("id")
    @property
    def weather(self):
        return [self.city_id, self.__city, str(self.__date), str(self.get_temperature()), str(self.get_weather_id())]

weather = Weather(user_city_id, data).weather

# Make db table:
conn = sqlite3.connect("weather.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS weather(city_id text, city text, date text, temperature text, weather_id text)")

# Insert data:
cursor.execute("INSERT OR REPLACE INTO weather VALUES(?, ?, ?, ?, ?)", weather)
# Save changes:
conn.commit()

# Print db:
print("My bd is:", list(cursor.execute("SELECT * FROM weather")))