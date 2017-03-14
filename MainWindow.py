# -*- coding: utf-8 -*-

from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication

import os
import sys
import Functions
import SegmentDivide
import GoldenSection
            
class Window(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        uic.loadUi("mainwindow.ui", self)
        
        self.cbFunc.addItems(Functions.func_str())
        self.btnGraph.clicked.connect(self.get_plot)
        self.btnSolve.clicked.connect(self.get_solve)
        self.btnSolve.setDefault(True)

        self.dsbA.valueChanged.connect(self.paramsChanged)
        self.dsbB.valueChanged.connect(self.paramsChanged)
        self.dsbEps.valueChanged.connect(self.paramsChanged)
        
        self.a = self.dsbA.value()
        self.b = self.dsbB.value()
        self.eps = self.dsbEps.value()
        
        self.show()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()

    def paramsChanged(self):
        self.lblSolve.setText("")   

    def get_solve(self):
        if len(sys.argv) == 1:
            result = SegmentDivide.solve(self.a, self.b, self.eps)
        else:
            result = GoldenSection.solve(self.a, self.b, self.eps)
        self.lblSolve.setText("Решение задачи: " + format(result, 'f'))
    
    def get_plot(self):
        os.system("python DrawPlot.py")

app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())
