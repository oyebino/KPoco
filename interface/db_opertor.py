import pymysql.cursors
import pymysql
import traceback
from Config.Config import Config
from common.logger import logger as log

class db_opertor:
    def __init__(self, charset="utf-8"):
        self.host = Config().db
        self.user = Config().db_user
        self.password = Config().db_password
        self.port = int(Config().db_port)
        self.database = Config().db_name
        self.charset = charset

    # 数据库连接方法:
    def open(self):
        self.db = pymysql.connect(host=self.host, user=self.user,
                          password=self.password, port=self.port,
                          database=self.database, charset="utf8")
        # 游标对象
        self.cur = self.db.cursor()

    # 数据库关闭方法:
    def close(self):
        self.cur.close()
        self.db.close()

    # 数据库执行操作方法:
    def execute(self, sql, L=[]):
        try:
            self.open()
            self.cur.execute(sql, L)
            self.db.commit()
            print("ok")
        except Exception as e:
            self.db.rollback()
            print("Failed", e)
        self.close()

    # 数据库查询所有操作方法:
    def select(self, sql, L =[]):
        try:
            self.open()
            self.cur.execute(sql, L)
            result = self.cur.fetchall()
            return result
        except Exception as e:
            print("Failed", e)
        self.close()

if __name__ == '__main__':
    a = db_opertor()
    a.open()
    csql = "select ID from coupon_template where name ='UI一点停通用劵25元'"
    result = a.select(csql)[0][0]
    print(result)