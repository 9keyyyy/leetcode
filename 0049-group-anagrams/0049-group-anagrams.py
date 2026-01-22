class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hashmap = defaultdict(list)
        for s in strs:
            arr = list(s)
            arr.sort()

            hashmap[tuple(arr)].append(s)

        ans = []
        for v in hashmap.values():
            ans.append(v)

        return ans