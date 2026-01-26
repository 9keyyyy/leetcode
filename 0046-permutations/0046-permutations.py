class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n  = len(nums)
        def dfs(cur, ans):
            if len(cur) == n:
                ans.append(cur)
                return

            for i in range(n):
                if nums[i] in cur:
                    continue
                dfs(cur + [nums[i]], ans)
        
        ans = []
        dfs([], ans)
        return ans