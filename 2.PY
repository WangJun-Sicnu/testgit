import matplotlib.pyplot as plt
import numpy as np


x = np.arange(-10, 10, 0.2)
y = np.sin(x)

plt.plot(x, y)
plt.show()