class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 1:
            return 1


        start, end = 0, 1
        cur = [s[start]]

        for i in range(1, len(s)):
            if cur[0] != s[i]:
                cur.append(s[i])
                end = i
                break

        if len(cur) == 1:
            return len(s)
   
        ans = end - start + 1

        while end < len(s):
            # if len(cur) == 2:
            if s[end] not in cur:
                ans = max(ans, end - start)
                cur = [s[end], s[end-1]]
                idx = end-1
                while start < idx:
                    if s[idx] == s[end-1]:
                        idx -= 1
                    else:
                        break
                start = idx + 1
            else:
                end += 1

                if end == len(s):
                    ans = max(ans, end - start)

                    
        return ans

            
            