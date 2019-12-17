import mysql.connector
import os


# cursor = conn.cursor()
# # cursor.execute('create table user (id varchar(20) primary key,name varchar(20))')
# # cursor.execute('insert into user (id,name) values (%s,%s)',['1','liujian'])
# cursor.execute('insert into user (id,name) values (%s,%s)',['2','liujian1'])
# conn.commit()
# cursor.close()
class operator_mysql:

    def __init__(self):
        self.conn = mysql.connector.connect(user='root', password='i23456', database='study')

    def create_table(self, sql):
        cur = self.conn.cursor()
        cur.execute(sql)
        self.conn.commit()
        cur.close()
        self.conn.close()

    def insert_sql(self, sql):
        cursor = self.conn.cursor()
        cursor.execute(sql)
        self.conn.commit()
        cursor.close()
        self.conn.close()

    def select_sql(self, sql):
        cursor = self.conn.cursor()
        cursor.execute(sql)
        res = cursor.fetchall()
        cursor.close()
        self.conn.close()
        return res


print(os.cpu_count())
