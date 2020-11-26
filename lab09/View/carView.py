# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'example_car_mvc.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from Controller.CarController import CarController
from Model.Car import Car

class Ui_MainWindow(object):
    def initSubClasses(self):
        self.C = Car()
        self.controller = CarController()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 562)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(520, 20, 256, 481))
        self.listWidget.setObjectName("listWidget")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(80, 50, 281, 51))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.plainTextEdit.setPlainText("valami");
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(80, 130, 281, 51))
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.plainTextEdit_3 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_3.setGeometry(QtCore.QRect(80, 210, 281, 51))
        self.plainTextEdit_3.setObjectName("plainTextEdit_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 70, 47, 13))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 150, 47, 13))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 230, 47, 13))
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(70, 340, 111, 71))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(250, 340, 111, 71))
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "típus"))
        self.label_2.setText(_translate("MainWindow", "rendszam"))
        self.label_3.setText(_translate("MainWindow", "evjarat"))
        self.pushButton.setText(_translate("MainWindow", "Mentes"))
        self.pushButton_2.setText(_translate("MainWindow", "Olvasas"))

    def configureConnections(self):
        self.pushButton.clicked.connect(self.storeParameters)
        self.pushButton_2.clicked.connect(self.readParameters)

    def readParameters(self):
        element = self.controller.readCarParameters(self.C)
        itemResult = QtWidgets.QListWidgetItem(element)
        self.listWidget.addItem(itemResult)

    def storeParameters(self):
        self.controller.storeCarParameters(self.C,self.plainTextEdit.toPlainText(),
                                    self.plainTextEdit_2.toPlainText(),
                                    self.plainTextEdit_3.toPlainText()
                                    )



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.configureConnections()
    ui.initSubClasses()
    MainWindow.show()
    sys.exit(app.exec_())