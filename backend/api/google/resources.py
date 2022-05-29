from api.google.compare_table import compare_table
from api.google.db_utils import update_data_in_db, db_read, get_or_save_data_course
from api.google.models import AnswerTable
from api.google.utils import read_table, create_dict

from flask_restful import Resource
from flask import jsonify

class GoogleSheets(Resource):
    def get(self):
        answer = AnswerTable()
        # Читаем таблицу из базы данных
        read_table_in_db = db_read()
        # Читаем таблицу с google
        table = read_table(num_start=1, num_end=40)
        # Если таблица пуста то используется значение по умолчанию
        if not table:
            table = answer.answer_null
        # Сравниваем таблицы и вносим изменения если они есть
        compare_table(table[1:], read_table_in_db)
        # Создаем список словарей
        format_table = create_dict(table)
        # Узнаем курс на текущую дату
        course_usd = answer.course_date()
        # Если нового курса в бд нету, то записываем
        get_or_save_data_course(course_usd)
        # Получаем новую таблицу с изминениями
        answer = answer.new_table(format_table, course_usd)
        # Обновляем бд
        update_data_in_db(answer)
        # Отправляем ответ
        return jsonify(answer)
