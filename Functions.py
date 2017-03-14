from math import sin

def func(x, num):
    if num == 0:
        return x*x
    if num == 1:
        return x*x*x
    return sin(x)

def func_str():
    return ["f(x) = x*x", "f(x) = x^3", "f(x) = sin(x)"]
