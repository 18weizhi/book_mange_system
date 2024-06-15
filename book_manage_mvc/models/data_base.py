from pymysql import connections
from book_manage_mvc.config.db_config import DB_config


class Database:
    def __init__(self):
        self.con = connections.Connection(**DB_config)
        self.cursor = self.con.cursor()

    def execute(self, sql):
        self.cursor.execute(sql)

    def fetchall(self):
        return self.cursor.fetchall()

    def close(self):
        self.cursor.close()
        self.con.close()

def login(user):
    """
    用户登录判断
    :param user:    用户实体
    :return:    登录成功返回用户信息实体，登录失败返回None
    """
    con = None
    try:
        con = Database()
        con.execute(f"select * from t_user where user_name='{user.user_name}' and pwd='{user.pwd}'")
        result = con.fetchall()
        return result
    except Exception as e:
        print(e)
        return None
    finally:
        con.close()


if __name__ == '__main__':
    d = Database