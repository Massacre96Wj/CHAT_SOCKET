from pymysql import connect
from config import *

class DB(object):
    def __init__(self):
        self.conn = connect(host = DB_HOST,
                            user = DB_USER,
                            port = DB_PORT,
                            password = DB_PASS,
                            database=DB_NAME
                            )
        self.cursor = self.conn.cursor()
    def get_one(self,sql):
        self.cursor.execute(sql)
        query_result = self.cursor.fetchone()
        if not query_result:
            return None
        fields = [field[0] for field in self.cursor.description]
        return_data = {}
        for field,value in zip(fields,query_result):
            return_data[field] = value
        return return_data
    def close(self):
        self.cursor.close()
        self.conn.close()
'''
测试函数
if __name__ == '__main__':
db = DB()
print(db.get_one("select * from users where user_name = 'john'"))
'''

