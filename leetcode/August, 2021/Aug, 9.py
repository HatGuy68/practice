# Add Strings

# Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.
# You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.

# Example 1:

# Input: num1 = "11", num2 = "123"
# Output: "134"

class Solution:
    def addStrings(self, num1, num2):
        maxlength = max(len(num1), len(num2))
        num1 = lenEqualize(num1, maxlength+1)[::-1]
        num2 = lenEqualize(num2, maxlength+1)[::-1]

        result = ["0"]*(maxlength+1)
        carry = 0
        for i in range(len(result)):
            temp = int(num1[i])+int(num2[i])+carry
            result[i] = str(temp%10)
            carry = temp//10


        return (str(int("".join(result[::-1]))))
        
def lenEqualize(number, maxlength):
    number = "0"*(maxlength-len(number))+number
    return number


s = Solution()
print( s.addStrings("11", "134") )