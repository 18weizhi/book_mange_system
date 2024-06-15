from book_manage_mvc.views.UI.booktypeadd import Ui_Form
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow
import sys


class BookTypeAddWd(QWidget, Ui_Form):
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setupUi(self)

    def reset(self):
        pass

    def add(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = BookTypeAddWd()
    w.show()

    app.exec_()