# -*- coding: utf-8 -*-

from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication

import os
import sys
import Functions
from Methods.SegmentDivide import segment_divide
from Methods.GoldenSection import golden_section
from Methods.ParabolicMethod import parabolic_method
            
class Window(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        uic.loadUi("mainwindow.ui", self)
        
        self.cbFunc.addItems(Functions.func_str())
        self.cbFunc.currentIndexChanged.connect(self.funcSelection)
        
        self.cbMethod.addItems(["Метод деления отрезка пополам",
                "Метод золотого сечения", "Метод парабол"])
        self.cbMethod.currentIndexChanged.connect(self.methodSelection)

        self.btnGraph.clicked.connect(self.get_plot)
        self.btnSolve.clicked.connect(self.get_solve)
        self.btnSolve.setDefault(True)
        
        self.lblFirstPoint.setVisible(False)
        self.dsbFirstPoint.setVisible(False)

        self.dsbA.valueChanged.connect(self.paramsChanged)
        self.dsbB.valueChanged.connect(self.paramsChanged)
        self.dsbEps.valueChanged.connect(self.paramsChanged)
        
        self.a = self.dsbA.value()
        self.b = self.dsbB.value()
        self.eps = self.dsbEps.value()
        self.func_index = 0
        self.method_index = 0

        self.show()
    
    # выход из программы по нажатию Esc
    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()

    # событие изменения значений концов отрезка и точности eps
    def paramsChanged(self):
        self.a = self.dsbA.value()
        self.b = self.dsbB.value()
        self.eps = self.dsbEps.value()
        self.lblSolve.setText("")   
    
    # запоминаем номер выбранной пользователем функции
    def funcSelection(self, i):
        self.func_index = i
        self.lblSolve.setText("")   

    # запоминаем номер выбранного пользователем метода
    def methodSelection(self, i):
        self.method_index = i
        self.lblSolve.setText("")   
        self.lblFirstPoint.setVisible(i > 1)
        self.dsbFirstPoint.setVisible(i > 1)

    # решение задачи
    def get_solve(self):
        # по номеру получаем выбранную функцию и отправляем ее выбранному методу решения
        func = Functions.choose_func(self.func_index)
        if self.method_index == 0:
            result = segment_divide(self.a, self.b, self.eps, func)
        elif self.method_index == 1:
            result = golden_section(self.a, self.b, self.eps, func)
        else:
            result = parabolic_method(self.a, self.b, 
                    self.dsbFirstPoint.value(), (self.b - self.a) / 16, self.eps, func)
        self.lblSolve.setText("Решение задачи: " + format(result, 'f'))
    
    # построение графика выбранной функции
    def get_plot(self):
        os.system("python DrawPlot.py " + str(self.func_index))

app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())
