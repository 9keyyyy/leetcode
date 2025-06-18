class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        dx = [-1, 0, 0, 1]
        dy = [0, 1, -1, 0]

        m = len(board[0])
        n = len(board)

        visited = [[0]*m for _ in range(n)]
        def dfs(y, x, idx):
            if idx == len(word)-1:
                return True
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or nx >= m or ny < 0 or ny >= n:
                    continue

                if word[idx+1] == board[ny][nx] and not visited[ny][nx]:
                    visited[ny][nx] = 1
                    if dfs(ny, nx, idx+1):
                        return True
                    visited[ny][nx] = 0
            
            return False


        for i in range(n):
            for j in range(m):
                if word[0] == board[i][j]:
                    visited[i][j]=1
                    if dfs(i, j, 0):
                        return True
                    visited[i][j]=0

        return False

                
