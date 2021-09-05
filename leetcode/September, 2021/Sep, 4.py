# Sum of Distances in Tree

# There is an undirected connected tree with n nodes labeled from 0 to n - 1 and n - 1 edges.
# You are given the integer n and the array edges where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree.
# Return an array answer of length n where answer[i] is the sum of the distances between the ith node in the tree and all other nodes.

# Example 1:

#   0
#  / \
# 1   2
#    /|\
#   3 4 5

# Input: n = 6, edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
# Output: [8,12,6,10,10,10]
# Explanation: The tree is shown above.
# We can see that dist(0,1) + dist(0,2) + dist(0,3) + dist(0,4) + dist(0,5)
# equals 1 + 1 + 2 + 2 + 2 = 8.
# Hence, answer[0] = 8, and so on.

import collections

class Solution:
    def sumOfDistancesInTree(self, n, edges):
        def dfs(graph, node, parent, count, result):
            for i in graph[node]:
                if i != parent:
                    dfs(graph, i, node, count, result)
                    count[node] += count[i]
                    result[node] += result[i]+count[i]

        def dfs2(graph, node, parent, count, result):
            for i in graph[node]:
                if i != parent:
                    result[i] = result[node]-count[i] + len(count)-count[i]
                    dfs2(graph, i, node, count, result)

        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        count = [1] * n
        result = [0] * n

        dfs(graph, 0, None, count, result)
        dfs2(graph, 0, None, count, result)
        return result


if __name__ == '__main__':
    sol = Solution()
    n = 6
    edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
    print(sol.sumOfDistancesInTree(n, edges))