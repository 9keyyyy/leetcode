class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
            
        res = []
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        
        while top <= bottom and left <= right:
            # 1. 왼쪽 -> 오른쪽
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            top += 1 # 윗줄 탐색 완료
            
            # 2. 위 -> 아래
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1 # 오른쪽 열 탐색 완료
            
            # 중간에 경계가 역전되었는지 확인 (중요!)
            if not (top <= bottom and left <= right):
                break
                
            # 3. 오른쪽 -> 왼쪽
            for i in range(right, left - 1, -1):
                res.append(matrix[bottom][i])
            bottom -= 1 # 아랫줄 탐색 완료
            
            # 4. 아래 -> 위
            for i in range(bottom, top - 1, -1):
                res.append(matrix[i][left])
            left += 1 # 왼쪽 열 탐색 완료
            
        return res