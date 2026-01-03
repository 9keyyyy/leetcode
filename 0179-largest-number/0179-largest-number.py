class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums = [str(n) for n in nums]
        
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] + nums[i] > nums[i] + nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
        
        ans = ''.join(nums)
        
        return '0' if ans[0] == '0' else ans
            