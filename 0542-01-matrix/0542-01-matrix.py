class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(mat)
        m = len(mat[0])
        
        q = deque()
        dist = [[1e9] * m for _ in range(n)]
        
        for r in range(n):
            for c in range(m):
                if mat[r][c] == 0:
                    dist[r][c] = 0
                    q.append((r, c)) # 모든 0을 시작점
        
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        
        while q:
            r, c = q.popleft()
            
            for i in range(4):
                nr, nc = r + dy[i], c + dx[i]
                
                # 범위 내에 있고, 더 짧은 거리를 발견한 경우
                if 0 <= nr < n and 0 <= nc < m:
                    if dist[nr][nc] > dist[r][c] + 1:
                        dist[nr][nc] = dist[r][c] + 1
                        q.append((nr, nc))
        
        return dist
                    

