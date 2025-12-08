class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        n = len(board)
        m = len(board[0])
        visited = [[0]*m for _ in range(n)]

        def bfs(a, b):
            dx = [-1, 0, 0, 1]
            dy = [0, -1, 1, 0]
            visited[a][b] = 1

            q = deque([(a, b)])
            while q:
                y, x = q.popleft()

                for i in range(4):
                    ny = y + dy[i]
                    nx = x + dx[i]

                    if nx < 0 or nx >= m or ny < 0 or ny >= n or visited[ny][nx]:
                        continue
                    if board[ny][nx] == "O":
                        visited[ny][nx] = 1
                        q.append((ny, nx))
            

        for i in range(n):
            if board[i][0] == "O" and not visited[i][0]:
                bfs(i, 0)
            if board[i][m-1] == "O" and not visited[i][m-1]:
                bfs(i, m-1)

        for j in range(m):
            if board[0][j] == "O" and not visited[0][j]:
                bfs(0, j)
            if board[n-1][j] == "O" and not visited[n-1][j]:
                bfs(n-1, j)
        
        for i in range(n):
            for j in range(m):
                if not visited[i][j]:
                    board[i][j] = "X"

        return board



        