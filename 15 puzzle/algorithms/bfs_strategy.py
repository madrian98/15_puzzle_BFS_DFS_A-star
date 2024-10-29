from node import Node
from helpers.board_helper import BoardHelper
from helpers.data_structures import Queue
from typing import Tuple, List

def bfs(target: BoardHelper) -> Tuple[List[str], int]:
    """
    Perform a breadth-first search (BFS) on the given board.

    Args:
        target (BoardHelper): The board helper object containing the starting board and order tab.

    Returns:
        Tuple[List[str], int]: A tuple containing the way to solve the board and the length of the way.
    """
    maximum_depth = 0
    processed_nodes = set()
    queue = Queue()
    queue.push(Node(target.starting_board, target.order_tab))

    while len(queue) > 0:
        current_node = queue.pop()
        if len(current_node.way) > maximum_depth:
            maximum_depth = len(current_node.way)

        target.empty_value_search(current_node.board)
        current_node.remove_ways_to_out_of_board(target.find_zero)
        processed_nodes.add(current_node)

        for move in current_node.to_visit:
            current_node.make_move(move, target.find_zero, target.order_tab)
            new_node: Node = current_node.children[move]
            if new_node in processed_nodes or new_node in queue:
                continue
            queue.push(new_node)

            if not target.is_solved(new_node.board):
                continue
            target.processed_states_len = len(processed_nodes)
            target.visited_states_len = len(processed_nodes) + len(queue)
            return new_node.way, len(new_node.way)
    return -1, maximum_depth
