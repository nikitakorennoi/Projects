'''Приложение ТЕЛЕМАСТЕРСКАЯ для автоматизированного контроля работ по
ремонту бытовой техники. БД должна содержать таблицу Ремонт телевизоров,
имеющую следующую структуру записи: Марка телевизора, Завод-изготовитель, Цена,
Дата ремонта, Документ, Мастер, Сумма оплаты.'''

import sqlite3 as sq
from televizor import televizor_info


with sq.connect('telemasterskaya.db') as con:
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS remont_tel")
    cur.execute("CREATE TABLE IF NOT EXISTS remont_tel("
                "marka TEXT ,"
                "zavod TEXT NOT NULL,"
                "price INTEGER NOT NULL,"
                "data DATE NOT NULL,"
                "document TEXT NOT NULL,"
                "master TEXT NOT NULL,"
                "price_oplat INTEGER NOT NULL)")
    
with sq.connect('telemasterskaya.db') as con:
    cur = con.cursor()
    cur.executemany("INSERT INTO remont_tel VALUES(?,?,?,?,?,?,?)", televizor_info)
    
with sq.connect('telemasterskaya.db') as con:
    cur = con.cursor()
    cur.execute("SELECT * FROM remont_tel WHERE marka=='Sony'")
    result_1 = cur.fetchall()
    print(*result_1, sep='\n', end='\n\n')
    
with sq.connect('telemasterskaya.db') as con:
    cur = con.cursor()
    cur.execute("SELECT * FROM remont_tel WHERE zavod=='ChinaFactory'")
    result_2 = cur.fetchall()
    print(*result_2, sep='\n', end='\n\n')
    
with sq.connect('telemasterskaya.db') as con:
    cur = con.cursor()
    cur.execute("SELECT * FROM remont_tel WHERE price>60000")
    result_3 = cur.fetchall()
    print(*result_3, sep='\n', end='\n\n')


with sq.connect('telemasterskaya.db') as con:
    cur = con.cursor()
    cur.execute("UPDATE remont_tel SET price=80000 WHERE document=='Есть' AND master=='Василий' ")
    cur.execute("SELECT * FROM remont_tel WHERE price=80000")
    result_4 = cur.fetchall()
    print(*result_4, sep='\n', end='\n\n')
    

with sq.connect('telemasterskaya.db') as con:
    cur = con.cursor()
    cur.execute("UPDATE remont_tel SET document='Есть' WHERE zavod=='Foxconn' ")
    cur.execute("SELECT * FROM remont_tel WHERE document='Есть'")
    result_5 = cur.fetchall()
    print(*result_5, sep='\n', end='\n\n')
    

with sq.connect('telemasterskaya.db') as con:
    cur = con.cursor()
    cur.execute("UPDATE remont_tel SET price_oplat=5000 WHERE master=='Василий' ")
    cur.execute("SELECT * FROM remont_tel WHERE price_oplat=5000 ")
    result_6 = cur.fetchall()
    print(*result_6, sep='\n', end='\n\n')


with sq.connect('telemasterskaya.db') as con:
    cur = con.cursor()
    cur.execute("DELETE FROM remont_tel WHERE price<24000")
    cur.execute("SELECT * FROM remont_tel")
    result_7 = cur.fetchall()
    print(*result_7, sep='\n', end='\n\n')


with sq.connect('telemasterskaya.db') as con:
    cur = con.cursor()
    cur.execute("DELETE FROM remont_tel WHERE price_oplat<1600")
    cur.execute("SELECT * FROM remont_tel")
    result_8 = cur.fetchall()
    print(*result_8, sep='\n', end='\n\n')
    

with sq.connect('telemasterskaya.db') as con:
    cur = con.cursor()
    cur.execute("DELETE FROM remont_tel WHERE document=='Нет' ")
    cur.execute("SELECT * FROM remont_tel")
    result_9 = cur.fetchall()
    print(*result_9, sep='\n', end='\n\n') 