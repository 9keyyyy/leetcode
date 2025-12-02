class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        s, e = 0, 0
        cur = 0
        ans = 100001
        
        while e < len(nums):
            cur += nums[e]
            if cur >= target:
                while cur >= target:
                    cur -= nums[s]
                    s += 1
                ans = min(ans, e-s+2)
            e += 1

        if ans == 100001:
            return 0
        else:
            return ans
            
                