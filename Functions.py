def choose_func(num):
    if num == 0:
        return lambda x: x*x
    if num == 1:
        return lambda x: x*x*x
    return lambda x: (x + 2)**2 - 2

def func_str():
    return ["f(x) = x*x", "f(x) = x^3", "f(x) = (x + 2)^2 - 2"]
