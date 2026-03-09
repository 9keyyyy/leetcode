class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(heights)
        m = len(heights[0])

        success = [[0]*m for _ in range(n)]
        success[0][m-1] = success[n-1][0] = 1
        
        def is_atl(y, x):
            return y == n-1 or x == m-1

        def is_pac(y, x):
            return y == 0 or x == 0

        dx = [-1, 0, 0, 1]
        dy = [0, -1, 1, 0]
        visited = [[0]*m for _ in range(n)]

        def bfs(b, a):
            q = deque()
            q.append((b, a))
            visited[b][a] = 1

            a = p = 0
            while q:
                y, x = q.popleft()
                
                if is_atl(y, x):
                    a = 1
                if is_pac(y, x):
                    p = 1
                
                if a and p:
                    return True

                for i in range(4):
                    ny = y + dy[i]
                    nx = x + dx[i]

                    if nx < 0 or nx >= m or ny < 0 or ny >= n:
                        continue

                    # if heights[ny][nx] > heights[y][x] and success[ny][nx] == 1:
                    #     return True

                    if heights[ny][nx] > heights[y][x] or visited[ny][nx]:
                        continue
                    
                    visited[ny][nx] = 1
                    q.append((ny, nx))
                    
            return False



        ans = []
        for i in range(n):
            for j in range(m):
                if success[i][j] != 1:
                    visited = [[0]*m for _ in range(n)]
                    res = bfs(i, j)
                    if not res:
                        success[i][j] = -1
                    else: 
                        success[i][j] = 1

        for i in range(n):
            for j in range(m):
                if success[i][j] == 1:
                    ans.append([i, j])

        return ans