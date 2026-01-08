class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        m = len(grid[0])

        visited = [[0]*m for _ in range(n)]

        def bfs(b, a):
            q = deque([(b, a)])
            visited[b][a] = 1
            dx = [-1, 0, 0, 1]
            dy = [0, -1, 1, 0]

            cur_m = 1
            while q:
                y, x = q.popleft()

                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]

                    if nx < 0 or nx >= m or ny < 0 or ny >= n or visited[ny][nx]:
                        continue
                    if grid[ny][nx]:
                        visited[ny][nx] = 1
                        cur_m += 1
                        q.append((ny, nx))

            return cur_m

        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] and not visited[i][j]:
                    ans = max(ans, bfs(i, j))

        return ans
