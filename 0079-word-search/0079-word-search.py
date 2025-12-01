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
            if cur == word:
                return True
            if cur != word[:len(cur)]:
                return False
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or nx >= m or ny < 0 or ny >= n or visited[ny][nx]:
                    continue
                visited[ny][nx] = 1
                if dfs(ny, nx, cur+board[ny][nx]):
                    return True
                visited[ny][nx] = 0
            
            return False

        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    visited[i][j] = 1
                    if dfs(i, j, word[0]):
                        return True
                    visited[i][j] = 0
        
        return False   
        