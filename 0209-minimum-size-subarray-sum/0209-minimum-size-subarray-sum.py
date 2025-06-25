class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        s, e = 0, 0
        n = len(nums)

        cur = nums[0]
        min_len = 1e9

        while True:
            if target > cur:
                e += 1

                if e >= n:
                    break

                cur += nums[e]
            else:
                if min_len > e - s + 1:
                    min_len = e - s + 1

                if e == s:
                    break

                cur -= nums[s]
                s += 1
        
        return min_len if min_len != 1e9 else 0