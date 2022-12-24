# How to plot a simple graph using python?
# It can be done by using a module- matplotlib and its submodule pyplot

import matplotlib.pyplot as plt
import numpy as np

xaxis = np.array([2, 3, 5])
yaxis = np.array([0, 1, 6])

plt.plot(xaxis, yaxis)
plt.show()

# This is same as ploting (2,0), (3,1), (5,6) in a graph sheet