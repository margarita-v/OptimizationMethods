from Functions import choose_onedimen_func, choose_twodimen_func

from Methods import *

# Решение задачи методом одномерной оптимизации
def onedimen_solve(method_index, func_index, a, b, eps, x0):
    func = choose_onedimen_func(func_index)
    if method_index == 0:
        result = SegmentDivide.segment_divide(a, b, eps, func)
    elif method_index == 1:
        result = GoldenSection.golden_section(a, b, eps, func)
    elif method_index == 2:
        result = ParabolicMethod.parabolic_method(a, b, eps, func)
    else:
        result = NewtonMethod.newton_method(a, b, x0, eps, func)
    return result, func(result)

# Решение задачи методом многомерной оптимизации
def twodimen_solve(method_index, func_index, x, y, eps, alpha):
    func = choose_twodimen_func(func_index)
    if method_index == 0:
        x, y = SplittingOfStep.splitting_of_step(x, y, alpha, eps, func)
    else:
        x, y = FastestDescent.fastest_descent(x, y, alpha, eps, func)
    return x, y, func(x, y)
