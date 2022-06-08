from cmath import sin
import matplotlib.pyplot as plt
import numpy as np

def current(t):

    c = 4*10**-6
    l = 0.1
    r = 30

    qnot = 48*10**-6
    omega = np.sqrt((1/(l*c))-(r/(2*l))**2)

    i = (qnot*np.e**(-r*t/(2*l))*np.sin(omega*t)) - (r*np.cos(omega*t))/(2*l)

    return i

timeInputs = np.linspace(0, 50, 100)
capacitor = current(timeInputs)


plt.plot(timeInputs, capacitor, '-', label='Current in RLC Circuit')
plt.legend(loc='best')
plt.xlabel('T')


plt.show()