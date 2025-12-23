class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prefix_index = {0: -1}
    
        max_len = 0
        prefix_sum = 0
        
        for i, num in enumerate(nums):
            # 0은 -1로 취급
            prefix_sum += 1 if num == 1 else -1
            
            if prefix_sum in prefix_index:
                # 같은 prefix sum을 이전에 봤다 = 그 사이 구간의 합이 0
                length = i - prefix_index[prefix_sum]
                max_len = max(max_len, length)
            else:
                # 처음 보는 prefix sum이면 인덱스 저장
                prefix_index[prefix_sum] = i
        
        return max_len