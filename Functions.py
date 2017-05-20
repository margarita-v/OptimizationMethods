# -*- coding: utf-8 -*-
import numpy as np

ONEDIMEN_FUNCTIONS = [
        lambda x: x**4 - x**2,
        lambda x: np.cos(x + np.pi/2),
        lambda x: (x - 5)**2 + 8]
TWODIMEN_FUNCTIONS = [
        lambda x, y: 3*x*x + 4*y*y + 1,
        lambda x, y: 8*x*x + 4*x*y + 5*y*y,
        lambda x, y: 2*x*x + 2*y*y + 2*x*y + 2*x + 10*y + 10]
ONEDIMEN_TO_STR = [
        "f(x) = x*x*x*x - x*x",
        "f(x) = cos(x + pi/2)",
        "f(x) = (x - 5)^2 + 8"]
TWODIMEN_TO_STR = [
        "z = 3*x*x + 4*y*y + 1", 
        "z = 8*x*x + 4*x*y + 5*y*y",
        "z = 2*x*x + 2*y*y + 2*x*y + 2*x + 10*y + 10"]

def choose_onedimen_func(num):
    return ONEDIMEN_FUNCTIONS[num]

def onedimen_func_str():
    return ONEDIMEN_TO_STR

def choose_twodimen_func(num):
    return TWODIMEN_FUNCTIONS[num]

def twodimen_func_str():
    return TWODIMEN_TO_STR
