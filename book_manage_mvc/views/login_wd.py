from book_manage_mvc.views.UI.login import Ui_Form
from PyQt5.QtWidgets import QWidget, QApplication
import sys
from PyQt5.QtCore import pyqtSignal


class LoginWd(QWidget, Ui_Form):
    signal_name_pwd = pyqtSignal(str,str)
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setupUi(self)

    def login(self):
        self.signal_name_pwd.emit(self.user_name_le.text(), self.pwd_le.text())

    def reset(self):
        self.user_name_le.clear()
        self.pwd_le.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = LoginWd()
    w.show()

    app.exec_()