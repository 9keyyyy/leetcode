class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        sum_val = 0
        prefix_sum_count = {0: 1}  # 초기값: 합이 0인 경우 1개
        
        for num in nums:
            sum_val += num  # 현재까지의 누적합
            
            # (현재 누적합 - k)가 이전에 나온 적이 있는지 확인
            if (sum_val - k) in prefix_sum_count:
                count += prefix_sum_count[sum_val - k]
            
            # 현재 누적합을 딕셔너리에 저장/업데이트
            prefix_sum_count[sum_val] = prefix_sum_count.get(sum_val, 0) + 1
        
        return count