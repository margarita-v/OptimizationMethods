import numpy as np
import matplotlib.pyplot as plt

from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.ticker import LinearLocator, FormatStrFormatter

from Functions import choose_onedimen_func, choose_twodimen_func

def show_2D_plot(func_index):
    x_axis = np.linspace(-8, 8, 100)
    func = choose_onedimen_func(func_index)
    plt.plot(x_axis, func(x_axis), '-')
    plt.grid(True)
    plt.show()

def show_3D_plot(func_index):
    fig = plt.figure()
    ax = fig.gca(projection='3d')

    X = np.arange(-1, 1, 0.25)
    Y = np.arange(-1, 1, 0.25)
    X, Y = np.meshgrid(X, Y)
    func = choose_twodimen_func(func_index)

    surf = ax.plot_surface(X, Y, func(X, Y), cmap=cm.coolwarm)
    ax.set_zlim(-10, 10)
    ax.zaxis.set_major_locator(LinearLocator(10))
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
    fig.colorbar(surf, shrink=0.5, aspect=5)
    plt.show()
