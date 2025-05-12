class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        s, e = 0, 0
        
        while e < len(nums):
            if nums[s] == 0:
                while nums[e] == 0:
                    e += 1
                    if e == len(nums):
                        break
            if e == len(nums):
                break

            nums[s], nums[e] = nums[e], nums[s]
            
            e += 1
            s += 1
