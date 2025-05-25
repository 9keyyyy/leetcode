class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        hmap = {}
        ans = []
        
        for s in strs:
            cur = "".join(sorted(s))
            
            if cur in hmap:
                hmap[cur].append(s)
            else:
                hmap[cur] = [s]

        for k, v in hmap.items():
            ans.append(v)
        
        return ans

