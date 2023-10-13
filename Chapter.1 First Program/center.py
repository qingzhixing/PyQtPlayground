import sys
from PyQt6.QtWidgets import QWidget, QApplication


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(350, 250)
        self.moveCenter()
        self.setWindowTitle("Center")

    def moveCenter(self):
        frame = self.frameGeometry()
        centerPoint = self.screen().availableGeometry().center()
        frame.moveCenter(centerPoint)
        self.move(frame.topLeft())


def main():
    app = QApplication(sys.argv)
    exampleWidget = Example()
    exampleWidget.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
