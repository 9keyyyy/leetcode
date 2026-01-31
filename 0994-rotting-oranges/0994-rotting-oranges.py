class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        m = len(grid[0])
        dx = [-1, 0, 0, 1]
        dy = [0,  -1, 1, 0]
        visited = [[0]*m for _ in range(n)]

        def bfs(b, a):
            q = deque([(b, a)])
            visited[b][a] = 1

            while q:
                y, x = q.popleft()

                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]

                    if nx >= m or nx < 0 or ny >= n or ny < 0:
                        continue
                    if grid[ny][nx] == 0 or  grid[ny][nx] == 2 or visited[ny][nx]:
                        continue

                    visited[ny][nx] = 1
                    if grid[ny][nx] == 1:
                        grid[ny][nx] = grid[y][x] + 1
                    else:
                        grid[ny][nx] = min(grid[ny][nx], grid[y][x] + 1)

                    
                    q.append((ny, nx))

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    visited = [[0]*m for _ in range(n)]
                    bfs(i, j)
        
        print(grid)

        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return -1
                ans = max(ans, grid[i][j] - 2)
        
        return ans
                    