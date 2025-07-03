class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
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


                    