# Array of Doubled Pairs


# Given an integer array of even length arr, return true if it is possible to reorder arr such that
# arr[2 * i + 1] = 2 * arr[2 * i] for every 0 <= i < len(arr) / 2, or false otherwise.

# Example 1:

# Input: arr = [3,1,3,6]
# Output: false

import collections

class Solution:
    def canReorderDoubled(self, arr):
        count = collections.Counter(arr)

        for x in sorted(count, key=abs):
            if count[x*2] < count[x]: return False
            count[x*2] -= count[x]

        return True

if __name__ == '__main__':
    sol = Solution()
    arr = [4,-2, 2, -4]
    print(sol.canReorderDoubled(arr))