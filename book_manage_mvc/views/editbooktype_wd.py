from book_manage_mvc.views.UI.editbooktype import Ui_Form
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow
import sys


class EditBookTypeWd(QWidget, Ui_Form):
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setupUi(self)

    def search(self):
        pass

    def init_form(self):
        pass

    def update_form(self):
        pass

    def delete_row(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = EditBookTypeWd()
    w.show()

    app.exec_()