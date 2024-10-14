from node import Node
from helpers.board_helper import BoardHelper
from helpers.data_structures import Stack
from typing import Tuple, List, Union

"""
Depth-First Search (DFS) algorithm for solving the 15-puzzle problem.
"""

def dfs(target: BoardHelper) -> Union[Tuple[List[str], int], Tuple[int, int]]:
    """
    Perform a Depth-First Search to solve the 15-puzzle problem.

    Args:
        target (BoardHelper): The board helper object containing the puzzle configuration.

    Returns:
        Union[Tuple[List[str], int], Tuple[int, int]]: A tuple containing the solution path and the maximum depth reached, or -1 and the maximum depth if no solution is found.
    """
    maximum_depth = 0
    stack = Stack()
    processed_state = set()
    unprocessed = set()
    current_depth = {}
    stack.push(Node(target.starting_board, target.order_tab))

    while len(stack) > 0:
        selected_node = stack.pop()
        node_hash = hash(selected_node)

        if selected_node in processed_state and len(selected_node.way) >= current_depth[node_hash]:
            continue

        current_depth[node_hash] = len(selected_node.way)
        if len(selected_node.way) > maximum_depth:
            maximum_depth = len(selected_node.way)

        if len(selected_node.way) == target.maximum_depth:
            unprocessed.add(selected_node)
            continue

        target.empty_value_search(selected_node.board)
        selected_node.remove_ways_to_out_of_board(target.find_zero)
        processed_state.add(selected_node)

        for move in selected_node.to_visit[::-1]:
            selected_node.make_move(move, target.find_zero, target.order_tab)
            new_node: Node = selected_node.children[move]
            stack.push(new_node)

            if not target.is_solved(new_node.board):
                continue

            target.processed_states_len = len(processed_state)
            visited_nodes = processed_state.union(unprocessed).union(stack)
            target.visited_states_len = len(visited_nodes)

            if len(new_node.way) > maximum_depth:
                maximum_depth = len(new_node.way)

            return new_node.way, maximum_depth

    return -1, maximum_depth
