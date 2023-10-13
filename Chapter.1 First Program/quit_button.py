import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QToolTip
from PyQt6.QtGui import QFont


class ExampleWidget(QWidget):
    # 构造函数
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont("SansSerif", 10))

        btn = QPushButton("Quit", self)
        btn.setToolTip("Click to <b>Quit</b>")
        btn.clicked.connect(QApplication.instance().quit)
        # 给按钮一个系统建议尺寸
        btn.resize(btn.sizeHint())
        btn.move(50, 50)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle("Quit Button")


def main():
    app = QApplication(sys.argv)
    exampleWidget = ExampleWidget()
    exampleWidget.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
