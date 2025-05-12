class Solution(object):
    ans = []
    n = 0
    letter = []

    def dfs(self, comb):
        if len(comb) == self.n:
            self.ans.append(comb)
            return

        for j in range(len(self.letter[len(comb)])):
            comb += self.letter[len(comb)][j]
            self.dfs(comb)
            comb = comb[:-1]


    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        letters = {
            2: ["a", "b", "c"],
            3: ["d", "e", "f"],
            4: ["g", "h", "i"],
            5: ["j", "k", "l"],
            6: ["m", "n", "o"],
            7: ["p", "q", "r", "s"],
            8: ["t", "u", "v"],
            9: ["w", "x", "y", "z"]
        }

        self.n = len(digits)
        self.letter = []
        self.ans = []
        # [["a", "b", "c"], ["d", "e", "f"]]
        for c in digits:
            self.letter.append(letters[int(c)])

        if self.n > 0:
            self.dfs("")

        return self.ans
            
            