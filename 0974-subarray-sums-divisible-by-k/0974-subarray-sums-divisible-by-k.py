class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        remainder_count = {0: 1}  # 나머지 0은 1번 등장한 것으로 시작
    
        prefix_sum = 0
        count = 0
        
        for num in nums:
            prefix_sum += num
            remainder = prefix_sum % k
            
            # 같은 나머지가 이전에 나온 횟수만큼 구간이 생김
            if remainder in remainder_count:
                count += remainder_count[remainder]
                remainder_count[remainder] += 1
            else:
                remainder_count[remainder] = 1
        
        return count