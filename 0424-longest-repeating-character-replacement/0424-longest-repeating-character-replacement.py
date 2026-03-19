class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        count = {} 
        left = 0
        max_len = 0
        
        for right in range(len(s)):
            # 1. 오른쪽으로 늘리면서 새로운 알파벳 추가
            char = s[right]
            count[char] = count.get(char, 0) + 1
            
            # 2. 현재 가장 많이 등장한 알파벳의 개수 찾기
            max_freq = max(count.values())
            
            # 3. 현재 액자의 크기
            window_size = right - left + 1
            
            # 4. 바꿔야 하는 알파벳 수가 k개를 초과한다면,
            # 다시 정상 상태가 될 때까지 left를 좁힘
            while window_size - max_freq > k:
                count[s[left]] -= 1
                left += 1
                
                # 상태 다시 계산
                window_size -= 1
                max_freq = max(count.values()) 
                
            # 5. 가장 큰 크기 저장
            max_len = max(max_len, window_size)
            
        return max_len