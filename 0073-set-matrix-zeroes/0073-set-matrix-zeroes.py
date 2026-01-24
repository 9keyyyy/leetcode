class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        first_row_zero = False
        first_col_zero = False
        
        # 1) 첫 행/열에 원래 0이 있는지 먼저 체크
        for j in range(n):
            if matrix[0][j] == 0:
                first_row_zero = True
        for i in range(m):
            if matrix[i][0] == 0:
                first_col_zero = True
        
        # 2) 나머지 영역 순회하며 마킹
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0  # 행 마커
                    matrix[0][j] = 0  # 열 마커
        
        # 3) 마커 보고 0으로 채우기
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        # 4) 첫 행/열 처리
        if first_row_zero:
            for j in range(n):
                matrix[0][j] = 0
        if first_col_zero:
            for i in range(m):
                matrix[i][0] = 0