# Erect the Fence

# You are given an array trees where trees[i] = [xi, yi] represents the location of a tree in the garden.
# You are asked to fence the entire garden using the minimum length of rope as it is expensive. The garden is well fenced only if all the trees are enclosed.
# Return the coordinates of trees that are exactly located on the fence perimeter.

# Example 1:

# Input: points = [[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]
# Output: [[1,1],[2,0],[3,3],[2,4],[4,2]]

import math

class Solution:
    def outerTrees(self, trees):
        def orientation( a, b, c):
            return (b[0]-a[0]) * (c[1]-b[1]) - (b[1]-a[1])*(c[0]-b[0])
        trees.sort(key=lambda x: (x[0], x[1]))
        ans = []
        
        # left -> right
        for i in range(len(trees)):
            while len(ans) >= 2 and orientation(ans[-2], ans[-1], trees[i]) < 0:
                ans.pop()
            ans.append(trees[i])
            
        if len(ans) == len(trees): return ans
        
        # right -> left
        for i in range(len(trees)-1-1, -1, -1):
            while len(ans) >= 2 and orientation(ans[-2], ans[-1], trees[i]) < 0:
                ans.pop()
            ans.append(trees[i])
            
        ans.pop()
        return ans
    
    
    
    # (b[0]-a[0])      (c[0]-b[0])
    # (b[1]-a[1])      (c[1]-b[1])  
        

if __name__ == '__main__':
    sol = Solution()
    points = [[0,0],[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]
    print(sol.outerTrees(points))