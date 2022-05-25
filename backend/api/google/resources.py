from flask_restful import Resource
from api.google.utils import convert_money, course_usd, read_table, create_dict
from api.google.compare_table import check_table, create_file
from api.google.db_utils import update_data_in_db
from flask import jsonify

class GoogleSheets(Resource):
    def get(self):
        #Делает запрос к базу и преобразует в список словарей
        table = create_dict(read_table(num_start=1, num_end=50))
        #Проверяет есть ли таблица в файле формата json
        check_update = check_table(table)
        #Проверяет курс валют
        course_data = course_usd()
        #Возвращает полностью готовый файлик json с ценой в рублях
        price_by_rub = convert_money(table, course_data)
        #Если нету создает файлик и записывает в базу
        if check_update:
            create_file(table)
            update_data_in_db(price_by_rub) 
        #Если есть то просто записывает обновления 
        if not check_update:
            update_data_in_db(price_by_rub)
        return jsonify(price_by_rub)
