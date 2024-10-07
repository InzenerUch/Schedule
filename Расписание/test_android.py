import sys
from PyQt6.QtWidgets import QApplication, QLabel

class MyApp(QApplication):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label = QLabel("Привет, мир!")
        self.setWindowTitle("Пример приложения")
        self.setCentralWidget(self.label)
        self.show()

if __name__ == "__main__":
    app = MyApp(sys.argv)
    sys.exit(app.exec())