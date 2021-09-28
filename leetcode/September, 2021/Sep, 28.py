# Sort Array By Parity II

# Given an array of integers nums, half of the integers in nums are odd, and the other half are even.
# Sort the array so that whenever nums[i] is odd, i is odd, and whenever nums[i] is even, i is even.
# Return any answer array that satisfies this condition.

# Example 1:

# Input: nums = [4,2,5,7]
# Output: [4,5,2,7]
# Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.

class Solution:
    def sortArrayByParityII(self, nums):
        sortedArray = ['']*len(nums)
        odd = 1
        even = 0
        
        for i in nums:
            if i%2==0:
                sortedArray[even] = i
                even+=2
            elif i%2==1:
                sortedArray[odd] = i
                odd+=2
        return sortedArray


if __name__ == '__main__':
    sol = Solution()
    nums = [4,2,5,7]
    print(sol.sortArrayByParityII(nums))