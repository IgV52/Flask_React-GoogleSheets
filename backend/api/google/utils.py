from decimal import Decimal
from api.google.google_sheets import read_sheets
from datetime import datetime

def check_data_table(table: list):
    if table:
        return False
    return True

def convert_money(table: list, course_data: dict):
    new_table = []
    #Конвертация цены
    price_by_rub = [round(float(price_by_usd['стоимость,$'])*course_data['price_usd'],2) 
                    for price_by_usd in table]
    for index,dicts in enumerate(table):
        dicts['стоимость в руб'] = price_by_rub[index]
        new_table.append(dicts)
    #Создает финальный файлик для отправки в базу
    new_table = create_dict(new_table)
    return new_table

def date_and_course(date: datetime, course: Decimal):
    #Перевод даты в рус формат
    date = date.strftime("%d.%m.%Y")
    price_usd = float(course)
    data_course = {'date': date, 'price_usd': price_usd}
    return data_course

def create_dict(table: list):
    list_keys = table[0]
    list_values = table[1:]
    new_table = []
    #Создание словаря по модели БД
    if isinstance(table[0], dict):
        for dicts in table:
            new_dicts = {}
            new_dicts['id']=dicts['№']
            new_dicts['number_order']=dicts['заказ №']
            new_dicts['price_by_usd']=dicts['стоимость,$']
            new_dicts['delivery_date']=dicts['срок поставки']
            new_dicts['price_by_rub']=dicts['стоимость в руб']
            new_table.append(new_dicts)
    #Cоздание списка словарей из данных таблицы
    else:
        for values in list_values:
            dict_data = dict(zip(list_keys, values))
            new_table.append(dict_data)
    return new_table

def read_table(num_start: int, num_end: int):
    new_table = []
    while True:
        table = read_sheets(num_start, num_end)
        #Проверка запроса таблицы, если запрос пришел
        #пустой то цикл останавливается
        if check_data_table(table):
            return new_table
        new_table += table
        #1 - корректировка начальной точки
        num_start = 1 + num_end 
        #Шаг 50
        num_end += 50 
