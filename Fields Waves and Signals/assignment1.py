from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import numpy as np


def f(t, y):

    #constants
    b = 10      #damping constant
    m = 25      #mass
    F0 = 150    #initial force
    k = 226     #spring constant


    x = y[0]
    v = y[1];
    f_v = -(b/m)*v - (k/m)*x + F0/m*np.sin(np.sqrt(k/m)*t)

    return np.array([v, f_v])




# QUESTION: cannot figure out difference between w' and w0
# current equation leaves out t(time) in sin wave 

def wave(om):
    #constants
    b = 10      #damping constant
    m = 25
    w = np.sqrt(m/226)  #sqrt(m/k)
    F0 = 150    #initial force

    A = F0/np.sqrt(m**2 * (om**2 - w**2) + b**2 * om)
    phi = np.arctan((b*om) / m * (om**2 - w**2))

    wave = A*np.sin(om + phi)


    return wave

def wave_t(t):
    #wave function with T
    
    #constants
    b = 10      #damping constant
    m = 25
    w0 = np.sqrt(226/m)  #sqrt(k/m)
    F0 = 150    #initial force
    w = w0

    A = F0/np.sqrt(m**2 * (w**2 - w0**2)**2 + b**2 * w**2)
    phi = np.arctan2((b*w), (m * (w**2 - w0**2)))

    wave = A*np.sin(w*t + phi)

    return wave


def Awave(w):
    #constants
    b = 10      #damping constant
    m = 25
    w0 = np.sqrt(226/m)  #sqrt(k/m)
    F0 = 150    #initial force

    A = F0/np.sqrt(m**2 * (w**2 - w0**2)**2 + b**2 * w**2)
    print(w0)

    return A



inputs = np.linspace(0, 10, 21)
#sinusoid = wave(inputs)
sinusoid_t = wave_t(inputs)

sol = solve_ivp(f, [0, 25], [20, 41], dense_output=True)

A = Awave(inputs)

#plt.plot(sol.t, sol.y[0,:], '-', label='Excercise 93')
#plt.plot(sinusoid, '-', label="sinusoid with om")
#plt.plot(sinusoid_t, '-', label="sinusoid with t")
plt.plot(A, '-', label='Amplitude with respect to w prime')
plt.legend(loc='best')
plt.xlabel('T')


plt.show()