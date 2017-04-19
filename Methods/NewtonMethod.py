# -*- coding: utf-8 -*-

# Нахождение первой производной функции
def first_derivative(F, x, h):
    return (F(x + h) - F(x)) / h

# Нахождение второй производной функции
def second_derivative(F, x, h):
    return (F(x + h) - 2*F(x) + F(x - h)) / (h**2)

# Нахождение минимума функции методом Ньютона
def newton_method(a, b, u0, eps, F):
    while (abs(first_derivative(F, u0, eps)) >= eps and u0 >= a and u0 <= b):
        u0 -= first_derivative(F, u0, eps) / second_derivative(F, u0, eps)
    if (u0 >= a and u0 <= b):
        return u0
    return a if u0 <= a else b
