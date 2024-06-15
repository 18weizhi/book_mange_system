from book_manage_mvc.views.UI.modifypwd import Ui_Form
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow
import sys


class ModifyPwd(QWidget, Ui_Form):
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setupUi(self)

    def submit(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = ModifyPwd()
    w.show()

    app.exec_()