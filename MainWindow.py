# -*- coding: utf-8 -*-

from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication
import sys


class Window(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        uic.loadUi("mainwindow.ui", self)
        self.btnSolve.clicked.connect(self.get_solve)
        self.btnSolve.setDefault(True)
        
        self.dsbA.valueChanged.connect(self.paramsChanged)
        self.dsbB.valueChanged.connect(self.paramsChanged)
        self.dsbEps.valueChanged.connect(self.paramsChanged)

        self.show()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()

    def paramsChanged(self):
        self.lblSolve.setText("")

    @staticmethod
    def func(x):
        return x*x

    def get_solve(self):
        a = self.dsbA.value()
        b = self.dsbB.value()
        if a > b:
            a, b = b, a
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
