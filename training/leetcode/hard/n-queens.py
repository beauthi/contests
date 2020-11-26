FREE = 0
QUEEN = 1
NOT_FREE = 2


class Solution:
    def solveNQueens_rec(self, board, n, total):
        if n == 0:
            if board not in self.results:
                self.results.append(board)
        for i in range(total):
            found = False
            for j in range(total):
                if board[i][j] == FREE:
                    found = True
                    board_copy = [b[:] for b in board]
                    board_copy[i][j] = QUEEN
                    for x in range(total):
                        if board_copy[i][x] == FREE:
                            board_copy[i][x] = NOT_FREE
                        if board_copy[x][j] == FREE:
                            board_copy[x][j] = NOT_FREE
                    x, y = i - 1, j - 1
                    while x >= 0 and y >= 0:
                        board_copy[x][y] = NOT_FREE
                        x, y = x - 1, y - 1
                    x, y = i - 1, j + 1
                    while x >= 0 and y < total:
                        board_copy[x][y] = NOT_FREE
                        x, y = x - 1, y + 1
                    x, y = i + 1, j - 1
                    while x < total and y >= 0:
                        board_copy[x][y] = NOT_FREE
                        x, y = x + 1, y - 1
                    x, y = i + 1, j + 1
                    while x < total and y < total:
                        board_copy[x][y] = NOT_FREE
                        x, y = x + 1, y + 1
                    self.solveNQueens_rec(board_copy, n - 1, total)
            if not found:
                return

    def solveNQueens(self, n):
        board = [[FREE for _ in range(n)] for __ in range(n)]
        self.results = []
        self.solveNQueens_rec(board, n, n)
        formatted_results = []
        for result in self.results:
            formatted_result = []
            for line in result:
                new_line = ""
                for elt in line:
                    if elt == QUEEN:
                        new_line += "Q"
                    else:
                        new_line += "."
                formatted_result.append(new_line)
            formatted_results.append(formatted_result)
        return formatted_results


s = Solution()
for n in [9]:
    print(s.solveNQueens(n))
