from math import sqrt


class Sudoku(object):
    def __init__(self, data):
        self.sudoku = data
        self.n = 0
        self.block_len = 0

    def is_valid(self):
        self.n = len(self.sudoku)
        try:
            self.block_len = int(sqrt(self.n))
        except ValueError:
            return False
        if any([len(row) != self.n for row in self.sudoku]):
            return False
        return all([self._is_valid_row(i)
                    and self._is_valid_column(i)
                    and self._is_valid_block(i)
                    for i in range(self.n)])

    def _is_valid_row(self, row_num):
        return self._is_valid_set(set(self.sudoku[row_num]))

    def _is_valid_column(self, column_num):
        return self._is_valid_set(set(self.sudoku[i][column_num] for i in range(self.n)))

    def _is_valid_block(self, block_num):
        block_row_num, block_column_num = divmod(block_num, self.block_len)
        block_row, block_column = block_row_num * self.block_len, block_column_num * self.block_len
        block_set = set()
        for i in range(block_row, block_row + self.block_len):
            for j in range(block_column, block_column + self.block_len):
                block_set.add(self.sudoku[i][j])
        return self._is_valid_set(block_set)

    def _is_valid_set(self, num_set):
        return len(num_set) == self.n and max(num_set) == self.n and min(num_set) == 1 and all(type(i) is int for i in num_set)

    
x = Sudoku([
  [7,8,4,  1,5,9,  3,2,6],
  [5,3,9,  6,7,2,  8,4,1],
  [6,1,2,  4,3,8,  7,5,9],

  [9,2,8,  7,1,5,  4,6,3],
  [3,5,7,  8,4,6,  1,9,2],
  [4,6,1,  9,2,3,  5,8,7],

  [8,7,6,  3,9,4,  2,1,5],
  [2,4,3,  5,6,1,  9,7,8],
  [1,9,5,  2,8,7,  6,3,4]
])

print(x.is_valid())

