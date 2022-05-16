from re import S
import matplotlib.pyplot as plt
import numpy as np

def ystanding(x = [], *args):

    #constants
    kn = 1

    answers = []
    
    for j in x:
        k = int(j)
        s = 0;
        for i in range(0, k+1):
            for n in range(5):
                s = s + n*np.sin(np.pi*k)
        answers.append(s)

    #y_standing = sum(cn*np.sin(kn*x)*np.cos(kn*v*t))

    #errors out - thinks we're doing matrix multiplication

    return answers

inputs = np.linspace(0, 1, 51)

sol = ystanding(inputs)

plt.plot(inputs, sol, '-', label="standing wave at 0")
plt.legend(loc='best')

plt.show()