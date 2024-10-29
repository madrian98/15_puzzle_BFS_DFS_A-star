from typing import List, Tuple

"""
Puzzle board functions.
"""

class BoardHelper:
    """
    A helper class for managing the puzzle board.
    """

    def __init__(self, order: List[str]):
        """
        Initialize the BoardHelper.

        Args:
            order (List[str]): The strategy order.
        """
        self.find_zero: Tuple[int, int] = (-1, -1)
        self.processed_states_len: int = 1
        self.visited_states_len: int = 1
        self.starting_board: List[List[str]] = []
        self.solved_board: List[List[str]] = []
        self.order_tab: List[str] = order
        self.maximum_depth: int = 20  # maximum recursive depth (20 set for DFS)

    def is_solved(self, selected_board: List[List[str]]) -> bool:
        """
        Check if the current board is already solved.

        Args:
            selected_board (List[List[str]]): The current board state.

        Returns:
            bool: True if the board is solved, False otherwise.
        """
        return selected_board == self.solved_board

    def empty_value_search(self, board: List[List[str]]) -> None:
        """
        Search for the empty value in the board.

        Args:
            board (List[List[str]]): The current board state.
        """
        self.find_zero = self.get_index_of_value(board, '0')

    def solved_board_generation(self, board_dimensions: Tuple[int, int]) -> None:
        """
        Generate the solved board configuration.

        Args:
            board_dimensions (Tuple[int, int]): The dimensions of the board (rows, columns).
        """
        rows, columns = board_dimensions
        board = [
            [f'{j + i * columns + 1}' for j in range(columns)]
            for i in range(rows)
        ]
        board[rows - 1][columns - 1] = '0'
        self.solved_board = board


    def get_index_of_value(board: List[List[str]], value: str) -> Tuple[int, int]:
        """
        Get the index of a value in the board.

        Args:
            board (List[List[str]]): The board state.
            value (str): The value to find.

        Returns:
            Tuple[int, int]: The row and column index of the value.
        """
        for i, row in enumerate(board):
            if value in row:
                return i, row.index(value)
        return -1, -1
