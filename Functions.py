# -*- coding: utf-8 -*-
from math import sin, cos, pi

# Функции для методов одномерной оптимизации
def choose_onedimen_func(num):
    if num == 0:
        return lambda x: x*x*x*x - x*x
    if num == 1:
        return lambda x: cos(x + pi/2)
    return lambda x: (x - 5)**2 + 8

def onedimen_func_str():
    return ["f(x) = x*x*x*x - x*x",
            "f(x) = cos(x + pi/2)",
            "f(x) = (x - 5)^2 + 8"]

# Функции для методов многомерной оптимизации
def choose_twodimen_func(num):
    if num == 0:
        return lambda x, y: (x*x + y*y, y)
    return lambda x, y: ((x - 4*y)**2 + 9, y)

def twodimen_func_str():
    return ["z = x^2 + y^2",
            "z = (x - 4y)^2 + 9"]
