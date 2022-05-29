from api.db import db
from api.google.models import History, Table

def db_read():
    new_table = []
    table = Table.query.order_by(Table.id).all()
    for line in table:
        tabs = [line.id, line.number_order, line.price_by_usd, line.delivery_date]
        format_str = [str(i) for i in tabs]
        new_table.append(format_str)
    return new_table

def delete_data_in_db(delete: list):
    if delete:
        for line in delete:
            table = Table.query.filter(Table.id == line['id']).first()
            db.session.delete(table)
            db.session.commit()

def get_or_save_data_course(course_data: dict):
    history = History.query.filter(History.date == course_data['date']).first()
    #Сохраняет курс доллара если на текущую дату записи нету
    if not history:
        history = History(date=course_data['date'], price_usd=course_data['price_usd'])
        db.session.add(history)
        db.session.commit()

def update_data_in_db(update: list):
    new_line = []
    history_id = History.query.order_by(History.id.desc()).first()
    for line in update:
        line['history_id'] = history_id.id
        table = Table.query.filter(Table.id == line['id']).first()
        #Обновление цены в рублях если еще не было
        if table and table.history_id != history_id.id:
            Table.query.filter(Table.id == line['id']).update(line)
        if not table:
            new_line.append(line)
    #Добавление новых строк
    if new_line:
        db.session.bulk_insert_mappings(Table, new_line)
    db.session.commit()