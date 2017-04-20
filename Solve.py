from Functions import choose_onedimen_func, choose_twodimen_func

from Methods.SegmentDivide   import segment_divide
from Methods.GoldenSection   import golden_section
from Methods.ParabolicMethod import parabolic_method
from Methods.NewtonMethod    import newton_method

def onedimen_solve(method_index, func_index, a, b, eps, x0):
    func = choose_onedimen_func(func_index)
    if method_index == 0:
        result = segment_divide(a, b, eps, func)
    elif method_index == 1:
        result = golden_section(a, b, eps, func)
    elif method_index == 2:
        result = parabolic_method(a, b, x0, eps, func)
    else:
        result = newton_method(a, b, x0, eps, func)
    return result, func(result)

def twodimen_solve(method_index, func_index, x, y, vector, eps, alpha):
    pass
