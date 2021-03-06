# 1. Two Sum
# Easy

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].

# Start Time: 9:34 pm Friday, 8 October 2021 (IST) 

class Solution:
    def twoSum(self, nums, target):        
        for ind, number in enumerate(nums):
            dual = target - number
            index_of_dual = nums.index(dual) if dual in nums else None
            if index_of_dual is not None and index_of_dual != ind:
                return [ind, index_of_dual]

if __name__ == '__main__':
    sol = Solution()
    nums = [3,2,3]
    target = 6
    print(sol.twoSum(nums, target))