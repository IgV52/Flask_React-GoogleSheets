from cbrf.models import DailyCurrenciesRates
from api.google.google_sheets import read_sheets
from api.google.db_utils import get_or_save_data_course
from datetime import datetime

def create_dict(table: list):
    list_keys = table[0]
    list_values = table[1:]
    new_table = []
    #Создание словаря по модели БД
    if len(list_keys) == 5:
        for dicts in table:
            new_dicts = {}
            new_dicts['id']=dicts['№']
            new_dicts['number_order']=dicts['заказ №']
            new_dicts['price_by_usd']=dicts['стоимость,$']
            new_dicts['delivery_date']=dicts['срок поставки']
            new_dicts['price_by_rub']=dicts['стоимость в руб']
            new_table.append(new_dicts)
    #Cоздание json из данных таблицы
    else:
        for values in list_values:
            dict_data = dict(zip(list_keys, values))
            new_table.append(dict_data)
    return new_table

def convert_money(table: list, course_data: dict):
    #Конвертация цены
    price_by_rub = [round(float(price_by_usd['стоимость,$'])*course_data['price_usd'],2) 
                    for price_by_usd in table if price_by_usd['стоимость,$']]
    
    new_table = []
    #Добавление колонки цена в руб
    for index,dicts in enumerate(table):
        dicts['стоимость в руб'] = price_by_rub[index]
        new_table.append(dicts)
    #Создает финальный файлик для опраки в базу
    new_table = create_dict(new_table)
    return new_table

def course_usd():
    #Код доллара
    id_code = 'R01235'
    date = datetime.today()
    daily = DailyCurrenciesRates(date=date)
    #Перевод даты в рус формат
    date = daily.date.strftime("%d.%m.%Y")
    price_usd = float(daily.get_by_id(id_code).value)
    data_course = {'date': date, 'price_usd': price_usd}
    #Сохранение цены курса и даты
    get_or_save_data_course(data_course)
    return data_course

def read_table(num_start: int, num_end: int):
    new_table = []
    #Читает таблицу до тех пор пока конечная точка
    #не будет больше полученного значения
    while True:
        table = read_sheets(num_start, num_end)
        new_table += table
        #Проверка полученной таблицы на длинну
        if check_data_table(new_table, num_end):
            return new_table
        #1 - корректировка начальной точки
        num_start = 1 + num_end 
        #Шаг 50
        num_end += 50 
    
def check_data_table(new_table: list, num_end: int):
    if len(new_table) == num_end:
        return False
    return True
