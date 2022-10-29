import matplotlib.pyplot as plt
import numpy as np

def unit_step(a, n): 
    unit =[] 
    for sample in n: 
        if sample<a: 
            unit.append(0) 
        else: 
            unit.append(1) 
    return(unit) 
  
a_u = 2
UL_u = 5
LL_u = 0
unit_i = np.arange(LL_u, UL_u, 1)

def unit_impulse(a, n): 
    delta =[] 
    for sample in n: 
        if sample == a: 
            delta.append(1) 
        else: 
            delta.append(0) 
              
    return delta 

a_i = 2
UL_i = 5
LL_i = 0
impulse_i = np.arange(LL_i, UL_i, 1) 
impulse = unit_impulse(a_i, impulse_i) 

unit = unit_step(a_u, unit_i)

muestras_y = len(unit) + len(impulse) - 1
inicio_y = min(impulse_i) + min(unit_i)

n = np.arange(inicio_y, muestras_y, 1)

y = np.convolve(unit,impulse)

plt.subplot(311)
plt.stem(unit_i,unit)

plt.subplot(312)
plt.stem(impulse_i,impulse)

plt.subplot(313)
plt.stem(n,y)

plt.show()