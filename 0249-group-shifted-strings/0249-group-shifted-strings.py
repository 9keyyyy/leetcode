class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        arr = defaultdict(list)
        for string in strings:
            cur = []
            for s in string:
                cur.append(ord(s)-ord("a"))
            
            criteria = cur[0]
            for i in range(len(cur)):
                cur[i] -= criteria
                if cur[i] < 0:
                    cur[i] += 26
            
            arr[tuple(cur)].append(string)

        return list(arr.values())
        