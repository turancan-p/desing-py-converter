# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:/Users/TuranCan/Desktop/conventer_menu.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(420, 330)
        MainWindow.setMinimumSize(QtCore.QSize(420, 330))
        MainWindow.setMaximumSize(QtCore.QSize(420, 330))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(10)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 121, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 120, 151, 31))
        self.label_2.setObjectName("label_2")
        self.ui_path_textbox = QtWidgets.QLineEdit(self.centralwidget)
        self.ui_path_textbox.setGeometry(QtCore.QRect(20, 50, 240, 22))
        self.ui_path_textbox.setObjectName("ui_path_textbox")
        self.py_path_textbox = QtWidgets.QLineEdit(self.centralwidget)
        self.py_path_textbox.setGeometry(QtCore.QRect(20, 160, 240, 22))
        self.py_path_textbox.setObjectName("py_path_textbox")
        self.select_ui_path_button = QtWidgets.QPushButton(self.centralwidget)
        self.select_ui_path_button.setGeometry(QtCore.QRect(290, 20, 105, 51))
        self.select_ui_path_button.setObjectName("select_ui_path_button")
        self.select_py_path_button = QtWidgets.QPushButton(self.centralwidget)
        self.select_py_path_button.setGeometry(QtCore.QRect(290, 130, 105, 51))
        self.select_py_path_button.setObjectName("select_py_path_button")
        self.convert_button = QtWidgets.QPushButton(self.centralwidget)
        self.convert_button.setGeometry(QtCore.QRect(140, 220, 131, 50))
        self.convert_button.setObjectName("convert_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Conventer"))
        self.label.setText(_translate("MainWindow", "Design file path (.ui)"))
        self.label_2.setText(_translate("MainWindow", "Converted file path (.py)"))
        self.select_ui_path_button.setText(_translate("MainWindow", "Select .ui Path"))
        self.select_py_path_button.setText(_translate("MainWindow", "Select Save Path"))
        self.convert_button.setText(_translate("MainWindow", "Convert .ui to .py"))

