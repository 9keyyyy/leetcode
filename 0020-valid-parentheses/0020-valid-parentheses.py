from collections import deque

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        q = deque()
        pair = [["(", ")"], ["{", "}"], ["[", "]"]]
        
        for c in s:
            for opened, closed in pair:
                if c == opened:
                    q.append(opened)
                elif c == closed:
                    if not q:
                        return False
                    cur = q.pop()
                    if cur != opened:
                        return False
        return not q