class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        
        n = len(matrix)
        n -= 1
        h = 0
        for c in range(n, 0, -2):
            for i in range(c):
                tmp = matrix[h][h+i]
                matrix[h][h+i] = matrix[n-h-i][h]
                matrix[n-h-i][h] = matrix[n-h][n-h-i]
                matrix[n-h][n-h-i] = matrix[h+i][n-h]
                matrix[h+i][n-h] = tmp
            h += 1

        return matrix