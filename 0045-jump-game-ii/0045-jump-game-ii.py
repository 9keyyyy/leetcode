class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        cur_max = nums[0] + 1
        criteria = 0
        
        if n == 1:
            return 0

        ans = 1
        for i in range(n):
            if i+cur_max >= n:
                break
            if cur_max <= nums[i]:
                if nums[criteria] - (i-criteria) < nums[i]:
                    criteria = i
                    print("criteria", i, criteria, nums[criteria], cur_max)
            cur_max -= 1
            if cur_max == 0:
                ans += 1
                cur_max = nums[criteria] - (i-criteria)
                print("cur_max", i, cur_max)

        return ans




