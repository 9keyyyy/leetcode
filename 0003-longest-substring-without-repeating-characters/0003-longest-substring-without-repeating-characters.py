class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start, end = 0, 0
        used = {}

        ans = 0
        while end < len(s):
            if not used.get(s[end]):
                used[s[end]] = 1
            else:
                used[s[end]] += 1

            while used[s[end]] > 1:
                used[s[start]] -= 1
                start += 1
            
            ans = max(ans, end - start + 1)
            end += 1

        return ans