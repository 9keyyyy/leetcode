class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        """
        # 메모이제이션을 위한 딕셔너리
        memo = {}
        
        def lcs(i, j):
            # 기저 조건: 한쪽 문자열이 끝나면 0
            if i >= len(text1) or j >= len(text2):
                return 0
            
            # 이미 계산된 결과가 있으면 반환
            if (i, j) in memo:
                return memo[(i, j)]
            
            # 현재 문자가 같으면 둘 다 다음으로 이동
            if text1[i] == text2[j]:
                result = 1 + lcs(i + 1, j + 1)
            else:
                # 다르면 둘 중 하나를 이동시켜서 최대값 선택
                result = max(lcs(i + 1, j), lcs(i, j + 1))
            
            # 결과를 메모에 저장
            memo[(i, j)] = result
            return result
        
        return lcs(0, 0)
        """

        m, n = len(text1), len(text2)
        
        # DP 테이블 초기화
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # 앞에서부터 채우기
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i-1] == text2[j-1]:
                    # 현재 문자가 같으면: 이전 대각선 + 1
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    # 현재 문자가 다르면: 위쪽 또는 왼쪽 중 최대값
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        return dp[m][n]


                    