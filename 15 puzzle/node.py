from typing import List, Dict, Tuple

"""
Node class for the 15-puzzle problem.
"""

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

class Node:
    """
    A class representing a node in the puzzle search tree.
    """

    def __init__(self, current_board: List[List[int]], order: List[str], way: List[str] = None):
        """
        Initialize a Node.

        Args:
            current_board (List[List[int]]): The current board state.
            order (List[str]): The order of moves.
            way (List[str], optional): The path taken to reach this node. Defaults to None.
        """
        self.board: List[List[int]] = current_board
        self.way: List[str] = way.copy() if way else []
        self.children: Dict[str, Node] = {}
        self.calc_f: int = 0
        self.to_visit: List[str] = order.copy()
        if way:
            self.to_visit.remove(REVERSE_MOVEMENT_MAP[way[-1]])

    def __lt__(self, other: 'Node') -> bool:
        """
        Compare nodes based on their calculated f value.

        Args:
            other (Node): The other node to compare.

        Returns:
            bool: True if this node's f value is less than the other node's f value, False otherwise.
        """
        return self.calc_f < other.calc_f

    def __eq__(self, other: object) -> bool:
        """
        Check if two nodes are equal based on their board state.

        Args:
            other (object): The other node to compare.

        Returns:
            bool: True if the nodes are equal, False otherwise.
        """
        if not isinstance(other, Node):
            return False
        return all(row1 == row2 for row1, row2 in zip(self.board, other.board))

    def __hash__(self) -> int:
        """
        Get the hash value of the node based on its board state.

        Returns:
            int: The hash value of the node.
        """
        return hash(tuple(tuple(cell for cell in row) for row in self.board))

    def __repr__(self) -> str:
        """
        Get a string representation of the node.

        Returns:
            str: The string representation of the node.
        """
        return ''.join([' '.join([str(cell) for cell in row]) + '\n' for row in self.board])

    def remove_ways_to_out_of_board(self, zero_position: Tuple[int, int]) -> None:
        """
        Remove moves that go out of the board.

        Args:
            zero_position (Tuple[int, int]): The position of the zero (empty space) on the board.
        """
        remove_way = []
        check_first_row = zero_position[0] == 0
        check_last_row = zero_position[0] == len(self.board) - 1
        check_first_col = zero_position[1] == 0
        check_last_col = zero_position[1] == len(self.board[0]) - 1

        if check_first_row:
            remove_way.append('U')
        elif check_last_row:
            remove_way.append('D')

        if check_first_col:
            remove_way.append('L')
        elif check_last_col:
            remove_way.append('R')

        for rem in remove_way:
            if rem in self.to_visit:
                self.to_visit.remove(rem)

    def create_child(self, board_after_move: List[List[int]], move: str, order: List[str]) -> None:
        """
        Create a child node after making a move.

        Args:
            board_after_move (List[List[int]]): The board state after the move.
            move (str): The move made.
            order (List[str]): The order of moves.
        """
        path = self.way + [move]
        child = Node(board_after_move, order, path)
        self.children[move] = child

    def make_move(self, move: str, empty: Tuple[int, int], order: List[str]) -> None:
        """
        Make a move on the board.

        Args:
            move (str): The move to make.
            empty (Tuple[int, int]): The position of the empty space.
            order (List[str]): The order of moves.
        """
        def swap_elements(board: List[List[int]], p1: Tuple[int, int], p2: Tuple[int, int]) -> None:
            """
            Swap two elements on the board.

            Args:
                board (List[List[int]]): The board state.
                p1 (Tuple[int, int]): The position of the first element.
                p2 (Tuple[int, int]): The position of the second element.
            """
            board[p1[0]][p1[1]], board[p2[0]][p2[1]] = board[p2[0]][p2[1]], board[p1[0]][p1[1]]

        x, y = empty
        d_xy = MOVEMENT_MAP[move]

        temp_array = [row.copy() for row in self.board]

        swap_elements(temp_array, (x, y), (x + d_xy[0], y + d_xy[1]))
        self.create_child(temp_array, move, order)