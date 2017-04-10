# -*- coding utf-8 -*-

# заданная пользователем функция
func = None

# реализация метода парабол
def parabolic_method(a, b, u0, eps, F):
    global func
    func = F
    if a > b:
        a, b = b, a
    i = 2
    h = (b - a) / 16

    # текущая тройка точек: t0, t1, t2
    t0 = u0
    t1 = t0 + h
    
    while True:
        I0 = func(t0)
        I1 = func(t1)

        if I1 <= I0:
            t2 = t0 + h*(2 ** i)
        else:
            t1 = t0 - h
            I0 = I1
            t2 = t0 - h*(2 ** i)
        
        I1 = func(t1)
        I2 = func(t2)

        # если точки или значения функций стали близки с точностью eps, то процесс завершен
        stop = check(t0, t2, eps) and check(t1, t2, eps) and check(t0, t2, eps) or \
                check(I0, I1, eps) and check(I1, I2, eps) and check(I0, I2, eps)
        if stop:
            return t0

        # проверка принадлежности новой точки отрезку
        if (t2 >= a) and (t2 <= b):
            # если принадлежит, проверить, является ли текущая тройка точек выпуклой
            if not is_convex(t0, t1, t2):
                # переходим к следующей точке
                t0 = t2
                t1 = t2 + h
                i = i + 1
            else:
                # найдена выпуклая тройка
                return W(t0, t1, t2)
        else:
            # выпуклая тройка не найдена
            # меняем начальную точку и уточняем точку минимума
            w = a if t2 < a else b
            
            points = [t0, t1, w]
            values = [I0, I1, func(w)]
            
            In = min(values)
            index = values.index(In)
            Un = points[index]

            if Un < a or Un > b or abs(w - Un) < eps:
                return w

            h = h / 2
            i = 2
            t0 = Un
            t1 = t0 + h

def check(x, y, eps):
    return abs(x - y) < eps

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
