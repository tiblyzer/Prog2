import numpy as np
import math

#----------------------
#----------ex1---------
#----------------------

limitMin = 0
limitMax = 500
lengthofSet = 50

numbers = np.random.randint(limitMin,limitMax,lengthofSet)
setA = set(numbers)

minElement = np.inf
maxElement = -np.inf

for i in setA:
    if i < minElement:
        minElement = i
    if i > maxElement:
        maxElement = i

print(setA)
print('The minimum value in setA: {}'.format(minElement))
print('The maximum values in SetA:', maxElement)

#----------------------
#----------ex2---------
#----------------------

str = '*'
N = 9

for i in range(1,N+1):
    if i<=math.ceil(float(N)/2):
        print(i*str)
    else:
        print((N+1-i)*str)

#----------------------
#----------ex3---------
#----------------------

rows = input('Number of rows:')
rows = int(rows)
columns = int(input('Number of colums:'))
M = np.zeros((rows,columns))
for i in range(0,rows):
    for j in range(0,columns):
        M[i,j] = i*j

print(M)