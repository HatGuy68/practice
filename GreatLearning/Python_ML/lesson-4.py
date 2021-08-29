import numpy as np

# Addition of all elements of numpy arrays # Caution: Shape of arrays should be the same
print('\nAddition of all elements of numpy arrays # Caution: Shape of arrays should be the same')
n1 = np.array([10, 20, 50])
n2 = np.array([30, 40, 5])
print('>>> np.sum([n1, n2])')
print(np.sum([n1, n2]))
# Addition along all elements in same array
print('\nAddition along all elements in same array')
print('>>> np.sum([n1, n2], axis=1)')
print(np.sum([n1, n2], axis=1)) # returns array of elements equal to number of arrays
# Addition along every element in all arrays
print('\nAddition along every element in all arrays')
print('>>> np.sum([n1, n2], axis=0)')
print(np.sum([n1, n2], axis=0)) # returns array of elements equal to number of elements in each array
print('-'*30)

# Basic addition
print('\nBasic addition')
print('\n>>> n3 += 1')
n3 = np.array([10, 20, 50])
n3 += 1
print(n3)
print('-'*30)

# Basic multiplication
print('\nBasic multiplication')
print('\n>>> n4 *= 1')
n4 = np.array([10, 20, 50])
n4 *= 10
print(n4)
print('-'*30)

# Basic subtraction
print('\nBasic subtraction')
print('\n>>> n5 -= 1')
n5 = np.array([10, 20, 50])
n5 -= 1
print(n5)
print('-'*30)

# Basic division
print('\nBasic division')
print('\n>>> n6 = n6 / 10')
n6 = np.array([10, 20, 50])
n6 = n6 / 10
print(n6)
print('-'*30)

# Mean
print('\nMean > np.arange(10, 61, 10)')
print('\n>>> np.mean(n7)')
n7 = np.arange(10, 61, 10)
print(np.mean(n7))

print('-'*30)
# Median
print('\nMedian > np.arange(10, 30, 3)')
print('\n>>> np.median(n7)')
n7 = np.arange(10, 30, 3)
print(np.median(n7))

print('-'*30)
# Standard Deviation
print('\nStandard Deviation > np.arange(10, 100, 3)')
print('\n>>> np.std(n7)')
n7 = np.arange(10, 100, 3)
print(np.std(n7))
print('-'*30)