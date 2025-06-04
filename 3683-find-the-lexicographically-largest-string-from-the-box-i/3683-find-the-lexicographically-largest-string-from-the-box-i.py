class Solution(object):
    def answerString(self, word, numFriends):
        """
        :type word: str
        :type numFriends: int
        :rtype: str
        """
        if numFriends == 1:
            return word
        n = len(word)
        res = ""
        for i in range(n):
            res = max(res, word[i : min(i + n - numFriends + 1, n)])
        return res
            
