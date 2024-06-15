# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'booktypeadd.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(487, 376)
        self.formLayoutWidget = QtWidgets.QWidget(Form)
        self.formLayoutWidget.setGeometry(QtCore.QRect(30, 50, 431, 241))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(20, 20, 20, 20)
        self.formLayout.setHorizontalSpacing(10)
        self.formLayout.setVerticalSpacing(20)
        self.formLayout.setObjectName("formLayout")
        self.book_type_name_la = QtWidgets.QLabel(self.formLayoutWidget)
        self.book_type_name_la.setObjectName("book_type_name_la")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.book_type_name_la)
        self.book_type_desc_la = QtWidgets.QLabel(self.formLayoutWidget)
        self.book_type_desc_la.setObjectName("book_type_desc_la")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.book_type_desc_la)
        self.book_type_name_le = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.book_type_name_le.setObjectName("book_type_name_le")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.book_type_name_le)
        self.book_type_desc_pte = QtWidgets.QPlainTextEdit(self.formLayoutWidget)
        self.book_type_desc_pte.setObjectName("book_type_desc_pte")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.book_type_desc_pte)
        self.add_btn = QtWidgets.QPushButton(Form)
        self.add_btn.setGeometry(QtCore.QRect(70, 320, 93, 28))
        self.add_btn.setObjectName("add_btn")
        self.reset_btn = QtWidgets.QPushButton(Form)
        self.reset_btn.setGeometry(QtCore.QRect(300, 320, 93, 28))
        self.reset_btn.setObjectName("reset_btn")

        self.retranslateUi(Form)
        self.reset_btn.clicked.connect(Form.reset) # type: ignore
        self.add_btn.clicked.connect(Form.add) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "图书类别名称"))
        self.book_type_name_la.setText(_translate("Form", "图书类别名称"))
        self.book_type_desc_la.setText(_translate("Form", "图书类别描述"))
        self.add_btn.setText(_translate("Form", "添加"))
        self.reset_btn.setText(_translate("Form", "重置"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())