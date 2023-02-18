import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QLabel
from PyQt5.QtCore import Qt

class Example(QWidget):
    def setupUi(self, MainWindow):
        MainWindow.size()

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)

        names = ['1', '2', '3', '4', '5',
        '6', '7', '8', '9', '10',
        '11', '12', '13', '14', '15',
        '16', '17', '18', '19', '20']

        positions = [(i, j) for i in range(4) for j in range(5)]

        for position, name in zip(positions, names):
         if name == '':
          continue
         # button = QPushButton(name)
         grid.setSpacing(0)
         label = QLabel(self)
         label.setText(name)
         label.setStyleSheet("min-width: 30px; min-height: 30px; border: 1px solid #444")
         label.setAlignment(Qt.AlignCenter)
         # grid.addWidget(button, *position)
         grid.addWidget(label, *position)

        self.move(300, 150)
        self.setWindowTitle('PyQt window')
        self.show()

if __name__ == '__main__':
     app = QApplication(sys.argv)
     ex = Example()
     sys.exit(app.exec_())