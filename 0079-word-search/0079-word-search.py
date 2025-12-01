class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        n = len(board)
        m = len(board[0])
        dx = [-1, 0, 0, 1]
        dy = [0, -1, 1, 0]
        visited = [[0]*m for _ in range(n)]

        def dfs(y, x, cur):
            cur += board[y][x]
            if cur == word:
                print(cur, word, visited)
                return True
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or nx >= m or ny < 0 or ny >= n or visited[ny][nx]:
                    continue
                if cur + board[ny][nx] != word[:len(cur)+1]:
                    continue
                visited[ny][nx] = 1
                if dfs(ny, nx, cur):
                    return True
                visited[ny][nx] = 0
            
            return False

        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    visited[i][j] = 1
                    if dfs(i, j, ""):
                        return True
                    visited[i][j] = 0
        
        return False   
        