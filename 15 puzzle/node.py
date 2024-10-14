from typing import List


"""
Node class for the 15-puzzle problem.
"""


class Node:
    """
    A class representing a node in the puzzle search tree.
    """

    def __init__(self, board, order_tab):
        """
        Initialize a Node.

        Args:
            board (list): The board state.
            order_tab (list): The order of moves.
        """
        self.board = board
        self.order_tab = order_tab
        self.way = []
        self.children = {}
        self.to_visit = []

    def remove_ways_to_out_of_board(self, find_zero):
        """
        Remove moves that go out of the board.

        Args:
            find_zero (function): Function to find the zero position.
        """
        # Implementation here

    def make_move(self, move, find_zero, order_tab):
        """
        Make a move on the board.

        Args:
            move (str): The move to make.
            find_zero (function): Function to find the zero position.
            order_tab (list): The order of moves.
        """
        # Implementation here


# Movement map
MOVEMENT_MAP = {
    'U': (-1, 0),
    'D': (1, 0),
    'L': (0, -1),
    'R': (0, 1)
}

# Reverse movement map
REVERSE_MOVEMENT_MAP = {
    'U': 'D',
    'D': 'U',
    'L': 'R',
    'R': 'L'
}
