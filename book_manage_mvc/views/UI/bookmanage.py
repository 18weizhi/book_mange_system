# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bookmanage.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(936, 766)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(30, 10, 871, 91))
        self.groupBox.setObjectName("groupBox")
        self.bookname_la = QtWidgets.QLabel(self.groupBox)
        self.bookname_la.setGeometry(QtCore.QRect(10, 40, 68, 21))
        self.bookname_la.setObjectName("bookname_la")
        self.bookauthor_la = QtWidgets.QLabel(self.groupBox)
        self.bookauthor_la.setGeometry(QtCore.QRect(250, 40, 68, 21))
        self.bookauthor_la.setObjectName("bookauthor_la")
        self.booktype_la = QtWidgets.QLabel(self.groupBox)
        self.booktype_la.setGeometry(QtCore.QRect(490, 40, 68, 21))
        self.booktype_la.setObjectName("booktype_la")
        self.search_btn = QtWidgets.QPushButton(self.groupBox)
        self.search_btn.setGeometry(QtCore.QRect(770, 40, 93, 28))
        self.search_btn.setObjectName("search_btn")
        self.bookname_le = QtWidgets.QLineEdit(self.groupBox)
        self.bookname_le.setGeometry(QtCore.QRect(90, 40, 131, 20))
        self.bookname_le.setObjectName("bookname_le")
        self.bookauthor_le = QtWidgets.QLineEdit(self.groupBox)
        self.bookauthor_le.setGeometry(QtCore.QRect(330, 40, 131, 20))
        self.bookauthor_le.setObjectName("bookauthor_le")
        self.booktype_cb = QtWidgets.QComboBox(self.groupBox)
        self.booktype_cb.setGeometry(QtCore.QRect(580, 40, 131, 22))
        self.booktype_cb.setObjectName("booktype_cb")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(30, 130, 871, 231))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 390, 871, 351))
        self.groupBox_2.setObjectName("groupBox_2")
        self.id_la = QtWidgets.QLabel(self.groupBox_2)
        self.id_la.setGeometry(QtCore.QRect(10, 30, 68, 15))
        self.id_la.setObjectName("id_la")
        self.bookname_la2 = QtWidgets.QLabel(self.groupBox_2)
        self.bookname_la2.setGeometry(QtCore.QRect(260, 30, 68, 15))
        self.bookname_la2.setObjectName("bookname_la2")
        self.sex_la = QtWidgets.QLabel(self.groupBox_2)
        self.sex_la.setGeometry(QtCore.QRect(500, 30, 68, 15))
        self.sex_la.setObjectName("sex_la")
        self.price_la = QtWidgets.QLabel(self.groupBox_2)
        self.price_la.setGeometry(QtCore.QRect(10, 80, 68, 15))
        self.price_la.setObjectName("price_la")
        self.bookauthor_la2 = QtWidgets.QLabel(self.groupBox_2)
        self.bookauthor_la2.setGeometry(QtCore.QRect(260, 80, 68, 15))
        self.bookauthor_la2.setObjectName("bookauthor_la2")
        self.booktype_la2 = QtWidgets.QLabel(self.groupBox_2)
        self.booktype_la2.setGeometry(QtCore.QRect(500, 80, 68, 15))
        self.booktype_la2.setObjectName("booktype_la2")
        self.bookdesc = QtWidgets.QLabel(self.groupBox_2)
        self.bookdesc.setGeometry(QtCore.QRect(10, 120, 68, 15))
        self.bookdesc.setObjectName("bookdesc")
        self.modify_btn = QtWidgets.QPushButton(self.groupBox_2)
        self.modify_btn.setGeometry(QtCore.QRect(90, 290, 93, 28))
        self.modify_btn.setObjectName("modify_btn")
        self.delete_btn = QtWidgets.QPushButton(self.groupBox_2)
        self.delete_btn.setGeometry(QtCore.QRect(350, 290, 93, 28))
        self.delete_btn.setObjectName("delete_btn")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.groupBox_2)
        self.plainTextEdit.setGeometry(QtCore.QRect(90, 120, 781, 161))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.id_le = QtWidgets.QLineEdit(self.groupBox_2)
        self.id_le.setGeometry(QtCore.QRect(90, 30, 113, 20))
        self.id_le.setReadOnly(True)
        self.id_le.setObjectName("id_le")
        self.price_le = QtWidgets.QLineEdit(self.groupBox_2)
        self.price_le.setGeometry(QtCore.QRect(90, 80, 113, 20))
        self.price_le.setObjectName("price_le")
        self.bookname_le2 = QtWidgets.QLineEdit(self.groupBox_2)
        self.bookname_le2.setGeometry(QtCore.QRect(340, 30, 113, 20))
        self.bookname_le2.setObjectName("bookname_le2")
        self.bookauthor_le2 = QtWidgets.QLineEdit(self.groupBox_2)
        self.bookauthor_le2.setGeometry(QtCore.QRect(340, 80, 113, 20))
        self.bookauthor_le2.setObjectName("bookauthor_le2")
        self.booktype_cb2 = QtWidgets.QComboBox(self.groupBox_2)
        self.booktype_cb2.setGeometry(QtCore.QRect(590, 80, 121, 22))
        self.booktype_cb2.setObjectName("booktype_cb2")
        self.man_rbtn = QtWidgets.QRadioButton(self.groupBox_2)
        self.man_rbtn.setGeometry(QtCore.QRect(590, 30, 51, 19))
        self.man_rbtn.setChecked(True)
        self.man_rbtn.setObjectName("man_rbtn")
        self.femal_rbtn = QtWidgets.QRadioButton(self.groupBox_2)
        self.femal_rbtn.setGeometry(QtCore.QRect(660, 30, 51, 19))
        self.femal_rbtn.setObjectName("femal_rbtn")

        self.retranslateUi(Form)
        self.search_btn.clicked.connect(Form.init_tablewidget) # type: ignore
        self.modify_btn.clicked.connect(Form.modify) # type: ignore
        self.delete_btn.clicked.connect(Form.delete) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "bookmanage"))
        self.groupBox.setTitle(_translate("Form", "查询操作"))
        self.bookname_la.setText(_translate("Form", "图书名称："))
        self.bookauthor_la.setText(_translate("Form", "图书作者："))
        self.booktype_la.setText(_translate("Form", "图书类别："))
        self.search_btn.setText(_translate("Form", "搜索"))
        self.groupBox_2.setTitle(_translate("Form", "表单操作"))
        self.id_la.setText(_translate("Form", "编号："))
        self.bookname_la2.setText(_translate("Form", "图书名称："))
        self.sex_la.setText(_translate("Form", "作者性别："))
        self.price_la.setText(_translate("Form", "价格："))
        self.bookauthor_la2.setText(_translate("Form", "图书作者："))
        self.booktype_la2.setText(_translate("Form", "图书类别："))
        self.bookdesc.setText(_translate("Form", "描述："))
        self.modify_btn.setText(_translate("Form", "修改"))
        self.delete_btn.setText(_translate("Form", "删除"))
        self.man_rbtn.setText(_translate("Form", "男"))
        self.femal_rbtn.setText(_translate("Form", "女"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
