class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = s[0]
        for i in range(len(s)):
            cur = s[i]
            start, end = i, i
            while True:
                start -= 1
                end += 1
                if start < 0 or end >= len(s):
                    break
                if s[start] == s[end]:
                    if len(ans) < end-start+1:
                        ans = s[start:end+1]
                else:
                    break

        for i in range(len(s)):
            cur = s[i]
            start, end = i, i+1
            if end >= len(s) or s[start] != s[end]:
                continue
            if len(ans) < end-start+1:
                ans = s[start:end+1]
            while True:
                start -= 1
                end += 1
                if start < 0 or end >= len(s):
                    break
                if s[start] == s[end]:
                    if len(ans) < end-start+1:
                        ans = s[start:end+1]
                        print(ans)
                else:
                    break
        return ans

