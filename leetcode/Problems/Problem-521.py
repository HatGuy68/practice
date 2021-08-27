# Given two strings a and b, return the length of the longest uncommon subsequence between a and b. If the longest uncommon subsequence does not exist, return -1.

# An uncommon subsequence between two strings is a string that is a subsequence of one but not the other.
# A subsequence of a string s is a string that can be obtained after deleting any number of characters from s.
#     For example, "abc" is a subsequence of "aebdc" because you can delete the underlined characters in "aebdc" to get "abc". Other subsequences of "aebdc" include "aebdc", "aeb", and "" (empty string).

# Example 1:

# Input: a = "aba", b = "cdc"
# Output: 3

class Solution:
    def findLUSlength(self, a, b):
        if a == b:
            return -1
        return max(len(a), len(b))

if __name__ == '__main__':
    sol = Solution()
    a = "aba"
    b = "cdc"
    print(sol.findLUSlength(a, b))