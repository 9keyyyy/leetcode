class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = s[0]
        for i in range(len(s)):
            start, end = i-1, i+1

            if end < len(s) and s[end] == s[i]:
                while end < len(s) and s[end] == s[i]:
                    end += 1

                if len(ans) < len(s[i:end]):
                    ans = s[i:end]


            while True:
                if start < 0 or end >= len(s):
                    break
                if s[start] == s[end]:
                    if len(ans) < len(s[start:end+1]):
                        ans = s[start:end+1]
                
                else:
                    break
                
                start -= 1
                end += 1

        return ans

