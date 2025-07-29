class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        q = []
        for arr in matrix:
            for n in arr:
                heapq.heappush(q, n)
        
        for i in range(k-1):
            heapq.heappop(q)

        return heapq.heappop(q)