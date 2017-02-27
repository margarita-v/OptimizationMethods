from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
import sys


class Window(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        uic.loadUi("mainwindow.ui", self)
        self.btnSolve.clicked.connect(self.get_solve)
        self.show()

    def get_solve(self):
        self.lblSolve.setText("gfjhgjfg")

app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())
