# -*- coding: utf-8 -*-
from TwodimensionalUtils import x_derivative, y_derivative, norma

# метод одномерной оптимизации
def segment_divide_help(x, y, eps, func):
    a = -10000
    b = 10000
    while (b - a) >= eps:
        delta = (b - a) / 16
        u1 = (b + a - delta) / 2
        u2 = (b + a + delta) / 2
        if help_func(x, y, u1, eps, func) < help_func(x, y, u2, eps, func):
            b = u2
        else:
            a = u1
    return (a + b) / 2

# вспомогательная функция, минимум которой требуется найти
def help_func(x, y, alpha, eps, func):
    return func(x - alpha * x_derivative(x, y, eps, func),
            y - alpha * y_derivative(x, y, eps, func))

# метод наискорейшего спуска
def fastest_descent(x, y, alpha, eps, func):
    gradX = x_derivative(x, y, eps, func)
    gradY = y_derivative(x, y, eps, func)
    while norma(gradX, gradY, eps, func) >= eps:
        alpha_new = segment_divide_help(x, y, eps, func)
        x -= alpha_new * gradX
        y -= alpha_new * gradY
        gradX = x_derivative(x, y, eps, func)
        gradY = y_derivative(x, y, eps, func)
    return x, y
