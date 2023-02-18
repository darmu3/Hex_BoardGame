# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'game.ui'
#
# Created by: PyQt5 UI code generator 5.15.8
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(754, 588)
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255),stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255))\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(260, 50, 461, 91))
        font = QtGui.QFont()
        font.setFamily("Attentat")
        font.setPointSize(72)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color:none;")
        self.label.setObjectName("label")
        self.control = QtWidgets.QFrame(self.centralwidget)
        self.control.setGeometry(QtCore.QRect(40, 250, 681, 211))
        self.control.setStyleSheet("background-color: rgba(255, 255, 255, 30);\n"
"border: 2px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;")
        self.control.setObjectName("control")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.control)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.control)
        font = QtGui.QFont()
        font.setFamily("Orpheus")
        font.setPointSize(36)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
"color: black;\n"
"background-color: rgba(255,255,255, 30);\n"
"border: 2px solid rgba(255,255,255,40);\n"
"border-radius: 7px;\n"
"width:230px;\n"
"height: 50px\n"
"}\n"
"")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/icons/hexagon_FILL0_wght400_GRAD0_opsz48.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.control)
        font = QtGui.QFont()
        font.setFamily("Orpheus")
        font.setPointSize(36)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"color: black;\n"
"background-color: rgba(255,255,255, 30);\n"
"border: 2px solid rgba(255,255,255,40);\n"
"border-radius: 7px;\n"
"width:230px;\n"
"height: 50px\n"
"}\n"
"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/icons/settings_FILL0_wght400_GRAD0_opsz48.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.control)
        font = QtGui.QFont()
        font.setFamily("Orpheus")
        font.setPointSize(36)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"color: black;\n"
"background-color: rgba(255,255,255, 30);\n"
"border: 2px solid rgba(255,255,255,40);\n"
"border-radius: 7px;\n"
"width:230px;\n"
"height: 50px\n"
"}\n"
"")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/newPrefix/icons/menu_book_FILL0_wght400_GRAD0_opsz48.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "HEX"))
        self.label.setText(_translate("MainWindow", "HEX"))
        self.pushButton.setText(_translate("MainWindow", "Играть"))
        self.pushButton_2.setText(_translate("MainWindow", "Настройки"))
        self.pushButton_3.setText(_translate("MainWindow", "Правила"))
import res_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
