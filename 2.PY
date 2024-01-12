import matplotlib.pyplot as plt
import numpy as np


x = np.arange(-10, 10, 0.2)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tanh(x)

plt.plot(x, y1, label='sin(x)')
plt.plot(x, y2, label='cos(x)')
plt.plot(x, y3, label='tanh(x)')
plt.legend(loc='best')
plt.xlabel('Time')
plt.ylabel('Value')
plt.show()