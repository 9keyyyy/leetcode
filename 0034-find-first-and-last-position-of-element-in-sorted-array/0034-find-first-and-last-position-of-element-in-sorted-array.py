class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)

        if n == 1 and target == nums[0]:
            return [0, 0]

        left, right = 0, n-1
        idx = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                idx = mid
                break
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        if idx != -1:
            start, end = idx, idx
            while 0 <= start:
                if nums[start] == target:
                    start -= 1
                else:
                    break
            while end < n:
                if nums[end] == target:
                    end += 1
                else:
                    break
            return [start+1, end-1]
        return [-1, -1]
                