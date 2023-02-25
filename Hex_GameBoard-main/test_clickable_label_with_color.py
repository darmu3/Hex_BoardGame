from PyQt5 import QtCore
from PyQt5.QtWidgets import QLabel, QApplication, QMainWindow

class W(QMainWindow):
    def __init__(self, *args):
        super().__init__()
        self.label = QLabel('')
        self.flag = True
        self.setCentralWidget(self.label)
        self.label.installEventFilter(self)
        self.label.setStyleSheet("min-width: 20px; min-height: 20px; border: 1px solid #444")

    def eventFilter(self, obj, e):
        if e.type() == 2:
            btn = e.button()
            if btn == 1:

                self.label.setStyleSheet("background-color: Red")
            elif btn == 2:
                
                self.label.setStyleSheet("background-color: Blue")
        return super(QMainWindow, self).eventFilter(obj, e)


app = QApplication([])
w = W()
w.show()
app.exec_()