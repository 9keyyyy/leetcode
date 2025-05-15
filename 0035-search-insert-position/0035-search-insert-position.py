class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        
        l, r = 0, n-1
        while (r-l) > 1:
            mid = (l+r)//2
            print(mid, nums[mid])
            if nums[mid] == target:
                return mid

            if nums[mid] < target:
                l = mid
            else:
                r = mid


        if nums[r] < target:
            return r+1
        if nums[l] > target:
            return 0
        if nums[r] == target:
            return r
        if nums[l] == target:
            return l

        return l+1
        # mid = n // 2

        # while mid <= n or mid > 0:
        #     if nums[mid] < target:
        #         mid = (mid + n) // 2
        #     else:
        #         mid = mid // 2


        