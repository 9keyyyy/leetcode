class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        dp = [[0]*i for i in range(1, numRows+1)]
        dp[0][0] = 1

        for i in range(1, numRows):
            for j in range(i+1):
                if j == 0 or j == i:
                    dp[i][j] = 1
                    continue
                
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j]

        return dp
        