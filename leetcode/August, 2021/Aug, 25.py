# Sum of Square Numbers

# Given a non-negative integer c, decide whether there're two integers a and b such that a2 + b2 = c.

# Example 1:

# Input: c = 5
# Output: true
# Explanation: 1 * 1 + 2 * 2 = 5

import math

class Solution:
    def judgeSquareSum(self, c):
        if c<0:
            return False
        left, right = 0, math.ceil(math.sqrt(c))
        while (left <= right):
            curr = left**2 + right**2
            if (curr < c):
                left+=1
            elif (curr > c):
                right-=1
            else:
                print(left, right)
                return True
        
        print(left, right)
        return False

if __name__ == '__main__':
    sol = Solution()
    k = 5
    print(sol.judgeSquareSum(k))