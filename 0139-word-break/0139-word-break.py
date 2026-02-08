
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        n = len(s)
        dp = [0] * (n+1)
        dp[0] = 1

        wordset = set(wordDict)

        for i in range(1, n+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordset:
                    dp[i] = 1
                    break

        return dp[-1] == 1
                

        