# A complex number can be represented as a string on the form "real+imaginaryi" where:
#     real is the real part and is an integer in the range [-100, 100].
#     imaginary is the imaginary part and is an integer in the range [-100, 100].
#     i2 == -1.
# Given two complex numbers num1 and num2 as strings, return a string of the complex number that represents their multiplications.

# Example 1:

# Input: num1 = "1+1i", num2 = "1+1i"
# Output: "0+2i"
# Explanation: (1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i, and you need convert it to the form of 0+2i.

class Solution:
    def threeSum(self, num1, num2):
        a, b = num1.split("+")
        a = int(a)
        b = int(b[:-1])
        c, d = num2.split("+")
        c = int(c)
        d = int(d[:-1])
        x = a*c - b*d
        y = a*d + b*c
        return str(x)+'+'+str(y)+'i'

if __name__ == '__main__':
    sol = Solution()
    num1 = "1+-1i"
    num2 = "0+0i"
    print(sol.threeSum(num1, num2))