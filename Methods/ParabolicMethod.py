# -*- coding utf-8 -*-

# заданная пользователем функция
func = None

# реализация метода парабол
def parabolic_method(a, b, u0, h, eps, F):
    global func
    func = F
    i = 2

    # текущая тройка точек: t0, t1, t2
    t0 = u0
    t1 = t0 + h

    # список всех точек
    points = [t0, t1]
    # список значений функции во всех рассмотренных точках
    values = [func(t0), func(t1)]
    
    isConvex = False
    condition = True

    while condition:
        I0 = func(t0)
        I1 = func(t1)

        if I1 <= I0:
            t2 = t0 + h*(2 ** i)
        else:
            points.remove(t1)
            values.remove(I1)
            t1 = t0 - h
            I1 = func(t1)
            points.append(t1)
            values.append(I1)
            I0 = func(t0 + h)
            t2 = t0 - h*(2 ** i)

        I2 = func(t2)

        # если точки или значения функций стали близки с точностью eps, то процесс завершен
        stop = abs(t0 - t2) < eps or abs(I0 - I2) < eps:
        if stop:
            return t0

        # проверка принадлежности новой точки отрезку
        # если принадлежит, проверить, является ли текущая тройка точек выпуклой
        isConvex = is_convex(t0, t1, t2)
        condition = (t2 >= a) and (t2 <= b) and not isConvex
        if (condition):
            points.append(t2)
            values.append(I2)
            # переходим к следующей точке
            t0 = t1
            t1 = t2
            i = i + 1

    # если выпуклая тройка была найдена
    if condition:
        print(t0, ' ', t1, ' ', t2)
        return W(t0, t1, t2)
    else:
        # ни одна тройка не является выпуклой
        w = a if t2 < a else b
        points.append(w)
        values.append(func(w))

        In = min(values)
        index = values.index(In)
        Un = points[index]
        
        if abs(w - Un) < eps:
            return w

        print('w = ', w)
        #print('points = ', points)
        print('Un = ', Un)
        print()

        # уточняем минимум, уменьшаем шаг и продолжаем процесс
        return parabolic_method(a, b, Un, h / 2, eps, F)

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
