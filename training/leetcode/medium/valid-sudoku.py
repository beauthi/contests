class Solution:
    def countElementsInList(self, l: list) -> bool:
        count = set()
        for elt in l:
            if elt != "." and elt in count:
                return False
            count.add(elt)
        return True

    def isValidSudoku(self, board: list) -> bool:
        for line in board:
            if not self.countElementsInList(line):
                return False
        for col_idx in range(9):
            l = [line[col_idx] for line in board]
            if not self.countElementsInList(l):
                return False
        blocks = [0, 3, 6]
        for block_line in blocks:
            for block_col in blocks:
                l = set()
                for index_i in range(3):
                    for index_j in range(3):
                        if board[block_line + index_i][block_col + index_j] != "." and \
                            board[block_line + index_i][block_col + index_j] in l:
                            return False
                        l.add(board[block_line + index_i][block_col + index_j])
        return True

s = Solution()
print(s.isValidSudoku([
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]) == True)
print(s.isValidSudoku([
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]) == False)