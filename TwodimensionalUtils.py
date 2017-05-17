# -*- coding: utf-8 -*-
from math import sqrt

# нахождение производной по x
def x_derivative(x, y, eps, func):
    return (func(x + eps, y) - func(x - eps, y)) / (2*eps)

# нахождение производной по y
def y_derivative(x, y, eps, func):
    return (func(x, y + eps) - func(x, y - eps)) / (2*eps)

# вычисление нормы
def norma(x, y, eps, func):
    return sqrt(x*x + y*y)
    #return sqrt(x_derivative(x, y, eps, func)**2 +
     #       y_derivative(x, y, eps, func)**2)
