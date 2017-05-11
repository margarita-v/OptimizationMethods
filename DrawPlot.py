# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import sys
from Functions import choose_onedimen_func, choose_twodimen_func

if len(sys.argv) > 2:
    x_axis = np.linspace(-8, 8, 100)
    y_axis = np.linspace(-8, 8, 100)
    # номер выбранной функции получаем из аргумента командной строки
    if int(sys.argv[1]) == 1:
        func = choose_onedimen_func(int(sys.argv[2]))
        plt.plot(x_axis, func(x_axis), '-')
    else:
        func = choose_twodimen_func(int(sys.argv[2]))
        plt.plot(x_axis, func(x_axis, y_axis), '-')
    plt.grid(True)
    plt.show()
