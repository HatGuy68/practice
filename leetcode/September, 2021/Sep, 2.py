# Unique Binary Search Trees II

# Given an integer n, return all the structurally unique BST's (binary search trees), which has exactly 
# n nodes of unique values from 1 to n. Return the answer in any order.

# Example 1:

# Input: n = 3
# Output: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def newTree(x, l, r): 
            t = TreeNode(x)
            t.left = l
            t.right = r
            return t

        def gen(s, e):      
            return [newTree(i, l, r) for i in range(s, e + 1) for l in gen(s, i - 1) for r in gen(i + 1, e)] or [None]

        return gen(1, n) if n > 0 else []

if __name__ == '__main__':
    sol = Solution()
    nums = [5,4,0,3,1,6,2] # Cannot be used :')
    print(sol.arrayNesting(nums))