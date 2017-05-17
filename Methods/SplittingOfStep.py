# -*- coding: utf-8 -*-
from TwodimensionalUtils import x_derivative, y_derivative, norma

# метод дробления шага
def splitting_of_step(x0, y0, alpha, eps, func):
    I0 = func(x0, y0)
    gradX = x_derivative(x0, y0, eps, func)
    gradY = y_derivative(x0, y0, eps, func)
    while norma(gradX, gradY, eps, func) >= eps:
        x1 = x0 - alpha * gradX
        y1 = y0 - alpha * gradY
        I1 = func(x1, y1)
        if I1 < I0:
            x0 = x1
            y0 = y1
            I0 = I1
        else:
            alpha /= 2
        gradX = x_derivative(x0, y0, eps, func)
        gradY = y_derivative(x0, y0, eps, func)
    return x0, y0
