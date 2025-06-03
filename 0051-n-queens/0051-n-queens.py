class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        cur = [[0]*n, [0]*n, [0]*(2*n-1), [0]*(2*n-1)] # 세로, 가로, 대각선1, 대각선2
        ans = []
        q_dir = []

        def dfs(cy, cx):
            if len(q_dir) == n:
                ans.append(q_dir[:])
                return

            for y in range(cy, n):
                for x in range(n):
                    if cur[0][y]:   # 세로
                        continue
                    if cur[1][x]:   # 가로
                        continue
                    if cur[2][-y+x+n-1]:  # 대각선1
                        continue
                    if cur[3][y+x]:  # 대각선1
                        continue

                    cur[0][y] = 1
                    cur[1][x] = 1
                    cur[2][-y+x+n-1] = 1
                    cur[3][y+x] = 1
                    q_dir.append([y, x])


                    if x == n-1:
                        dfs(y+1, 0)
                    else:
                        dfs(y, x+1)
                    
                    cur[0][y] = 0
                    cur[1][x] = 0
                    cur[2][-y+x+n-1] = 0
                    cur[3][y+x] = 0
                    q_dir.pop()

        dfs(0, 0)
        res = []
        for a in ans:
            cur_res = [["."]*n for _ in range(n)]
            for c in a:
                cur_res[c[0]][c[1]] = 'Q'
            
            tmp = []
            for i in range(n):
                line = "".join(cur_res[i])
                tmp.append(line)
            res.append(tmp)

        return res
