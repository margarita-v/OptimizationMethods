# -*- coding: utf-8 -*-

from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication

import os
import sys
from Solve import onedimen_solve, twodimen_solve
from Functions import onedimen_func_str, twodimen_func_str

METHODS = ["Метод деления отрезка пополам", "Метод золотого сечения",
        "Метод парабол", "Метод Ньютона"]
METHODS_MULTIDIMENSIONAL = ["Метод дробления шага", "Метод наискорейшего спуска"]

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
        # second tab
        self.cbFuncSecond.addItems(twodimen_func_str())
        self.cbFuncSecond.currentIndexChanged.connect(self.funcSelection)
        
        # Заполнение выпадающего списка доступных методов
        self.cbMethod.addItems(METHODS)
        self.cbMethod.currentIndexChanged.connect(self.methodSelection)
        # second tab
        self.cbMethodSecond.addItems(METHODS_MULTIDIMENSIONAL)
        self.cbMethodSecond.currentIndexChanged.connect(self.methodSelection)

        # Обработчики для кнопок
        self.btnGraph.clicked.connect(self.get_plot)
        self.btnSolve.clicked.connect(self.get_solve)
        self.btnSolve.setDefault(True)
        # second tab
        #self.btnSolveSecond.clicked.connect(self.get_solve)
        self.btnSolveSecond.setDefault(True)
        
        self.lblFirstPoint.setVisible(False)
        self.dsbFirstPoint.setVisible(False)

        # Обработчик изменения значений входных параметров для методов
        self.dsbA.valueChanged.connect(self.paramsChanged)
        self.dsbB.valueChanged.connect(self.paramsChanged)
        self.dsbEps.valueChanged.connect(self.paramsChanged)
        self.dsbFirstPoint.valueChanged.connect(self.paramsChanged)
        # second tab
        self.dsbX1.valueChanged.connect(self.paramsChangedSecond)
        self.dsbX2.valueChanged.connect(self.paramsChangedSecond)
        self.dsbY1.valueChanged.connect(self.paramsChangedSecond)
        self.dsbY2.valueChanged.connect(self.paramsChangedSecond)
        self.dsbVectorX.valueChanged.connect(self.paramsChangedSecond)
        self.dsbVectorY.valueChanged.connect(self.paramsChangedSecond)
        self.dsbEpsSecond.valueChanged.connect(self.paramsChangedSecond)
        self.dsbAlpha.valueChanged.connect(self.paramsChangedSecond)
        
        # Обработчик переключения между вкладками
        self.tabWidget.currentChanged.connect(self.onTabChanged)
        self.tabWidget.setCurrentIndex(0)

        # Параметры для одномерной оптимизации
        self.a = self.dsbA.value()
        self.b = self.dsbB.value()
        self.eps = self.dsbEps.value()
        self.x0 = self.dsbFirstPoint.value()

        # Параметры для многомерной оптимизации
        self.x1 = self.dsbX1.value()
        self.x2 = self.dsbX2.value()
        self.y1 = self.dsbY1.value()
        self.y2 = self.dsbY2.value()
        self.vectorX = self.dsbVectorX.value()
        self.vectorY = self.dsbVectorY.value()
        self.alpha = self.dsbAlpha.value()

        self.show()
    
    # выход из программы по нажатию Esc
    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()

    # событие переключения между вкладками
    def onTabChanged(self, i):
        self.eps = self.dsbEps.value() if i == 0 else self.dsbEpsSecond.value()

    # событие изменения значений параметров для методов одномерной оптимизации
    def paramsChanged(self):
        self.a = self.dsbA.value()
        self.dsbB.setMinimum(self.a)

        self.b = self.dsbB.value()
        self.dsbFirstPoint.setMinimum(self.a)
        self.dsbFirstPoint.setMaximum(self.b)

        self.eps = self.dsbEps.value()
        self.x0 = self.dsbFirstPoint.value()
        self.lblSolve.setText("")   

    # событие изменения значений параметров для методов многомерной оптимизации
    def paramsChangedSecond(self):
        self.x1 = self.dsbX1.value()
        self.dsbX2.setMinimum(self.x1)

        self.y1 = self.dsbY1.value()
        self.dsbY2.setMinimum(self.y1)

        self.x2 = self.dsbX2.value()
        self.y2 = self.dsbY2.value()
        
        self.dsbVectorX.setMinimum(self.x1)
        self.dsbVectorX.setMaximum(self.x2)
        self.dsbVectorY.setMinimum(self.y1)
        self.dsbVectorY.setMaximum(self.y2)

        self.eps = self.dsbEpsSecond.value()
        self.alpha = self.dsbAlpha.value()
        self.lblSolveSecond.setText("")
    
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
        onFirstTab = self.tabWidget.currentIndex() == 0
        
        point, value = onedimen_solve(method_index, func_index, 
                self.a, self.b, self.eps, self.x0)
        message = "Решение задачи:\n\n" + "x = " + format(point, 'f') + \
                "\n\nf(x) = " + format(value, 'f')
        if onFirstTab:
            self.lblSolve.setText(message)
        else:
            self.lblSolveSecond.setText(message)
    
    # построение графика выбранной функции
    def get_plot(self):
        os.system("python DrawPlot.py " + str(func_index))

app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())
