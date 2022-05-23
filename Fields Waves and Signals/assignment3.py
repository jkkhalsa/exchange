import matplotlib.pyplot as plt
import numpy as np

def voltage(t):
    
    y = 1-np.e**(-t/.0075)

    return y


timeInputs = np.linspace(0, .0172693882, 50)
capacitor = voltage(timeInputs)


plt.plot(timeInputs, capacitor, '-', label='Voltage over capacitor')
plt.legend(loc='best')
plt.xlabel('T')


plt.show()