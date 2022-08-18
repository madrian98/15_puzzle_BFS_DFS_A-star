from typing import List


"""Puzzle board functions"""


class BoardHelper:

    find_zero = (-1, -1)
    processed_states_len = 1
    visited_states_len = 1
    starting_board = []
    solved_board = []
    order_tab = []

    def __init__(self, order):
        self.order_tab = order  # strategy order
        self.maximum_depth = 20  # maximum recursive depth(20 set for DFS)

    # check if current board is already solved
    def is_solved(self, selected_board):
        return selected_board == self.solved_board


    def empty_value_search(self, temp):
        self.find_zero = get_index_of_value(temp, '0')

    # solving board generation
    def solved_board_generation(self, board_dimensions):
        rows, columns = board_dimensions
        board = \
        [
            [
                f'{j + i*columns + 1}'
                for j in range(columns)
            ]
            for i in range(rows)
        ]
        board[rows-1][columns-1] = '0'
        self.solved_board = board


def get_index_of_value(board: List[List], value):
    for i, row in enumerate(board):
        if value in row:
            return i, row.index(value)


