class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 큐 초기화: (현재 숫자, 단계)
        queue = deque([(0, 0)])
        visited = {0}  # 이미 방문한 숫자
        
        while queue:
            current, steps = queue.popleft()
            
            # 모든 제곱수 시도
            i = 1
            while i * i <= n:
                next_num = current + i * i
                
                # 목표 도달!
                if next_num == n:
                    return steps + 1
                
                # 아직 안 가본 곳이고, n 안 넘으면 큐에 추가
                if next_num < n and next_num not in visited:
                    visited.add(next_num)
                    queue.append((next_num, steps + 1))
                
                i += 1