import sys
from PyQt6.QtWidgets import QApplication, QWidget, QMessageBox


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 350, 200)
        self.setWindowTitle("Message Box")

    def closeEvent(self, event):
        reply = QMessageBox.question(self, "Message", "Are U sure to quit?",
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.Yes:
            event.accept()
        else:
            event.ignore()


def main():
    app = QApplication(sys.argv)
    example = Example()
    example.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
