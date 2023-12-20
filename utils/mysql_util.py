import pymysql

from utils.read import base_data

data = base_data.read_data()['mysql']
DB_CONF = {
    "host": data['MYSQL_HOST'],
    "port": data['MYSQL_PORT'],
    "user": data['MYSQL_USER'],
    "password": data['MYSQL_PASSWD'],
    "db": data['MYSQL_DB']
}


class MysqlDb:
    def __init__(self):
        # 连接mysql数据库
        self.conn = pymysql.connect(**DB_CONF, autocommit=True)
        self.cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    # 释放资源
    def __del__(self):
        self.cur.close()
        self.conn.close()

