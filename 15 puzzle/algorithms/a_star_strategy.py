from typing import List
from node import Node
from helpers.board_helper import BoardHelper, get_index_of_value
from queue import PriorityQueue

"""A* algorithm initialised with algorithm parameters."""

"""

"""



def astr(target: BoardHelper, heuristic):
    maximum_depth = 0
    get_method_cost = calculate_cost(heuristic)
    open_list = PriorityQueue()
    closed_list = set()
    open_list.put(Node(target.starting_board, target.order_tab))

    while not open_list.empty():
        selected_node: Node = open_list.get()
        if len(selected_node.way) > maximum_depth:
            maximum_depth = len(selected_node.way)

        if target.is_solved(selected_node.board):
            target.processed_states_len = len(closed_list)
            queue_elements = set([selected_node])
            while not open_list.empty():
                queue_elements.add(open_list.get())
            target.visited_states_len = len(closed_list) + len(queue_elements)
            return selected_node.way, maximum_depth

        closed_list.add(selected_node)
        target.empty_value_search(selected_node.board)
        selected_node.remove_ways_to_out_of_board(target.find_zero)

        for move in selected_node.to_visit:
            selected_node.make_move(move, target.find_zero, target.order_tab)
            new_node: Node = selected_node.children[move]
            if new_node in closed_list:
                continue

            calc_g = get_method_cost(target.starting_board, new_node.board)
            calc_h = get_method_cost(new_node.board, target.solved_board)
            new_node.calc_f = calc_g + calc_h
            open_list.put(new_node)
    return -1, maximum_depth


def distance_list(current_board: List[List], target_board: List[List]):
    dist_list = [sum([
        abs(current_brd - target_brd)
        for current_brd, target_brd in zip((row_index, column_index), get_index_of_value(target_board, val))
        if val != '0'
    ])
        for row_index, row in enumerate(current_board)
        for column_index, val in enumerate(row)
    ]
    return dist_list

def manhattan_cost(current_board: List[List], target_board: List[List]):
    return sum(distance_list(current_board, target_board))

def hamming_cost(current_board: List[List], target_board: List[List]):
    return sum([
        val != 0 for val in distance_list(current_board, target_board)
    ]
    )


def calculate_cost(heuristic: str):
    return manhattan_cost if heuristic == 'manh' else hamming_cost
