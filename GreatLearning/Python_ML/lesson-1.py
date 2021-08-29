import numpy as np

# Single Dimension Array # Type: numpy.ndarray
print('\nSingle Dimension Array # Type: numpy.ndarray')
print('\n>>> np.array([10, 20, 30, 40])')
n1 = np.array([10, 20, 30, 40])
print(n1, type(n1))
print('-'*30)

# Multi Dimension Array
print('\nMulti Dimension Array')
print('\n>>> np.array([[10,20,30,40], [40,30,20,10]])')
n2 = np.array([[10,20,30,40], [40,30,20,10]])
print(n2, type(n2))
print('-'*30)

# Initializing Array with zeros
print('\nInitializing Array with zeros')
print('\n>>> np.zeros( (3,2) )')
n3 = np.zeros( (3,2) ) # 3 arrays with 2 zeros each
print(n3)
print('-'*30)

# Initializing Array with any number
print('\nInitializing Array with any number')
print('\n>>> np.full((3,2), 10)')
n4 = np.full((3,2), 10) # 3 arrays with 2 (10) each
print(n4)
print('-'*30)

# Initializing Array with numbers within a range
print('\nInitializing Array with numbers within a range')
print('\n>>> np.arange(10, 60, 5)')
n5 = np.arange(10, 60, 5)
print(n5)
print('-'*30)

# Initializing Array with random numbers
print('\nInitializing Array with random numbers')
print('\n>>> np.random.randint(1, 100, 6)')
n6 = np.random.randint(1, 100, 6) # returns 6 random digits between 1 and 100
print(n6)
print('-'*30)

# Checking and changing the shape of an array
print('\nChecking and changing the shape of an array')
print('\n>>> np.array([[1,2,3], [4,5,6]])')
n7 = np.array([[1,2,3], [4,5,6]]) # 2 arrays with 3 element each
print(n7, n7.shape)
n7.shape = (3,2) # 3 arrays with 2 element each
print(n7, n7.shape)
print('-'*30)