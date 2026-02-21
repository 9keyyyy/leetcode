class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        n = len(temperatures)
        ans = [0]*n
        
        q = deque([(temperatures[n-1], n-1)])
        for i in range(n-2, -1, -1):
            while q:
                cur, idx = q.pop()
                if temperatures[i] >= cur:
                    continue
                else:
                    ans[i] = idx - i
                    q.append((cur, idx))
                    break
            q.append((temperatures[i], i))
        return ans    

