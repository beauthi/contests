class Solution:
    def firstSolution(self, matrix: list) -> None:
        new_matrix = []
        for x in range(len(matrix)):
            m = []
            for y in range(len(matrix)):
                m.append(0)
            new_matrix.append(m)
        for index_x in range(len(matrix)):
            for index_y in range(len(matrix)):
                new_matrix[index_y][len(matrix) - index_x - 1] = matrix[index_x][index_y]
        for index_x in range(len(matrix)):
            for index_y in range(len(matrix)):
                matrix[index_x][index_y] = new_matrix[index_x][index_y]
    def rotate(self, matrix: list) -> None:
        for index_x in range(len(matrix) - 1):
            for index_y in range(index_x, len(matrix) - index_x - 1):
                matrix[index_x][index_y], matrix[len(matrix) - index_y - 1][index_x], \
                    matrix[len(matrix) - index_x - 1][len(matrix) - index_y - 1], matrix[index_y][len(matrix) - index_x - 1] = \
                        matrix[len(matrix) - index_y - 1][index_x], matrix[len(matrix) - index_x - 1][len(matrix) - index_y - 1], \
                            matrix[index_y][len(matrix) - index_x - 1], matrix[index_x][index_y]

s = Solution()
l = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
s.rotate(l)
print(l)
l = [
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
]
s.rotate(l)
print(l)