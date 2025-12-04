class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        if not dp[0] and n > 1:
            return False

        for i in range(1, n-1):
            dp[i] = max(dp[i-1]-1, nums[i])
            if dp[i] == 0:
                return False

        return True
        