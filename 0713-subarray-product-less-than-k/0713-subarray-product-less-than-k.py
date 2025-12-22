class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        prefix_s = [0] * (n+1)
        prefix_s[0] = 1

        s, ans = 0, 0

        if min(nums) >= k:
            return 0

        for i in range(1, n+1):
            prefix_s[i] = prefix_s[i-1] * nums[i-1]
            if prefix_s[i] // prefix_s[s] < k:
                pass
            else:
                # print(i, s, prefix_s[i]//prefix_s[s])
                while prefix_s[i] // prefix_s[s] >= k:
                    s += 1
            ans += i-s
                
        return ans