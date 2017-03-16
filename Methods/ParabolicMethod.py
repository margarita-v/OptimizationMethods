# -*- coding utf-8 -*-

# заданная пользователем функция
func = None

# реализация метода парабол
def parabolic_method(a, b, u0, F):
    global func
    func = F
    h = (b - a) / 16
    i = 2

    # текущая тройка точек: t0, t1, t2
    t0 = u0
    t1 = t0 + h
    
    while True:
        I0 = func(t0)
        I1 = func(t1)

        if I1 <= I0:
            t2 = t0 + h*(2 ** i)
            I2 = func(t2)
        else:
            t1 = t0 - h
            I0 = func(t0 + h)
            t2 = t0 - h*(2 ** i)

        # проверка принадлежности новой точки отрезку
        # если принадлежит, проверить, является ли текущая тройка точек t0, t1, t2 выпуклой
        if (t2 >= a) and (t2 <= b) and not is_convex(t0, t1, t2):
            # переходим к следующей точке
            t0 = t1
            t1 = t2
            i = i + 1
        else:
            break

    # если выпуклая тройка была найдена
    if is_convex(t0, t1, t2):
        return W(t0, t1, t2)
    else:
        # ни одна тройка не является выпуклой
        return a

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
