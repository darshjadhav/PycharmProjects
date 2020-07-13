import math
import numpy as np
from numpy.random import randn

# declare and assign variable type int
x = 2

print(x)

print(type(x))

# string
strx = "hello"

print(strx)

print(type(strx))

# logical

boolx = True

print(boolx)
print(type(boolx))

# using math package
print(math.sqrt(x))

# working with strings
greet = "greeting "
name = "bob"

greetings = greet + name;
print(greetings)

# While Loop
i = 1
while boolx == True:
    i = i + 1
    if i == 2:
        boolx = False

# For Loop

for i in range(5):
    print(i)

i = 0
j = 0
counterOne = 0
counterTwo = 0
counterThree = 0
totalOne = 0
totalTwo = 0
totalThree = 0
lstNo = [100, 200, 300]
for i in range(len(lstNo)):
    if i == 0:
        randomOneList = randn(lstNo[i])
        for j in range(lstNo[i]):
            if randomOneList[j] > -1 and randomOneList[j] < 1:
                counterOne = counterOne + 1
        totalOne = counterOne / lstNo[i]
    elif i == 1:
        randomTwoList = randn(lstNo[i])
        for k in range(lstNo[i]):
            if randomTwoList[k] > -1 and randomTwoList[k] < 1:
                counterTwo = counterTwo + 1
        totalTwo = counterTwo / lstNo[i]
    elif i == 2:
        randomThreeList = randn(lstNo[i])
        for l in range(lstNo[i]):
            if randomThreeList[l] > -1 and randomThreeList[l] < 1:
                counterThree = counterThree + 1
        totalThree = counterThree / lstNo[i]

print(totalOne)
print(totalTwo)
print(totalThree)

lst = list(range(5))
print(lst)
lst2 = lst[2:4]
print(lst2)

# numpy array
arr1 = np.array([range(5)])
print('array ', arr1)

print(arr1.mean())