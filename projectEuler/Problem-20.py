#!/bin/python3

# Sum of the digits of the result of factorial of a number

def fact(n):
    if n == 1:
        return 1
    
    return n*fact(n-1)

def solve():
    add = 0
    for i in str(fact(100)):
        add += int(i)
    
    return add

print(solve())