import numpy as np

# Comparing Elements

# Finding common elements in arrays
n1 = np.array([10, 20, 30, 40, 50])
n2 = np.array([40, 50, 60, 70])
print(np.intersect1d(n1,n2))

# Finding uncommon elements 
n3 = np.array([1, 2, 3, 4, 5])
n4 = np.array([4, 5, 6, 7])
# In first array
print(np.setdiff1d(n3,n4))
# In second array
print(np.setdiff1d(n4,n3))

# Comparing each element in the two arrays
n5 = np.array([5, 6, 7, 8])
n6 = np.array([5, 8, 7, 6])
print(n5 == n6)
