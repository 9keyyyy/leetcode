class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = [0] * (n + 1)
        
        dp[0] = 1          # 빈 문자열 → 1가지
        dp[1] = 0 if s[0] == '0' else 1  # 첫 글자가 '0'이면 불가
        
        for i in range(2, n + 1):
            # 1자리로 읽기
            one = int(s[i-1])
            if one >= 1:
                dp[i] += dp[i-1]
            
            # 2자리로 읽기
            two = int(s[i-2:i])
            if 10 <= two <= 26:
                dp[i] += dp[i-2]
        
        return dp[n]