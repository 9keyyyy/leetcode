class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        result = []
        
        for i in range(len(nums) - 2):
            # 중복 스킵
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            L, R = i + 1, len(nums) - 1
            
            while L < R:
                total = nums[i] + nums[L] + nums[R]
                
                if total < 0:
                    L += 1
                elif total > 0:
                    R -= 1
                else:
                    result.append([nums[i], nums[L], nums[R]])
                    # 중복 스킵
                    while L < R and nums[L] == nums[L+1]: L += 1
                    while L < R and nums[R] == nums[R-1]: R -= 1
                    L += 1
                    R -= 1
        
        return result
        