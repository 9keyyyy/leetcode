class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n == 1:
            return k

        dp = [0] * (n+1)
        
        dp[1] = k
        dp[2] = k * k

        for i in range(3, n+1):
            dp[i] = (k-1)*dp[i-1] + (k-1)*dp[i-2]
        print(dp)
        return dp[-1]