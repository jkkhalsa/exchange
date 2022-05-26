import matplotlib.pyplot as plt
import numpy as np


proteinNames = []
dielectricConstants = []
polarizability = []
volume = []



#split each line where commas appear, then add discrete parts into relevant lists
#in separate function because it was easier to debug
def splitLine(l):
    temp = l.split(",")
    proteinNames.append(temp[0])
    dielectricConstants.append(temp[1])
    polarizability.append(temp[2])
    volume.append(temp[3])



#iterate over entire file line by line
with open('epsilon.csv') as text:
    for index, line in enumerate(text):
        splitLine(line)


plt.plot(polarizability, volume, '-', label='Polarizability against Volume')
#plt.legend(loc='best')

plt.show()

