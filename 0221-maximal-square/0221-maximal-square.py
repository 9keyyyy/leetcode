class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        n = len(matrix)
        m = len(matrix[0])

        dp = [[0]*m for _ in range(n)]
        
        max_side = 0
        for i in range(n):
            dp[i][0] = int(matrix[i][0])
            max_side = max(max_side, dp[i][0])

        for i in range(1, m):
            dp[0][i] = int(matrix[0][i])
            max_side = max(max_side, dp[0][i])

        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][j] == "1":
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    max_side = max(max_side, dp[i][j])

        return max_side * max_side