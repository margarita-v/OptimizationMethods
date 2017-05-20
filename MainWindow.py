# -*- coding: utf-8 -*-

from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox

import os
import sys
from Solve import onedimen_solve, twodimen_solve
from Functions import onedimen_func_str, twodimen_func_str
from DrawPlot  import show_2D_plot, show_3D_plot

METHODS = [
        "Метод деления отрезка пополам",
        "Метод золотого сечения",
        "Метод парабол",
        "Метод Ньютона"]
METHODS_MULTIDIMENSIONAL = [
        "Метод дробления шага",
        "Метод наискорейшего спуска"]

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
        
        # Заполнение выпадающего списка доступных функций
        self.cbFunc.addItems(onedimen_func_str())
        self.cbFunc.currentIndexChanged.connect(self.funcSelection)
        
        # Заполнение выпадающего списка доступных методов
        self.cbMethod.addItems(METHODS)
        self.cbMethod.currentIndexChanged.connect(self.methodSelection)

        # Обработчики для кнопок
        self.btnGraph.clicked.connect(self.get_plot)
        self.btnSolve.clicked.connect(self.get_solve)
        self.btnSolve.setDefault(True)
        
        # Обработчик изменения значений входных параметров для методов
        self.dsbA.valueChanged.connect(self.paramsChanged)
        self.dsbB.valueChanged.connect(self.paramsChanged)
        self.dsbEps.valueChanged.connect(self.paramsChanged)
        # second tab
        self.dsbVectorX.valueChanged.connect(self.paramsChangedSecond)
        self.dsbVectorY.valueChanged.connect(self.paramsChangedSecond)
        self.dsbAlpha.valueChanged.connect(self.paramsChangedSecond)
        
        # Обработчик переключения между вкладками
        self.tabWidget.currentChanged.connect(self.onTabChanged)
        self.tabWidget.setCurrentIndex(0)
        self.onFirstTab = True

        # Параметры для одномерной оптимизации
        self.a = self.dsbA.value()
        self.b = self.dsbB.value()
        self.eps = self.dsbEps.value()

        # Параметры для многомерной оптимизации
        self.vectorX = self.dsbVectorX.value()
        self.vectorY = self.dsbVectorY.value()
        self.alpha = self.dsbAlpha.value()

        self.show()
    
    # выход из программы по нажатию Esc
    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            result = QMessageBox.question(self, "Подтверждение выхода", 
                    "Вы действительно хотите выйти?")
            if result == QMessageBox.Yes:
                self.close()

    # событие переключения между вкладками
    def onTabChanged(self, i):
        self.onFirstTab = i == 0
        self.cbFunc.clear()
        self.cbMethod.clear()
        if i == 0:
            self.cbFunc.addItems(onedimen_func_str())
            self.cbMethod.addItems(METHODS)
        else:
            self.cbFunc.addItems(twodimen_func_str())
            self.cbMethod.addItems(METHODS_MULTIDIMENSIONAL)
        self.clear_solve()

    # событие изменения значений параметров для методов одномерной оптимизации
    def paramsChanged(self):
        self.a = self.dsbA.value()
        self.dsbB.setMinimum(self.a)
        self.b = self.dsbB.value()
        self.eps = self.dsbEps.value()
        self.clear_solve()

    # событие изменения значений параметров для методов многомерной оптимизации
    def paramsChangedSecond(self):
        self.vectorX = self.dsbVectorX.value()
        self.vectorY = self.dsbVectorY.value()
        self.eps = self.dsbEps.value()
        self.alpha = self.dsbAlpha.value()
        self.clear_solve()
    
    # запоминаем номер выбранной пользователем функции
    def funcSelection(self, i):
        global func_index
        func_index = i
        self.clear_solve()

    # запоминаем номер выбранного пользователем метода
    def methodSelection(self, i):
        global method_index
        method_index = i
        self.clear_solve()

    # решение задачи
    def get_solve(self):
        if self.onFirstTab:
            point, value = onedimen_solve(method_index, func_index, 
                self.a, self.b, self.eps)
            message = "x = " + format(point, 'f') + \
                "\n\nf(x) = " + format(value, 'f')
        else:
            x, y, result = twodimen_solve(method_index, func_index,
                    self.vectorX, self.vectorY, self.eps, self.alpha)
            message = "x = " + format(x, 'f') + \
                    "\ny = " + format(y, 'f') + \
                    "\nz(x, y) = " + format(result, 'f')
        self.lblSolve.setText(message)
    
    # построение графика выбранной функции
    def get_plot(self):
        if self.onFirstTab:
            show_2D_plot(func_index)
        else:
            show_3D_plot(func_index)

    # очистка лейбла для вывода результата решения
    def clear_solve(self):
        self.lblSolve.setText("")

app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())
