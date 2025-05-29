class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(p) > len(s):
            return []
        start, end = 0, len(p)-1

        cur = defaultdict(int)
        pdict = defaultdict(int)

        for c in p:
            pdict[c] += 1

        for i in range(end+1):
            cur[s[i]] += 1

        ans = []
        while True:
            # print(start, cur, pdict)
            if cur == pdict:
                ans.append(start)
                
            if cur[s[start]] == 1:
                cur.pop(s[start], None)
            else:
                cur[s[start]] -= 1
            start += 1
            end += 1

            if end >= len(s):
                break

            cur[s[end]] += 1

        return ans




        