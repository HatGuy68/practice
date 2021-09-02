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
    def generateTrees(self, n):
        result = []
        tree_list = {}
        return self.dfs(result, 1, n, tree_list)

    def dfs(self, result, start, end, tree_list):
        if start == end:
            return [TreeNode(start)]
        if start > end:
            return [None]
        if (start, end) in tree_list:
            return tree_list[(start, end)]
        
        root_trees = []
        for i in range(start, end + 1):
            left_trees = self.dfs(result, start, i - 1, tree_list)
            right_trees = self.dfs(result, i + 1, end, tree_list)
            
            for left_tree in left_trees:
                for right_tree in right_trees:
                    root = TreeNode(i)
                    root.left = left_tree
                    root.right = right_tree
                    root_trees.append(root)
                    
        tree_list[(start, end)] = root_trees
        return root_trees

def preorder( root):
    if (root != None):
        print(root.val, end = " " )
        preorder(root.left)
        preorder(root.right)

if __name__ == '__main__':
    sol = Solution()
    nums = 3 # Cannot be used :')
    trees = sol.generateTrees(nums)
    for i in range(len(trees)):
        preorder(trees[i])
        print()