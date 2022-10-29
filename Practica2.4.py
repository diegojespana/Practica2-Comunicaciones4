from signal import signal
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal
import scipy.interpolate

def sin_wave (f,fs,t):
    Ts = 1/fs
    n = t/Ts
    n = np.arange(n)
    y = np.sin(2*np.pi*f*n*Ts)
    return y



x = np.arange(0, 0.01, 1/8000)
fs = 8000
t = 0.01
hz_300 = sin_wave(f=300,fs=fs,t=t)

decimada = scipy.signal.decimate(hz_300, 2)
x_decimada = scipy.signal.decimate(x,2)

x2 = np.arange(0, 0.01, 1/32000)
interpolada = np.interp(x2, x, hz_300)

pq = 40
resampleada = scipy.signal.resample(hz_300, pq)
x3 = np.arange(0, 0.01, 1/(100*pq))

fig, (ax1, ax2, ax3, ax4) = plt.subplots(4)

ax1.stem(x, hz_300, 'b')
ax1.set_title("Funcion Original")

ax2.stem(x_decimada,decimada, 'r')
ax2.set_title("Funcion Decimada")

ax3.stem(x2, interpolada, 'g')
ax3.set_title("Funcion Interpolada")

""" print(len(hz_300)) """
ax4.stem(x3, resampleada)
ax4.set_title("Funcion Resampleada")

plt.show()