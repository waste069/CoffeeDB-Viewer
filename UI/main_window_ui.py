# Form implementation generated from reading ui file 'UI/main_window.ui'
#
# Created by: PyQt6 UI code generator 6.8.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(762, 506)
        self.tableWidget = QtWidgets.QTableWidget(parent=Form)
        self.tableWidget.setGeometry(QtCore.QRect(10, 150, 741, 341))
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(0)
        self.addButton = QtWidgets.QPushButton(parent=Form)
        self.addButton.setGeometry(QtCore.QRect(50, 20, 609, 23))
        self.addButton.setObjectName("addButton")
        self.editButton = QtWidgets.QPushButton(parent=Form)
        self.editButton.setGeometry(QtCore.QRect(50, 50, 609, 23))
        self.editButton.setObjectName("editButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.addButton.setText(_translate("Form", "Добавить"))
        self.editButton.setText(_translate("Form", "Редактировать"))