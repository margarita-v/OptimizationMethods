# -*- coding: utf-8 -*-

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
    
    @staticmethod
    def func(x):
        return x*x

    def get_solve(self):
        a = self.dsbA.value()
        b = self.dsbB.value()
        eps = self.dsbEps.value()

        curA = a
        curB = b

        while True:
            delta = (curB - curA) / 4
            u1 = (curB + curA - delta) / 2
            u2 = (curB + curA + delta) / 2

            if self.func(u1) <= self.func(u2):
                curB = u2
            else:
                curA = u1
            
            # условие прекращения цикла
            if not abs(curB - curA) >= eps:
                break

        self.lblSolve.setText("Решение задачи: " + str(curA))
    
app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())
