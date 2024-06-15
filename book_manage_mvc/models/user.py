"""
用户实体类
"""


class User():
    # 主键ID
    id = None
    # 用户名
    user_name = None
    # 密码
    pwd = None
    # 新密码
    newpwd = None

    def __init__(self, user_name, pwd):
        self.user_name = user_name
        self.pwd = pwd

    @classmethod
    def myinit(cls, user_name, pwd, newpwd):
        obj = User(user_name, pwd)
        obj.newpwd = newpwd
        return obj

    def login(self, user):
        """
        用户登录判断
        :param user:    用户实体
        :return:    登录成功返回用户信息实体，登录失败返回None
        """
        con = None
        try:
            con = dbUtil.getCon()
            print(type(con))
            cursor = con.cursor()
            print(type(cursor))
            cursor.execute(f"select * from t_user where user_name='{user.user_name}' and pwd='{user.pwd}'")
            result = cursor.fetchone()
            print(result)
            return result
        except Exception as e:
            con.rollback()
            print(e)
            return None
        finally:
            dbUtil.closeCon(con)