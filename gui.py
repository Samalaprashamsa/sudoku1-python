import tkinter as tk
from tkinter import messagebox
from util import scale_font_size
from sudoku import Sudoku

class SudokuGUI:
    def __init__(self, sudoku):
        self.sudoku = sudoku
        self.font_size = 18

        self.window = tk.Tk()
        self.window.title("Sudoku")
        self.create_board()

    def create_board(self):
        self.cells = []
        for row in range(9):
            row_cells = []
            for col in range(9):
                value = self.sudoku.get_value(row, col)
                if value != 0:
                    cell = tk.Label(
                        self.window,
                        text=str(value),
                        font=("Arial", self.font_size),
                        width=2,
                        relief=tk.RAISED,
                        padx=10,
                        pady=10
                    )
                else:
                    cell = tk.Entry(
                        self.window,
                        font=("Arial", self.font_size),
                        width=2,
                        justify='center'
                    )
                cell.grid(row=row, column=col)
                row_cells.append(cell)
            self.cells.append(row_cells)

        check_button = tk.Button(
            self.window,
            text="Check",
            font=("Arial", self.font_size),
            command=self.check
        )
        check_button.grid(row=9, column=0, columnspan=3, pady=10)

        solve_button = tk.Button(
            self.window,
            text="Solve",
            font=("Arial", self.font_size),
            command=self.solve
        )
        solve_button.grid(row=9, column=3, columnspan=3, pady=10)

    def check(self):
        self.update_board()
        if self.validate_solution():
            messagebox.showinfo("Sudoku Checker", "All entries are correct!")
        else:
            messagebox.showwarning("Sudoku Checker", "Some entries are incorrect.")

    def validate_solution(self):
        for row in range(9):
            for col in range(9):
                cell = self.cells[row][col]
                if isinstance(cell, tk.Entry):
                    value = cell.get()
                    if value.isdigit():
                        if not self.sudoku.is_valid(row, col, int(value)):
                            return False
        return True

    def solve(self):
        self.update_board()
        if self.sudoku.solve():
            self.display_board()
        else:
            messagebox.showinfo("Sudoku Solver", "No solution found.")

    def update_board(self):
        for row in range(9):
            for col in range(9):
                cell = self.cells[row][col]
                if isinstance(cell, tk.Entry):
                    value = cell.get()
                    if value.isdigit():
                        self.sudoku.set_value(row, col, int(value))
                    else:
                        self.sudoku.set_value(row, col, 0)

    def display_board(self):
        for row in range(9):
            for col in range(9):
                cell = self.cells[row][col]
                if isinstance(cell, tk.Entry):
                    value = self.sudoku.get_value(row, col)
                    cell.delete(0, tk.END)
                    cell.insert(0, str(value) if value != 0 else "")

    def run(self):
        self.window.mainloop()
