# -*- coding: utf-8 -*-
import numpy as np

# Функции для методов одномерной оптимизации
def choose_onedimen_func(num):
    if num == 0:
        return lambda x: x*x*x*x - x*x
    return lambda x: (x - 5)**2 + 8

def onedimen_func_str():
    return ["f(x) = x*x*x*x - x*x",
            "f(x) = (x - 5)^2 + 8"]

# Функции для методов многомерной оптимизации
def choose_twodimen_func(num):
    if num == 0:
        return lambda x, y: 3*x*x + 4*y*y + 1
    return lambda x, y: 2*x*x + 2*y*y + 2*x*y + 2*x + 10*y + 10

def twodimen_func_str():
    return ["z = 3*x*x + 4*y*y + 1", 
            "z = 2*x*x + 2*y*y + 2*x*y + 2*x + 10*y + 10"]
