import numpy as np
import matplotlib.pyplot as plt

def sin_wave (f,fs,t):
    Ts = 1/fs
    n = t/Ts
    n = np.arange(n)
    y = np.sin(2*np.pi*f*n*Ts)
    return y

inciso = input('Ingresar a para mostrar inciso a. Ingresar b para mostrar inciso b: ')

if inciso == 'a':
    fs = 8000
    t = 0.01

    x = np.arange(0, 0.01, 1/8000)

    hz_100 = sin_wave(f=100,fs=fs,t=t)
    hz_225 = sin_wave(f=225,fs=fs,t=t)
    hz_350 = sin_wave(f=350,fs=fs,t=t)
    hz_475 = sin_wave(f=475,fs=fs,t=t)

    markerline1, stemlines, _ = plt.stem(x, hz_100, 'b')
    plt.setp(markerline1, 'markerfacecolor', 'b')

    markerline2, stemlines, _ = plt.stem(x, hz_225, 'r')
    plt.setp(markerline2, 'markerfacecolor', 'r')

    markerline3, stemlines, _ = plt.stem(x, hz_350, 'g')
    plt.setp(markerline1, 'markerfacecolor', 'g')

    markerline4, stemlines, _ = plt.stem(x, hz_475, 'k')
    plt.setp(markerline4, 'markerfacecolor', 'k')

    plt.show()

if inciso == 'b':
    fs = 8000
    t = 0.01

    x = np.arange(0, 0.01, 1/8000)

    hz_7525 = sin_wave(f=7525,fs=fs,t=t)
    hz_7650 = sin_wave(f=7650,fs=fs,t=t)
    hz_7775 = sin_wave(f=7775,fs=fs,t=t)
    hz_7900 = sin_wave(f=7900,fs=fs,t=t)

    markerline1, stemlines, _ = plt.stem(x, hz_7525, 'b')
    plt.setp(markerline1, 'markerfacecolor', 'b')

    markerline2, stemlines, _ = plt.stem(x, hz_7650, 'r')
    plt.setp(markerline2, 'markerfacecolor', 'r')

    markerline3, stemlines, _ = plt.stem(x, hz_7775, 'h')
    plt.setp(markerline1, 'markerfacecolor', 'g')

    markerline4, stemlines, _ = plt.stem(x, hz_7900, 'k')
    plt.setp(markerline4, 'markerfacecolor', 'k')

    plt.show()    



