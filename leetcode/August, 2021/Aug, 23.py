# Two Sum IV - Input is a BST

# Given the root of a Binary Search Tree and a target number k, return true if there exist two elements in the BST such that their sum is equal to the given target.

# Example 1:

# Input: root = [5,3,6,2,4,null,7], k = 9
# Output: true

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findTarget(self, root, k):
        # x + y = k
        # y = k - x

        l = set()
        def dfs(node):
            if not node: return False
            y = k - node.val
            if y in l:
                return True
            else:
                l.add(node.val)
            return dfs(node.left) or dfs(node.right)

        return dfs(root)


if __name__ == '__main__':
    sol = Solution()
    root = TreeNode(val= 5,
                    left= TreeNode(val= 3,
                                   left= TreeNode(val= 2,
                                                  left= None,
                                                  right= None),
                                   right= TreeNode(val= 4,
                                                   left= None,
                                                   right= None)),
                    right= TreeNode(val= 6,
                                    left= None,
                                    right= TreeNode(val= 7,
                                                    left= None,
                                                    right= None)))
    k = 9
    print(sol.findTarget(root, k))