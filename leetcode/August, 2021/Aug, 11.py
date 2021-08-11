# Flip String to Monotone Increasing


# A binary string is monotone increasing if it consists of some number of 0's (possibly none), followed by some number of 1's (also possibly none).
# You are given a binary string s. You can flip s[i] changing it from 0 to 1 or from 1 to 0.
# Return the minimum number of flips to make s monotone increasing.

# Example 1:

# Input: s = "00110"
# Output: 1
# Explanation: We flip the last digit to get 00111.


class Solution:
    def minFlipsMonoIncr(self, s):
        zeros = 0
        ones = 0
        flips = 0
        
        for i in s:
            if i == "0":
                zeros += 1
                flips = min(flips + 1, ones)
            else:
                ones += 1
        
        return flips
        
        
if __name__ == '__main__':
    sol = Solution()
    string = "111110000000"
    print(sol.minFlipsMonoIncr(string))