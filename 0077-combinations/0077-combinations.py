class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        ans = []
        arr = []
        def dfs(c, arr, ans):
            if len(arr) == k:
                ans.append(arr[:])
            
            for i in range(c, n+1):
                arr.append(i)
                dfs(i+1, arr, ans)
                arr.pop()

        dfs(1, arr, ans)

        return ans
        