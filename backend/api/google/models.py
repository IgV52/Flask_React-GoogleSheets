from api.db import db
from cbrf.models import DailyCurrenciesRates
from sqlalchemy import Column, Float, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from api.google.utils import convert_money, date_and_course

import datetime

class AnswerTable:
    
    def __init__(self):
        self.id_code = 'R01235'
        self.date = datetime.datetime.today()
        self.daily = DailyCurrenciesRates(date=self.date)
        self.answer_null = [['№', 'заказ №', 'стоимость,$', 'срок поставки'], ['0', '0', '0', '0']] 

    def course_date(self):
        self.price_usd = self.daily.get_by_id(self.id_code).value
        self.course_info = date_and_course(self.date, self.price_usd)
        return self.course_info

    def new_table(self, table: list, course_usd: dict):
        self.new_table = convert_money(table, course_usd)
        return self.new_table

    def __repr__(self):
        return f"{self.answer_null}" 

class History(db.Model):
    __tablename__ = 'history'

    id = Column(Integer, primary_key=True)
    date = Column(String)
    price_usd = Column(Float)
    table = relationship('Table', backref='tables')

    def __repr__(self):
        return f"{self.id}"

class Table(db.Model):
    __tablename__ = 'tables'

    id = Column(Integer, primary_key=True)
    number_order = Column(Integer)
    price_by_usd = Column(Integer)
    delivery_date = Column(String)
    price_by_rub = Column(Integer)
    history_id = Column(Integer, ForeignKey('history.id'))

    def __repr__(self):
        return f"[{self.id}, {self.number_order}, {self.price_by_usd}, {self.delivery_date}]"

