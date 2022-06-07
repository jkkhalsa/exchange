import random

array = []
isPrime = True
temp = 0

for x in range(100):
    while(isPrime):
        temp = random.randint(3, 1000)
        for n in range(2, temp):
            if(temp%n == 0):
                isPrime = False
    array.append(temp)
    isPrime = True

print(array)

import random

array = []
isPrime = True
temp = 0

while len(array) <= 100:
    while(isPrime):
        temp = random.randint(3, 1000)
        for n in range(2, temp):
            if(temp%n == 0):
                isPrime = False
    array.append(temp)
    isPrime = True

print(array)