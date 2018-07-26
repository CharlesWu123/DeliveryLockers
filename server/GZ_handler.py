# GZ_MYSQL.py
from pymysql import *
class Sql_pj(object):
    def __init__(self):
        self.host = 'localhost'
        self.port = 3306
        self.user = 'root'
        self.passwd = '123456'
        self.db='delivery'
        self.charset = 'utf8'
    def open(self):
        try:
            self.conn=connect(host=self.host,port=self.port,user=self.user,
                passwd=self.passwd,db=self.db,charset=self.charset)
            self.cur=self.conn.cursor()
            # print('ok')
        except Exception as e:
            print(e)
    def close(self):
        self.cur.close()
        self.conn.close()


    def execute_select(self,sql):
        self.open()
        try:
            self.cur.execute(sql)
            result=self.cur.fetchall()
            return result
        except Exception:
            self.conn.rollback()
            return 'False'

    def execute_write(self,sql):
        self.open()
        try:
            self.cur.execute(sql)
            self.conn.commit()
            return 'True'
        except Exception:
            self.conn.rollback() 
            return 'False'       

# 创建数据库对象
mydb = Sql_pj()
def create_table(mydb):
    # 创建的sql语句
    # sql='create table gz_info(id int primary key auto_increment,\
    #                                      ipaddr varchar(20),\
    #                                      emsnum varchar(25),\
    #                                      phone char(11),\
    #                                      size char(2),\
    #                                      md5 char(6),\
    #                                      state enum("Null","Full","Done"),\
    #                                      time timestamp);'
    # rul=mydb.execute_write(sql)
    sql='create table user_info(id int primary key auto_increment,\
    username varchar(20),passwd char(6));'
    rul=mydb.execute_write(sql)
    print(rul)
if __name__ == '__main__':
    create_table(mydb)
