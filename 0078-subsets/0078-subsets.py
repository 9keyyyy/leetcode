class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        ans = []
        def dfs(idx, cur, m):
            if len(cur) == m:
                ans.append(cur)
                return

            for i in range(idx, n):
                dfs(i+1, cur+[nums[i]], m)
        
        for i in range(n+1):
            dfs(0, [], i)

        return ans
                