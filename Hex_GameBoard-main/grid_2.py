import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel


class Example(QWidget):
    def __init__(self):
        super().__init__()
        #     self.initUI()
        #
        # def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)

        colors = {0: 'White', 1: 'Blue', 2: 'Green'}

        color_map = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                     0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0,
                     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                     0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0,
                     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        positions = [(i, j) for i in range(1, 12) for j in range(1, 12)]

        for position, color_map in zip(positions, color_map):
            grid.setSpacing(0)
            label = QLabel(self)
            label.setObjectName(f'{position[0]}_{position[1]}')
            label.setText(f'{position[0]}:{position[1]}')
            label.setStyleSheet(f'min-width: 50px; '
                                f'min-height: 50px; '
                                f'border: 1px solid #444; '
                                f'background-color: {colors[color_map]}')
            label.setAlignment(Qt.AlignCenter)
            grid.addWidget(label, *position)

        self.move(350, 150)
        self.setWindowTitle('Board')
        self.show()

        label2 = self.findChild(QLabel, '5_5')
        print(label2.text())
        col = f'min-width: 50px; ' f'min-height: 50px; ' f'border: 1px solid #444; ' f'background-color: {colors[0]}'
        if label2.styleSheet() == col:
            print(f'{colors[0]}')
        col2 = f'min-width: 50px; ' f'min-height: 50px; ' f'border: 1px solid #444; ' f'background-color: {colors[1]}'
        if label2.styleSheet() == col2:
            print(f'{colors[1]}')
        col3 = f'min-width: 50px; ' f'min-height: 50px; ' f'border: 1px solid #444; ' f'background-color: {colors[2]}'
        if label2.styleSheet() == col3:
            print(f'{colors[2]}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
