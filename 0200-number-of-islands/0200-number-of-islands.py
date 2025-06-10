class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        dx = [-1, 0, 0, 1]
        dy = [0, -1, 1, 0]

        m = len(grid[0])
        n = len(grid)
        visited = [[0]*m for _ in range(n)]

        def bfs(i, j):
            q = deque()
            q.append([i, j])
            while q:
                y, x = q.popleft()
                
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]

                    if nx >= m or nx < 0 or ny < 0 or ny >= n:
                        continue
                    
                    if not visited[ny][nx] and grid[ny][nx] == "1":
                        visited[ny][nx] = 1
                        q.append([ny, nx])

        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1" and not visited[i][j]:
                    bfs(i, j)
                    ans += 1

        return ans