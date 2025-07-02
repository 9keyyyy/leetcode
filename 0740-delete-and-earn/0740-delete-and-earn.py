class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cur = [0]*10001

        for n in nums:
            cur[n] += n
        
        dp = [0]*10001
        dp[0] = cur[0]
        dp[1] = cur[1]

        for i in range(2, 10001):
            dp[i] = max(dp[i-1], dp[i-2]+cur[i])

        return dp[-1]
        
        
