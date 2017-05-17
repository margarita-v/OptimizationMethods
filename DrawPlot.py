# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import sys
from Functions import choose_onedimen_func

if len(sys.argv) > 1:
    x_axis = np.linspace(-8, 8, 100)
    # номер выбранной функции получаем из аргумента командной строки
    func = choose_onedimen_func(int(sys.argv[1]))
    plt.plot(x_axis, func(x_axis), '-')
    plt.grid(True)
    plt.show()
