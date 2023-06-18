class Sudoku:
    def __init__(self):
        self.board = None

    def load_board(self, filename):
        with open(filename, "r") as file:
            lines = file.readlines()
            self.board = [[int(num) for num in line.split()] for line in lines]

    def get_value(self, row, col):
        return self.board[row][col]

    def set_value(self, row, col, value):
        self.board[row][col] = value

    def is_valid(self, row, col, value):
        # Check row
        for c in range(9):
            if self.board[row][c] == value:
                return False

        # Check column
        for r in range(9):
            if self.board[r][col] == value:
                return False

        # Check 3x3 box
        start_row = (row // 3) * 3
        start_col = (col // 3) * 3
        for r in range(start_row, start_row + 3):
            for c in range(start_col, start_col + 3):
                if self.board[r][c] == value:
                    return False

        return True

    def solve(self):
        empty_cell = self.find_empty_cell()
        if not empty_cell:
            return True

        row, col = empty_cell
        for num in range(1, 10):
            if self.is_valid(row, col, num):
                self.set_value(row, col, num)
                if self.solve():
                    return True
                self.set_value(row, col, 0)

        return False

    def find_empty_cell(self):
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == 0:
                    return row, col

        return None
