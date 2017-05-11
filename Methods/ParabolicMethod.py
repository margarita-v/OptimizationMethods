# -*- coding: utf-8 -*-

# заданная пользователем функция
func = None

# реализация метода парабол
def parabolic_method(a, b, eps, F):
    global func
    func = F
    if a > b:
        a, b = b, a
    i = 1
    h = (b - a) / 16

    u0 = u1 = a + (b - a) / 2
    u2 = u0 + h

    I0 = func(u0)
    I2 = func(u2)
    if I0 < I2:
        minU = u0
        minF = I0
    else:
        minU = u2
        minF = I2
    isInSegment = True
    
    while isInSegment:
        u0 = u1
        u1 = u2

        I0 = func(u0)
        I1 = func(u1)

        if I1 <= I0:
            u2 = u0 + h*(2 ** i)
        else:
            u1 = u0 - h
            I0 = I1
            #I1 = func(u1)
            u2 = u0 - h*(2 ** i)
        I2 = func(u2)

        # если выпуклая тройка найдена
        if is_convex(u0, u1, u2):
            return W(u0, u1, u2)
        
        if I2 < minF:
            minF = I2
            minU = u2
        
        isInSegment = (u2 >= a) and (u2 <= b)

    if isInSegment:
        return W(u0, u1, u2)

    u0 = u1
    u1 = u2
    u2 = a if abs(a - u2) < abs (b - u2) else b
    if func(u2) < minF:
        return u2
    return minU

# проверка, является ли тройка точек выпуклой для заданной функции
def is_convex(u1, u2, u3):
    d1 = func(u1) - func(u2)
    d2 = func(u3) - func(u2)
    return d1 >= 0 and d2 >= 0 and d1 + d2 > 0

# вычисление точки минимума параболы,
# построенной через выпуклую тройку точек
def W(u1, u2, u3):
    I1 = func(u1)
    I2 = func(u2)
    I3 = func(u3)
    return -0.5 * ((I2 - I1)*u3*u3 + (I1 - I3)*u2*u2 + (I3 - I2)*u1*u1) / \
            ((I1 - I2)*u3 + (I3 - I1)*u2 + (I2 - I3)*u1)
