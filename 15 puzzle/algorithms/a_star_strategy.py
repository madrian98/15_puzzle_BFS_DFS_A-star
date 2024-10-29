from node import Node
from helpers.board_helper import BoardHelper, get_index_of_value
from helpers.data_structures import PriorityQueue
from typing import Tuple, List

"""
A* Search algorithm for solving the 15-puzzle problem.
"""

def a_star(target: BoardHelper) -> Tuple[List[str], int]:
    """
    Perform an A* search on the given board.

    Args:
        target (BoardHelper): The board helper object containing the starting board and order tab.

    Returns:
        Tuple[List[str], int]: A tuple containing the way to solve the board and the length of the way.
    """
    maximum_depth = 0
    processed_nodes = set()
    priority_queue = PriorityQueue()
    priority_queue.push(Node(target.starting_board, target.order_tab))

    while len(priority_queue) > 0:
        current_node = priority_queue.pop()
        if len(current_node.way) > maximum_depth:
            maximum_depth = len(current_node.way)

        target.empty_value_search(current_node.board)
        current_node.remove_ways_to_out_of_board(target.find_zero)
        processed_nodes.add(current_node)

        for move in current_node.to_visit:
            current_node.make_move(move, target.find_zero, target.order_tab)
            new_node: Node = current_node.children[move]
            if new_node in processed_nodes or new_node in priority_queue:
                continue
            priority_queue.push(new_node)

            if not target.is_solved(new_node.board):
                continue
            target.processed_states_len = len(processed_nodes)
            target.visited_states_len = len(processed_nodes) + len(priority_queue)
            return new_node.way, len(new_node.way)
    return -1, maximum_depth


def distance_list(current_board: List[List[str]], target_board: List[List[str]]) -> List[int]:
    """
    Calculate the Manhattan distance for each tile in the current board compared to the target board.

    Args:
        current_board (List[List[str]]): The current board state.
        target_board (List[List[str]]): The target board state.

    Returns:
        List[int]: A list of Manhattan distances for each tile.
    """
    dist_list = [
        sum([
            abs(current_brd - target_brd)
            for current_brd, target_brd in zip((row_index, column_index), get_index_of_value(target_board, val))
            if val != '0'
        ])
        for row_index, row in enumerate(current_board)
        for column_index, val in enumerate(row)
    ]
    return dist_list


def manhattan_cost(current_board: List[List[str]], target_board: List[List[str]]) -> int:
    """
    Calculate the Manhattan cost between the current board and the target board.

    Args:
        current_board (List[List[str]]): The current board state.
        target_board (List[List[str]]): The target board state.

    Returns:
        int: The Manhattan cost.
    """
    return sum(distance_list(current_board, target_board))


def hamming_cost(current_board: List[List[str]], target_board: List[List[str]]) -> int:
    """
    Calculate the Hamming cost between the current board and the target board.

    Args:
        current_board (List[List[str]]): The current board state.
        target_board (List[List[str]]): The target board state.

    Returns:
        int: The Hamming cost.
    """
    return sum([
        val != 0 for val in distance_list(current_board, target_board)
    ])


def calculate_cost(heuristic: str):
    """
    Calculate the cost based on the given heuristic.

    Args:
        heuristic (str): The heuristic to use ('manh' for Manhattan, otherwise Hamming).

    Returns:
        function: The cost calculation function.
    """
    return manhattan_cost if heuristic == 'manh' else hamming_cost
