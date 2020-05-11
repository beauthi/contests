class Solution:
    def print(self, board: list) -> None:
        for line in board:
            for elt in line:
                print(elt, end=" ")
            print("")
        print("-" * 17)

    def isValid(self, board) -> bool:
        for index_line in range(3):
            for index_col in range(3):
                block = [l[index_col * 3 : index_col * 3 + 3] for l in board[index_line * 3 : index_line * 3 + 3]]
                if "." in block:
                    return False
                for i in range(9):
                    if not any(str(i + 1) in l for l in block):
                        return False
        for line in board:
            if "." in line:
                return False
            for i in range(9):
                if str(i + 1) not in line:
                    return False
        for col in range(9):
            c = [l[col] for l in board]
            if "." in c:
                return False
            for i in range(9):
                if str(i + 1) not in c:
                    return False
              
        return True

    def solve(self, board):
        for x in range(9):
            for y in range(9):
                if board[x][y] != ".":
                    continue
                block = [l[int(y / 3) * 3 : int(y / 3) * 3 + 3] for l in board[int(x / 3) * 3 : int(x / 3) * 3 + 3]]
                line = board[x]
                col = [l[y] for l in board]
                found = False
                for i in range(9):
                    if any(str(i + 1) in l for l in block) or str(i + 1) in line or str(i + 1) in col:
                        continue
                    board[x][y] = str(i + 1)
                    if not self.solve(board):
                        board[x][y] = "."
                    else:
                        found = True
                        break
                if not found:
                    return False
        return self.isValid(board)

    def solveSudoku(self, board: list) -> None:
        self.solve(board)
s = Solution()
s.solveSudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]])
s.solveSudoku([[".",".","9","7","4","8",".",".","."],["7",".",".",".",".",".",".",".","."],[".","2",".","1",".","9",".",".","."],[".",".","7",".",".",".","2","4","."],[".","6","4",".","1",".","5","9","."],[".","9","8",".",".",".","3",".","."],[".",".",".","8",".","3",".","2","."],[".",".",".",".",".",".",".",".","6"],[".",".",".","2","7","5","9",".","."]])