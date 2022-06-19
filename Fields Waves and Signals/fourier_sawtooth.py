### Fields, Waves and Signals  -- Sean Gryb
###
### Perform and plot Fourier of transform of `sawtooth' wave
###
### Code sample for Assignment 7, Problem 2

## Import required libraries
import matplotlib.pyplot as plt   # For plotting
import numpy as np  # For numerics
from scipy.integrate import quad_vec   # For numerical integration of vectors
from scipy import signal   # For `sawtooth' function

## Input function parameters -- modify these to your choosing
N = 15  # Number of Fourier coeficients
w = 1  # Modify this!! -- default: w = 1

## Other parameters
L = 1  # Number of cycles to analyse (centered on zero) -- default: L = 1
pts = 300  # Number of points to plot - default: pts = 300

## Plot options -- Modify these to get different plot combinations (both can be True)
PlotFourierApprox = True   # To plot Fourier approx at order N
PlotFourierCoef = True     # To plot Fourier coeficients up to order N

## Define vectors with values of 'n' and 't'
n = np.arange(N+1)
t = np.linspace(-L, L, pts )

## Define `sawtooth' function to Fourier Transform
def func(t):
    return signal.sawtooth(np.pi*t,w)

## Compute a_n and b_n coefficients

# Define integrand for a_n
def inta(t):
    return func(t)*np.cos(np.pi*n*t/L)

# Compute a_n
an,erra = quad_vec( inta, -L, L)  # erra - error estimate (not used)
an = an/L  # Include normalization

# Define integrand for b_n
def intb(t):
    return func(t)*np.sin(np.pi*n*t/L)

# Compute b_n
bn,errb = quad_vec( intb, -L, L)
bn = bn/L

## Initiate for-loop to compute Fourier sum
f = an[0]/2
for i in n[1:n.shape[0]]:
    f = f+an[i]*np.cos(i*np.pi*t/L) + bn[i]*np.sin(i*np.pi*t/L)

## Plot using different options
if (PlotFourierApprox and not(PlotFourierCoef)): # Plot only N^th order Fourier approx
    plt.figure(figsize=(10,8))
    plt.title('Fourier approximation to waveform')
    plt.xlabel('t')
    plt.ylabel('f')
    plt.plot(t,func(t))
    plt.plot(t,f)
        
if (PlotFourierCoef and not(PlotFourierApprox)): # Plot only Fourier coefficients
    plt.title('Fourier coefficients')
    plt.xlabel('n')
    plt.ylabel('Coefficient')
    plt.plot(n,an,'o--',label = 'a_n')
    plt.plot(n,bn,'o--',label = 'b_n')
    plt.legend()
    

if (PlotFourierApprox and PlotFourierCoef): # Plot both
    plt.figure(figsize=(10,16))
    plt.subplot(2,1,1)
    plt.title('Fourier approximation to waveform')
    plt.xlabel('t')
    plt.ylabel('f')
    plt.plot(t,func(t))
    plt.plot(t,f)
        
    plt.subplot(2,1,2)
    plt.title('Fourier coefficients')
    plt.xlabel('n')
    plt.ylabel('Coefficient')
    plt.plot(n,an,'o--',label = 'a_n')
    plt.plot(n,bn,'o--',label = 'b_n')
    plt.legend()


    