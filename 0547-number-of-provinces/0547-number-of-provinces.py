class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        n = len(isConnected)

        visited = [0] * n

        def bfs(a):
            q = deque([a])
            visited[a] = 1
            while q:
                c = q.popleft()
                
                for i in range(n):
                    if isConnected[c][i] == 1 and not visited[i]:
                        visited[i] = 1
                        q.append(i)

        ans = 0
        for i in range(n):
            if not visited[i]:
                bfs(i)
                ans += 1
        return ans
        
