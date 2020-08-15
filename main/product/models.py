# -*- coding: utf-8 -*-
from main import db
from sqlalchemy import Column, desc, text, create_engine
from constants import STRING_LEN


class Product(db.Model):

    __tablename__ = 'tbl_product'

    id = Column(db.Integer, primary_key=True)
    first_name = Column(db.String(STRING_LEN), nullable=False, unique=True)
    last_name = Column(db.String(STRING_LEN), nullable=False, unique=True)
    pet_name = Column(db.String(STRING_LEN), nullable=False, default="")
    email = Column(db.String(STRING_LEN), nullable=False, default="")
    gender = Column(db.Numeric, nullable=False, default=0.0)
    ip_address = Column(db.String(STRING_LEN), nullable=False, default="")

    def __repr__(self):
        return '<tbl_product %r>' % self.first_name
    
    @staticmethod
    def get_product_list(data, select):
        print(data)
        sql_query = 'SELECT * from tbl_product '
        sql_query += ' ORDER BY id DESC '
        if(select == 'select'):
            sql_query += ' LIMIT '+str(data['Limitpage'])
            if(data['start'] > 0):
                sql_query += ' OFFSET '+str(data['start'])
        sql = text(sql_query)
        datalist = db.engine.execute(sql)
        result_list = datalist.fetchall()
        if(select == 'count'):
            return len(result_list)
        return result_list
