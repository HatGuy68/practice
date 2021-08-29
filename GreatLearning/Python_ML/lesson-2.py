import numpy as np

# Joining arrays vertically
print('\nJoining arrays vertically')
print('\n>>> np.vstack((n1,n2))')
n1 = np.array([10,20,30])
n2 = np.array([40,50,60])
print(np.vstack((n1,n2))) # 2 arrays with 3 element each
print('-'*30)

# Joining arrays horizontally
print('\nJoining arrays horizontally')
print('\n>>> np.hstack((n3,n4))')
n3 = np.array([1,2,3])
n4 = np.array([4,5,6])
print(np.hstack((n3,n4))) # 1 array of 6 elements
print('-'*30)

# Joining arrays horizontally
print('\nJoining arrays horizontally')
print('\n>>> np.column_stack((n5,n6))')
n5 = np.array([1,2,3])
n6 = np.array([4,5,6])
print(np.column_stack((n5,n6))) # 3 arrays with 2 element each
print('-'*30)
