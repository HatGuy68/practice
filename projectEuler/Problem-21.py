#!/bin/python3

# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into 
# n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are 
# called amicable numbers.

# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d
# 220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

def sumOfProperDivisors(n):
    add = 0
    for i in range(1,(n//2)+1):
        if n%i == 0:
            add += i
    return add

def amicable(limit):
    amicableList = []
    for i in range(limit):
        if amicableList.count(i) > 0:
            continue

        temp = sumOfProperDivisors(i)
        if sumOfProperDivisors(temp) == i:
            amicableList.append(i)
            amicableList.append(temp)

    return set(amicableList)

def solve():
    nums = amicable(10000)
    print(nums)
    add = 0
    for i in nums:
        add += int(i)
    return add

print(solve())