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
        self.setToolTip("This is a <b>QWidget</b> widget")

        btn = QPushButton("Button", self)
        btn.setToolTip("This is a <b>QPushButton</b> widget")
        # 给按钮一个系统建议尺寸
        btn.resize(btn.sizeHint())
        btn.move(50, 50)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle("ToolTips")


def main():
    app = QApplication(sys.argv)
    exampleWidget = ExampleWidget()
    exampleWidget.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
