# -*- coding: utf-8 -*-

from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication

import os
import sys
import Functions

from Methods.SegmentDivide   import segment_divide
from Methods.GoldenSection   import golden_section
from Methods.ParabolicMethod import parabolic_method
from Methods.NewtonMethod    import newton_method

METHODS = ["Метод деления отрезка пополам", "Метод золотого сечения",
        "Метод парабол", "Метод Ньютона"]

# Параметры для методов нахождения минимума функции
a = 0
b = 0
eps = 0
x0 = 0
# Номер выбранной пользователем функции
func_index = 0
# Номер выбранного пользователем метода
method_index = 0

class Window(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        uic.loadUi("mainwindow.ui", self)
        
        self.cbFunc.addItems(Functions.func_str())
        self.cbFunc.currentIndexChanged.connect(self.funcSelection)
        
        self.cbMethod.addItems(METHODS)
        self.cbMethod.currentIndexChanged.connect(self.methodSelection)

        self.btnGraph.clicked.connect(self.get_plot)
        self.btnSolve.clicked.connect(self.get_solve)
        self.btnSolve.setDefault(True)
        
        self.lblFirstPoint.setVisible(False)
        self.dsbFirstPoint.setVisible(False)

        self.dsbA.valueChanged.connect(self.paramsChanged)
        self.dsbB.valueChanged.connect(self.paramsChanged)
        self.dsbEps.valueChanged.connect(self.paramsChanged)
        self.dsbFirstPoint.valueChanged.connect(self.paramsChanged)
        
        global a, b, eps
        a = self.dsbA.value()
        b = self.dsbB.value()
        eps = self.dsbEps.value()

        self.show()
    
    # выход из программы по нажатию Esc
    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()

    # событие изменения значений концов отрезка и точности eps
    def paramsChanged(self):
        global a, b, eps, x0
        a = self.dsbA.value()
        self.dsbB.setMinimum(a)

        b = self.dsbB.value()
        self.dsbFirstPoint.setMinimum(a)
        self.dsbFirstPoint.setMaximum(b)

        eps = self.dsbEps.value()
        x0 = self.dsbFirstPoint.value()
        self.lblSolve.setText("")   
    
    # запоминаем номер выбранной пользователем функции
    def funcSelection(self, i):
        global func_index
        func_index = i
        self.lblSolve.setText("")   

    # запоминаем номер выбранного пользователем метода
    def methodSelection(self, i):
        global method_index
        method_index = i
        self.lblSolve.setText("")   
        self.lblFirstPoint.setVisible(i > 1)
        self.dsbFirstPoint.setVisible(i > 1)

    # решение задачи
    def get_solve(self):
        # по номеру получаем выбранную функцию и отправляем ее выбранному методу решения
        func = Functions.choose_func(func_index)
        if method_index == 0:
            result = segment_divide(a, b, eps, func)
        elif method_index == 1:
            result = golden_section(a, b, eps, func)
        elif method_index == 2:
            result = parabolic_method(a, b, x0, eps, func)
        else:
            result = newton_method(a, b, x0, eps, func)
        self.lblSolve.setText("Решение задачи:\n\n" + "x = " + format(result, 'f') + 
                "\n\nf(x) = " + format(func(result), 'f'))
    
    # построение графика выбранной функции
    def get_plot(self):
        os.system("python DrawPlot.py " + str(func_index))

app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())
