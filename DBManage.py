#数据库操作类
#-*- coding:UTF-8 -*-
import pymssql
class DBManage:
    def __init__(self,host,port,user,password,database,charset):
        self.host=host
        self.port=port
        self.user=user
        self.password=password
        self.database=database
        self.charset=charset

    #获得sqlserver连接
    def getMSSConnetion(self):
        self.conn=pymssql.connect(host=self.host,port=self.port,user=self.user,password=self.password,database=self.database,charset=self.charset)
        self.cursor=self.conn.cursor()
    def SaveSql(self,sql):
        self.cursor.execute(sql)
        self.cursor.commit()
    def QuerySql(self,sql):
        self.cursor.execute(sql)
        return self.cursor
    def closeConn(self):
        self.conn.close()


