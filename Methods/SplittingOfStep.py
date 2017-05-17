# -*- coding: utf-8 -*-
from TwodimensionalUtils import x_derivative, y_derivative, norma

# метод дробления шага
def splitting_of_step(x0, y0, alpha, eps, func):
    I0 = func(x0, y0)
    calcNextPoint = False
    while True:
        # шаг 2: посчитать градиент и проверить критерий остановки
        if not calcNextPoint:
            gradX = x_derivative(x0, y0, eps, func)
            gradY = y_derivative(x0, y0, eps, func)
            if norma(gradX, gradY, eps, func) < eps:
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
