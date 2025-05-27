class Solution(object):
    def isValidRec(self, y, x, board):
        cur = {}
        for i in range(3):
            for j in range(3):
                if board[y+i][x+j] == ".":
                    continue
                if board[y+i][x+j] in cur:
                    return False
                else:
                    cur[board[y+i][x+j]] = 1
        return True


    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                if not self.isValidRec(i, j, board):
                    return False
        
        for i in range(9):
            cur = {}
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in cur:
                    return False
                else:
                    cur[board[i][j]] = 1

        for i in range(9):
            cur = {}
            for j in range(9):
                if board[j][i] == ".":
                    continue
                if board[j][i] in cur:
                    return False
                else:
                    cur[board[j][i]] = 1
        
        return True