# -*- coding: utf-8 -*-

# Функции для методов одномерной оптимизации
def choose_onedimen_func(num):
    if num == 0:
        return lambda x: x*x*x - x
    if num == 1:
        return lambda x: x*x - 5*x
    return lambda x: (x - 5)**2 + 8

def onedimen_func_str():
    return ["f(x) = x*x*x - x", "f(x) = x*x - 5*x", "f(x) = (x - 5)^2 + 8"]

# Функции для методов многомерной оптимизации
def choose_twodimen_func(num):
    if num == 0:
        return lambda x, y: x*x + y*y
    return lambda x, y: (x - 4*y)**2 + 9

def twodimen_func_str():
    return ["f(x,y) = x^2 + y^2", "f(x,y) = (x - 4y)^2 + 9"]
