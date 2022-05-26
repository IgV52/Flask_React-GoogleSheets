from api.google.db_utils import delete_data_in_db

import json
import os
import pandas

basedir = os.path.join('google_table', 'table.json')
os.makedirs('google_table', exist_ok=True)

def check_table(data):
    #Проверяет наличие таблицы в фалике json
    #Если есть читает и сравнивает изменения
    if os.path.isfile(basedir):
        read = read_file()
        compare_file(data, read)
        return False
    return True

def compare_file(data, read):
    df_new = pandas.json_normalize(data)
    df_old = pandas.json_normalize(read)
    newdf=(
        pandas.concat([df_new,df_old]).
        drop_duplicates(keep=False)).to_dict(orient='records'
        )
    #Проверяет есть ли изменения
    if newdf:
        deletes = []
        for line in newdf:
            #Найденые изменения добавляються 
            #в список deletes для удаления
            if line in read:
                line['id'] = line['№']
                deletes.append(line)
        if deletes:
            delete_data_in_db(deletes)
    #Создается новый обновленный файлик
    create_file(data)

def create_file(data):
    with open(basedir,'w+', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def read_file():
    with open(basedir,'r', encoding='utf-8') as f:
        read = json.load(f)
    return read

    