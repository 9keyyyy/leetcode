class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        prefix_sum = 0
        seen = {0: 1} 
        
        for num in nums:
            prefix_sum += num
            
            # 이전에 (현재 누적합 - k)가 있었으면, 그만큼 답에 추가
            if prefix_sum - k in seen:
                count += seen[prefix_sum - k]
            
            # 현재 누적합 기록
            seen[prefix_sum] = seen.get(prefix_sum, 0) + 1
        
        return count

                
