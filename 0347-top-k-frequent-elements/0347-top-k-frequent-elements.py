class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        hashmap = defaultdict(int)
        for n in nums:
            hashmap[n] += 1
        
        arr = []
        for n, v in hashmap.items():
            arr.append((v, n))

        arr.sort(reverse=True)
        ans = []
        for i in range(k):
            ans.append(arr[i][1])
        
        return ans
