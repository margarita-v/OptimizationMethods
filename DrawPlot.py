import numpy as np
import matplotlib.pyplot as plt
import sys
import SegmentDivide

x_axis = np.linspace(-5, 5, 100)
plt.plot(x_axis, SegmentDivide.func(x_axis), '-')
plt.show()
