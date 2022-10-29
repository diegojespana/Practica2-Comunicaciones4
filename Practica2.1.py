import matplotlib.pyplot as plt
import numpy as np

x = [0,1,2,3,4]
xi = [0,1,2,3,4]

h = [2,4,6,8,10]
hi = [0,1,2,3,4]

muestras_y = len(x) + len(h) - 1
inicio_y = min(hi) + min(xi)

n = np.arange(inicio_y, muestras_y, 1)

y = np.convolve(x,h)

plt.subplot(311)
plt.stem(xi,x)

plt.subplot(312)
plt.stem(hi,h)

plt.subplot(313)
plt.stem(n,y)

plt.show()

