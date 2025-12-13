class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        for i in range(1, n):
            nums[i] = nums[i] + (nums[i-1] if nums[i-1] > 0 else 0)

        return max(nums)