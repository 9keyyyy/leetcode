class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        def add_bracket(s, open, close):
            if len(s) == n * 2:
                ans.append(s)

            if open < n:
                add_bracket(s + "(", open + 1, close)
            if open > close:
                add_bracket(s + ")", open, close + 1)

        add_bracket("", 0, 0)
        return ans