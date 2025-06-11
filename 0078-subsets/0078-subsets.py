class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        def backtracking(n, arr, idx):
            if len(arr) == n:
                ans.append(arr[:])
            
            for i in range(idx, len(nums)):
                arr.append(nums[i])
                backtracking(n, arr, i+1)
                arr.pop()

        for i in range(len(nums)+1):
            backtracking(i, [], 0)

        return ans