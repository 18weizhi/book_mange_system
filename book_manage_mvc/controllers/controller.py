from PyQt5.QtGui import QDesktopServices
from book_manage_mvc.views import booktypeadd_wd, bookinfoadd_wd, booknamage_wd, editbooktype_wd, login_wd, modifypwd_wd, main_wd
import sys
from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5.QtCore import QUrl
from book_manage_mvc.models.user import User
from book_manage_mvc.models.data_base import Database


class Controller:
    def __init__(self):
        self.init_wd()
        self.link()

    def init_wd(self):
        self.bookinfoadd = bookinfoadd_wd.BookInfoAdd_wd()
        self.booktypeadd = booktypeadd_wd.BookTypeAddWd()
        self.booknamage = booknamage_wd.BookManageWd()
        self.editbooktype = editbooktype_wd.EditBookTypeWd()
        self.login = login_wd.LoginWd()
        self.modifypwd = modifypwd_wd.ModifyPwd()
        self.main = main_wd.Main_wd()

    def login_(self, name, pwd):
        """登录界面，登录成功后弹出主界面"""
        if pwd.strip() == '' or name.strip() == '':
            QMessageBox.warning(None, '错误提示', '账户或密码不能为空', QMessageBox.Ok | QMessageBox.Cancel, QMessageBox.Cancel)
        else:
            user = User(name, pwd)
            database = Database()
            database.execute(f"select * from t_user where user_name='{user.user_name}' and pwd='{user.pwd}'")
            result = database.fetchall()
            database.close()
            if result:
                self.main.show()
                self.login.hide()
            else:
                QMessageBox.warning(None, '错误提示', '账户或密码错误')

    def open_book_info(self, lab):
        """打开图书添加界面和图书管理界面"""
        if lab == '图书添加':
            self.bookinfoadd.show()
        elif lab == '图书信息管理':
            self.booknamage.show()
        elif lab == '图书类别添加':
            self.booktypeadd.show()
        elif lab == '图书类别信息管理':
            self.editbooktype.show()
        elif lab == '修改密码':
            self.modifypwd.show()
        elif lab == '安全退出':
            respones = QMessageBox.question(None, '系统提示', '确定要退出吗？')
            if respones == QMessageBox.Yes:
                self.main.close()
        elif lab == '关于作者':
            QDesktopServices.openUrl(QUrl("https://www.bilibili.com/"))



    def link(self):
        """链接所有的界面的信号"""
        self.login.signal_name_pwd.connect(lambda name, pwd: self.login_(name, pwd))
        self.main.signal_lab.connect(lambda lab: self.open_book_info(lab))

    def run(self):
        self.login.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    c = Controller()
    c.run()

    app.exec_()

