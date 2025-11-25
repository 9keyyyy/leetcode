class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start, end = 0, 0
        if len(s) == 0:
            return 0

        ans = 1
        while start <= end and end < len(s) - 1:
            end += 1
            if s[end] in s[start:end]:
                while s[end] in s[start:end]:
                    start += 1
            else:
                ans = max(ans, end - start + 1)

        return ans
        