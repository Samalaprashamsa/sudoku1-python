from sudoku import Sudoku
from gui import SudokuGUI

def main():
    # Create a Sudoku board
    board = Sudoku()

    # Load the board configuration from file
    board.load_board("board.txt")

    # Create the Sudoku GUI and pass the board
    gui = SudokuGUI(board)

    # Run the GUI
    gui.run()

if __name__ == "__main__":
    main()
