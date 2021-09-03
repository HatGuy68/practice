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
        def cross(o, a, b):
            return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
        
        ps = sorted(trees, key=lambda p: (p[0],p[1]))
        ps = [(x,y) for (x,y) in ps]
        
        up,down = [], []
        for p in ps:
            while len(up) >= 2 and cross(up[-2],up[-1],p) < 0:
                up.pop()
            up.append(p)
        for p in reversed(ps):
            while len(down) >= 2 and cross(down[-2],down[-1],p) < 0:
                down.pop()
            down.append(p)
        return list(set(up+down))

if __name__ == '__main__':
    sol = Solution()
    points = [[0,0],[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]
    print(sol.outerTrees(points))