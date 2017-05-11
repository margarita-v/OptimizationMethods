from Functions import choose_onedimen_func, choose_twodimen_func

from Methods import *

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

def twodimen_solve(method_index, func_index, x, y, vector, eps, alpha):
    pass
