#!/bin/python3
# sum of all the prime numbers upto certain limit

limit = 2000000
arr = [0]*limit
ans = 0

for i in range(2, int(len(arr)**0.5)+1):
    if arr[i] == 0:
        for j in range(i**2, len(arr), i):
            arr[j] = 1

for j in range(2, len(arr)):
    if arr[j] == 0:
        ans+=j

print(ans)