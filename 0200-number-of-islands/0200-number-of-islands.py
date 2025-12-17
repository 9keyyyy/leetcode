class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        n = len(grid)
        m = len(grid[0])
        visited = [[0]*m for _ in range(n)]

        def bfs(b, a):
            dx = [-1, 0, 0, 1]
            dy = [0, -1, 1, 0]

            q = deque([(b, a)])

            while q:
                y, x = q.popleft()

                for i in range(4):
                    ny = y + dy[i]
                    nx = x + dx[i]

                    if ny < 0 or ny >= n or nx < 0 or nx >= m:
                        continue
                    if visited[ny][nx]:
                        continue

                    if grid[ny][nx] == "1":
                        visited[ny][nx] = 1
                        q.append((ny, nx))

        ans = 0
        for i in range(n):
            for j in range(m):
                if not visited[i][j] and grid[i][j] == "1":
                    visited[i][j] = 1
                    ans += 1
                    bfs(i, j)

        return ans