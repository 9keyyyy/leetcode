class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        ########## DP
        dp = [n] * (n + 1)
        dp[0] = 0
        
        # 1부터 n까지 각 숫자에 대해 최소 개수 계산
        for i in range(1, n + 1):
            j = 1
            while j * j <= i:
                # i에서 제곱수(j*j)를 뺀 값의 dp + 1 중 최솟값 갱신
                dp[i] = min(dp[i], dp[i - j * j] + 1)
                j += 1
                
        return dp[n]
        ########## BFS 
        # # 큐 초기화: (현재 숫자, 단계)
        # queue = deque([(0, 0)])
        # visited = {0}  # 이미 방문한 숫자
        
        # while queue:
        #     current, steps = queue.popleft()
            
        #     # 모든 제곱수 시도
        #     i = 1
        #     while i * i <= n:
        #         next_num = current + i * i
                
        #         # 목표 도달!
        #         if next_num == n:
        #             return steps + 1
                
        #         # 아직 안 가본 곳이고, n 안 넘으면 큐에 추가
        #         if next_num < n and next_num not in visited:
        #             visited.add(next_num)
        #             queue.append((next_num, steps + 1))
                
        #         i += 1