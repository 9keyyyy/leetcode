class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        
        r_list = [0]*n
        for i in range(n):
            if i == 0:
                r_list[i] = nums[i]
            else:
                r_list[i] = nums[i]*r_list[i-1]

        l_list = [0]*n
        for i in range(n-1, -1, -1):
            if i == n-1:
                l_list[i] = nums[i]
            else:
                l_list[i] = nums[i]*l_list[i+1]

        ans = []
        for i in range(n):
            if i == 0:
                ans.append(l_list[i+1])
            elif i == n-1:
                ans.append(r_list[i-1])
            else:
                ans.append(r_list[i-1]*l_list[i+1])
        
        return ans