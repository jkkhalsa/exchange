from cmath import sin
import matplotlib.pyplot as plt
import numpy as np

def current(t):

    xl = 158.113883
    xc = xl

    phi = np.arctan((xl - xc) / 30)
    Inot = 12 / (np.sqrt(30**2 + (xl - xc)**2))
    omega = 1581.13883

    i = Inot * np.sin(omega * t - phi)

    return i

timeInputs = np.linspace(0, 50, 100)
capacitor = current(timeInputs)


plt.plot(timeInputs, capacitor, '-', label='Current in RLC Circuits')
plt.legend(loc='best')
plt.xlabel('T')


plt.show()