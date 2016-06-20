# -*- coding:UTF-8 -*-
import psycopg2
conn = psycopg2.connect(host='localhost',
        database="hw04", user="dbo", password="123456")
cur = conn.cursor()
cur.execute('''
DROP TABLE IF EXISTS hw_a;
CREATE TABLE IF NOT EXISTS hw_a(
    sn       INTEGER,    
    name     TEXT,       
    PRIMARY  KEY(sn)       
);
	''')
for i in range(6):
	sn = 10*i+10
	name = 'A%d' % sn
	cur.execute('''
		INSERT INTO hw_a(sn, name) VALUES (%(sn)s, %(name)s) 
	''',{'sn':sn, 'name':name})
cur.execute('''
DROP TABLE IF EXISTS hw_b;
CREATE TABLE IF NOT EXISTS hw_b(
    sn       INTEGER,    
    name     TEXT,      
    PRIMARY  KEY(sn)       
);
	''')
for i in range(5):
	sn = 10*(i+4)
	name = 'B%d' % sn
	cur.execute('''
		INSERT INTO hw_b(sn, name) VALUES (%(sn)s, %(name)s) 
	''', {'sn':sn, 'name':name} )
conn.commit()
