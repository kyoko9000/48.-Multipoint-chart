"""
source:
https://www.w3schools.com/python/matplotlib_plotting.asp
"""
import sys
# pip install pyqt5
from PyQt5.QtWidgets import QApplication, QMainWindow
from code_handle import show_chart
from gui import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # the way app working
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)

        # khai bao nut an
        self.uic.Button_start_1.clicked.connect(self.show_diagram)

        self.index = "you can send data here"

    def show_diagram(self):
        if self.uic.screen.isEmpty():
            self.uic.screen.addWidget(show_chart(self.index))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())