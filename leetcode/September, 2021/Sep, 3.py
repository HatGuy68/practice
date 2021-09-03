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
        trees = sorted(map(tuple, trees), key=lambda x:(x[0], x[1]))
        return list(set(self.build(trees) + self.build(trees[::-1])))
        
    def sign(self, o, a, b):
        return (a[0]-o[0]) * (b[1]-o[1]) - (b[0]-o[0]) * (a[1]-o[1])
    
    def build(self, trees):
        hull = []
        for p in trees:
            while len(hull) >= 2 and self.sign(hull[-2], hull[-1], p) < 0:
                hull.pop()
            hull.append(p)
        return hull
        
    
    
    # (b[0]-a[0])      (c[0]-b[0])
    # (b[1]-a[1])      (c[1]-b[1])  
        

if __name__ == '__main__':
    sol = Solution()
    points = [[0,0],[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]
    print(sol.outerTrees(points))