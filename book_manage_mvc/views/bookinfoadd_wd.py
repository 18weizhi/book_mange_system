from book_manage_mvc.views.UI.bookinfoadd import Ui_Form
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow
import sys


class BookInfoAdd_wd(QWidget, Ui_Form):
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setupUi(self)

    def add_book(self):
        pass

    def reset(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = BookInfoAdd_wd()
    w.show()

    app.exec_()