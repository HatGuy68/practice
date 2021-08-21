# Set Matrix Zeroes

# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's, and return the matrix.
# You must do it in place.

class Solution:
    def setZeroes(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        N=len(matrix)
        n=len(matrix[0])
        iarr=set()
        jarr=set()
 
        for i in range(N):
            for j in range(n):
                if matrix[i][j]==0:
                    if i not in iarr:
                        iarr.add(i)
                    if j not in jarr:
                        jarr.add(j)
                    
        for val in iarr:
            for j in range(n):
                matrix[val][j]=0
        for val in jarr:
            for i in range(N):
                matrix[i][val]=0
        return matrix
        

if __name__ == '__main__':
    sol = Solution()
    matrix = [[1,1,1],[1,0,1],[1,1,1]]
    print(sol.setZeroes(matrix))