# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindowKursacha.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 600)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 600))
        MainWindow.setMaximumSize(QtCore.QSize(1000, 600))
        MainWindow.setSizeIncrement(QtCore.QSize(1000, 800))
        MainWindow.setBaseSize(QtCore.QSize(1000, 600))
        MainWindow.setStyleSheet("\n"
"\n"
"background-color: rgb(0, 255, 0);\n"
"font: 75 12pt \"Fixedsys\";\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.AccidentsBtn = QtWidgets.QPushButton(self.centralwidget)
        self.AccidentsBtn.setGeometry(QtCore.QRect(20, 10, 111, 31))
        self.AccidentsBtn.setStyleSheet("background-color: rgb(255, 207, 64);\n"
"")
        self.AccidentsBtn.setObjectName("AccidentsBtn")
        self.DriversBtn = QtWidgets.QPushButton(self.centralwidget)
        self.DriversBtn.setGeometry(QtCore.QRect(20, 50, 111, 31))
        self.DriversBtn.setStyleSheet("background-color: rgb(255, 207, 64);\n"
"")
        self.DriversBtn.setObjectName("DriversBtn")
        self.FuelBtn = QtWidgets.QPushButton(self.centralwidget)
        self.FuelBtn.setGeometry(QtCore.QRect(20, 90, 111, 31))
        self.FuelBtn.setStyleSheet("background-color: rgb(255, 207, 64);\n"
"")
        self.FuelBtn.setObjectName("FuelBtn")
        self.InspectionsBtn = QtWidgets.QPushButton(self.centralwidget)
        self.InspectionsBtn.setGeometry(QtCore.QRect(20, 130, 111, 31))
        self.InspectionsBtn.setStyleSheet("background-color: rgb(255, 207, 64);\n"
"")
        self.InspectionsBtn.setObjectName("InspectionsBtn")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Vehicles"))
        self.AccidentsBtn.setText(_translate("MainWindow", "Раписание"))
        self.DriversBtn.setText(_translate("MainWindow", "Доктор"))
        self.FuelBtn.setText(_translate("MainWindow", "Пациент"))
        self.InspectionsBtn.setText(_translate("MainWindow", "Прием"))