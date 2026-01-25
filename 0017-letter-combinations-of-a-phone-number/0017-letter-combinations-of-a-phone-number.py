class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        nums = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
        n = len(digits)

        def backtrack(s, ans):
            if len(s) == n:
                ans.append(s)
                return

            for num in nums[digits[len(s)]]:
                s += num
                backtrack(s, ans)
                s = s[:-1]

        ans = []
        for num in nums[digits[0]]:
            backtrack(num, ans)

        return ans