class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        stack = []
        num = 0
        prev = ""
        for ss in s:
            if ss.isdigit():
                num = int(ss) + num*10
            elif ss == "[":
                stack.append((num, prev))
                prev = ""
                num = 0
            elif ss == "]":
                cnum, cprev = stack.pop()
                prev = cprev + cnum * prev
            else:
                prev += ss
        
        return prev
