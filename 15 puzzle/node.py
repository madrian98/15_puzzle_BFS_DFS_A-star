from typing import List


"""Node class / Movement maps"""


class Node:

    def __init__(self, current_board, order: List, way: List = None):
        self.board: List[List] = current_board
        self.way: List = way.copy() if way else []
        self.children = {}
        self.calc_f = 0
        self.to_visit: List = order.copy()
        if way:
            self.to_visit.remove(REVERSE_MOVEMENT_MAP[way[-1]])

    #less than
    def __lt__(self, obj) -> bool:
        obj: Node = obj
        return self.calc_f < obj.calc_f

    # checking if instance exists as well as if board and its boxes are the same
    def __eq__(self, obj: object) -> bool:
        if not isinstance(obj, Node):
            return False
        obj: Node = obj
        return all(l1 == l2 for l1, l2 in zip(obj.board, self.board))

    # returns unique object id if boards are equal
    def __hash__(self):
        return hash(tuple(tuple(entr for entr in row) for row in self.board))

    #class objects as a string
    def __repr__(self) -> str:
        return ''.join([
            ' '.join([str(entr) for entr in row]) + '\n'
            for row in self.board])

    # Remove illegal moves
    def remove_ways_to_out_of_board(self, find_zero):
        remove_way = []
        check_first_row = find_zero[0] == 0
        check_last_row = find_zero[0] == len(self.board) - 1
        check_first_col = find_zero[1] == 0
        check_last_col = find_zero[1] == len(self.board[0]) - 1

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

    #children after making move
    def create_child(self, board_after_move, move: str, order):
        path = self.way + [move]
        child = Node(board_after_move, order, path)
        self.children[move] = child

    # make a move and swap elements
    def make_move(self, move, empty, order):
        def swap_elements(board, p1, p2):
            board[p1[0]][p1[1]], board[p2[0]][p2[1]] = board[p2[0]][p2[1]], board[p1[0]][p1[1]]

        x, y = empty
        d_xy = MOVEMENT_MAP[move]

        temp_array = []
        for row in self.board:
            temp_array.append(row.copy())

        swap_elements(temp_array, (x, y), (x + d_xy[0], y + d_xy[1]))
        self.create_child(temp_array, move, order)


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
