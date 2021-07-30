#!/bin/python3

# Lattice path in an n*n grid

def fact(a):
    if a==1:
        return 1
    return a*fact(a-1)

def latticePath(n):
    return (fact(n*2)//(fact(n)*fact(n)))

print(latticePath(20))