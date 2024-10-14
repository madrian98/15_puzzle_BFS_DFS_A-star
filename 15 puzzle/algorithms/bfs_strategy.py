from node import Node
from helpers.board_helper import BoardHelper
from helpers.data_structures import Queue

"""BFS algorithm"""


def bfs(target: BoardHelper):
    maximum_depth = 0
    process = set()
    queue = Queue()
    queue.push(Node(target.starting_board, target.order_tab))

    while len(queue) > 0:
        processed_node = queue.pop()
        if len(processed_node.way) > maximum_depth:
            maximum_depth = len(processed_node.way)

        target.empty_value_search(processed_node.board)
        processed_node.remove_ways_to_out_of_board(target.find_zero)
        process.add(processed_node)

        for move in processed_node.to_visit:
            processed_node.make_move(move, target.find_zero, target.order_tab)
            new_node: Node = processed_node.children[move]
            if new_node in process or new_node in queue:
                continue
            queue.push(new_node)

            if not target.is_solved(new_node.board):
                continue
            target.processed_states_len = len(process)
            target.visited_states_len = len(process) + len(queue)
            return new_node.way, len(new_node.way)
    return -1, maximum_depth
