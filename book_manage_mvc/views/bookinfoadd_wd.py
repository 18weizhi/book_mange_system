from book_manage_mvc.views.UI.bookinfoadd import Ui_Form
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow
from PyQt5.QtCore import pyqtSignal
import sys


class BookInfoAdd_wd(QWidget, Ui_Form):
    signal_info = pyqtSignal(str, str, str, str, str)
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setupUi(self)

    def add_book(self):
        self.signal_info.emit(self.bookname_le.text(), self.bookauthor_le.text(), self.bookprice_le.text(), self.booktype_cb.currentData(), self.bookdesc_pte.toPlainText())

    def reset(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = BookInfoAdd_wd()
    w.show()

    app.exec_()