# -*- coding: utf-8 -*-

from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication
import sys

import SegmentDivide
import GoldenSection
            
class Window(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        uic.loadUi("mainwindow.ui", self)
        
        if len(sys.argv) == 1:
            self.setWindowTitle("Метод деления отрезка пополам")
        else:
            self.setWindowTitle("Метод золотого сечения")

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

    def get_solve(self):
        a = self.dsbA.value()
        b = self.dsbB.value()
        eps = self.dsbEps.value()
        
        if len(sys.argv) == 1:
            result = SegmentDivide.solve(a, b, eps)
        else:
            result = GoldenSection.solve(a, b, eps)

        self.lblSolve.setText("Решение задачи: " + str(result))
    
app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())
