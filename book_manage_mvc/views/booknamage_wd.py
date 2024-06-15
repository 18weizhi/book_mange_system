from book_manage_mvc.views.UI.bookmanage import Ui_Form
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow
import sys


class BookManageWd(QWidget, Ui_Form):
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setupUi(self)

    def init_tablewidget(self):
        pass

    def modify(self):
        pass

    def delete(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = BookManageWd()
    w.show()

    app.exec_()