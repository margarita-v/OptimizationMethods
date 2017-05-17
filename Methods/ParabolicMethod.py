# -*- coding: utf-8 -*-

# заданная пользователем функция
func = None

# реализация метода парабол
def parabolic_method(a, b, x0, eps, F):
    global func
    func = F
    if a > b:
        a, b = b, a
    u1 = a
    u2 = (a + b) / 2
    u3 = b
    while u3 - u1 >= eps and u2 >= a and u2 <= b:
        d = parabolas_min(u1, u2, u3)
        I1 = func(u1)
        I2 = func(u2)
        I3 = func(u3)
        Imin = func(d)
        if d < u2:
            if Imin < I2:
                u3 = u2
                u2 = d
            elif Imin > I2:
                u1 = d
            else:
                if I1 > I2:
                    u3 = u2
                    u2 = d
                elif I2 > I3:
                    i1 = d
        elif d > u2:
            if Imin < I2:
                u1 = u2
                u2 = d
            elif Imin > I2:
                u3 = d
            else:
                if I3 > I2:
                    u1 = u2
                    u2 = d
                elif I1 > I2:
                    u3 = d
        else:
            if func(u2 - eps) < I2:
                u2 -= eps
            elif func(u2 + eps) < I2:
                u2 += eps
            else:
                break
    if u2 < a:
        return a
    if u2 > b:
        return b
    return u2

# вычисление точки минимума параболы,
# построенной через выпуклую тройку точек
def parabolas_min(u1, u2, u3):
    I1 = func(u1)
    I2 = func(u2)
    I3 = func(u3)
    return -0.5 * ((I2 - I1)*u3*u3 + (I1 - I3)*u2*u2 + (I3 - I2)*u1*u1) / \
            ((I1 - I2)*u3 + (I3 - I1)*u2 + (I2 - I3)*u1)
