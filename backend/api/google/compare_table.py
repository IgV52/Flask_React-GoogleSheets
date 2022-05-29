from api.google.db_utils import delete_data_in_db

import pandas

def compare_table(data, read):
    df_new = pandas.DataFrame(data)
    df_old = pandas.DataFrame(read)
    newdf=(
        pandas.concat([df_new,df_old]).
        drop_duplicates(keep=False)).to_dict(orient='records'
        )
    #Проверяет есть ли изменения в таблице
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

    