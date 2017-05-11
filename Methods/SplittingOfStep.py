# -*- coding: utf-8 -*-
from math import sqrt

# заданная пользователем функция
func = None
# точность решения
eps = 0

# нахождение производной по x
def x_derivative(x, y):
    return (func(x + eps, y) - func(x - eps, y)) / (2*eps)

# нахождение производной по y
def y_derivative(x, y):
    return (func(x, y + eps) - func(x, y - eps)) / (2*eps)

# вычисление нормы
def norma(x, y):
    return sqrt(x_derivative(x, y)**2 + y_derivative(x, y)**2)

# метод дробления шага
def splitting_of_step(x0, y0, alpha, Eps, F):
    global func, eps
    func = F
    eps = Eps

    I0 = func(x0, y0)
    calcNextPoint = False
    while True:
        # шаг 2: посчитать градиент и проверить критерий остановки
        if not calcNextPoint:
            gradX = x_derivative(x0, y0)
            gradY = y_derivative(x0, y0)
            if norma(gradX, gradY) < eps:
                return x0, y0
        # шаг 3: посчитать следующую точку
        x1 = x0 - alpha * gradX
        y1 = y0 - alpha * gradY
        I1 = func(x1, y1)
        if I1 < I0:
            x0 = x1
            y0 = y1
            I0 = I1
            # перейти к шагу 2
            calcNextPoint = False
        else:
            alpha /= 2
            # перейти к шагу 3
            calcNextPoint = True
    return x0, y0
