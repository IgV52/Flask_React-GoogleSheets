from api.db import db
from sqlalchemy import Column, Float, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class History(db.Model):
    __tablename__ = 'history'

    id = Column(Integer, primary_key=True)
    date = Column(String)
    price_usd = Column(Float)
    table = relationship('Table', backref='tables')

class Table(db.Model):
    __tablename__ = 'tables'

    id = Column(Integer, primary_key=True)
    number_order = Column(Integer)
    price_by_usd = Column(Integer)
    delivery_date = Column(String)
    price_by_rub = Column(Integer)
    history_id = Column(Integer, ForeignKey('history.id'))

