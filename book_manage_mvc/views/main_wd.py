from book_manage_mvc.views.UI.main import Ui_MainWindow
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QAction
from PyQt5.QtCore import pyqtSignal
import sys


class Main_wd(QMainWindow, Ui_MainWindow):
    signal_lab = pyqtSignal(str)
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setupUi(self)
        self.menu_2.triggered[QAction].connect(self.openbooktype)
        self.menu.triggered[QAction].connect(self.openbook)
        self.menu_3.triggered[QAction].connect(self.opensettings)

    def openbooktype(self, obj):
        if obj.text() == '图书类别添加':
            self.signal_lab.emit('图书类别添加')
        elif obj.text() == '图书类别信息管理':
            self.signal_lab.emit('图书类别信息管理')

    def openbook(self, obj):
        if obj.text() == '图书添加':
            self.signal_lab.emit('图书添加')
        elif obj.text() == '图书信息管理':
            self.signal_lab.emit('图书信息管理')

    def opensettings(self, obj):
        if obj.text() == '修改密码':
            self.signal_lab.emit('修改密码')
        elif obj.text() == '安全退出':
            self.signal_lab.emit('安全退出')
        elif obj.text() == '关于作者':
            self.signal_lab.emit('关于作者')


if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = Main_wd()
    w.show()

    app.exec_()