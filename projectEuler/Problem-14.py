#!/bin/python3

# Longest Collatz Sequence under 1,000,000


def collatz(n):
    longestSequence = []
    for i in range(n):
        sequence = []
        element = i
        sequence.append(int(element))
        while element > 1:
            if element%2 == 0:
                element/=2
                sequence.append(int(element))
            else:
                element = 3*element + 1
                sequence.append(int(element))

        if len(sequence) > len(longestSequence):
            longestSequence = sequence

    return longestSequence

print(collatz(1000000))

# solution using dp: