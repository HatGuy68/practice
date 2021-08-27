# Longest Uncommon Subsequence II

# Given an array of strings strs, return the length of the longest uncommon subsequence between them. If the longest uncommon subsequence does not exist, return -1.
# An uncommon subsequence between an array of strings is a string that is a subsequence of one string but not the others.
# A subsequence of a string s is a string that can be obtained after deleting any number of characters from s.
#     For example, "abc" is a subsequence of "aebdc" because you can delete the underlined characters in "aebdc" to get "abc". Other subsequences of "aebdc" include "aebdc", "aeb", and "" (empty string).

# Example 1:

# Input: strs = ["aba","cdc","eae"]
# Output: 3


class Solution:
    def findLUSlength(self, strs):
        def isSubsequence(a, b):
            i = 0
            for j in xrange(len(b)):
                if i >= len(a):
                    break
                if a[i] == b[j]:
                    i += 1
            return i == len(a)

        strs.sort(key=len, reverse=True)
        for i in xrange(len(strs)):
            all_of = True
            for j in xrange(len(strs)):
                if len(strs[j]) < len(strs[i]):
                    break
                if i != j and isSubsequence(strs[i], strs[j]):
                    all_of = False
                    break
            if all_of:
                return len(strs[i])
        return -1

        
if __name__ == '__main__':
    sol = Solution()
    strs = ["aba","cdc","eae"]
    print(sol.findLUSlength(strs))