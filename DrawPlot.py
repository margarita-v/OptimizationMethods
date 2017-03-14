import numpy as np
import matplotlib.pyplot as plt
import Functions
import sys

if len(sys.argv) > 1:
    func = Functions.choose_func(int(sys.argv[1]))
    x_axis = np.linspace(-5, 5, 100)
    plt.plot(x_axis, func(x_axis), '-')
    plt.show()
