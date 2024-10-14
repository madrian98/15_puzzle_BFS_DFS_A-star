from algorithms.a_star_strategy import a_star
from algorithms.bfs_strategy import bfs
from algorithms.dfs_strategy import dfs
from validators.input_validator import Validator
from helpers.strategy_methods import BFS_DFS_Methods
from time import time_ns
from helpers.board_helper import BoardHelper

"""
Main program for solving the 15-puzzle problem using different search strategies.
"""

def main():
    """
    Main function to run the 15-puzzle solver.
    """
    val = Validator()
    if not val.final_validator():
        return

    order = list(val.strategy) if val.option == 0 else BFS_DFS_Methods['data']
    board_helper = BoardHelper(order)

    # getting initial board
    with open(val.source) as input_board:
        board_helper.solved_board_generation(
            list(map(int, input_board.readline().split()))
        )
        for line in input_board:
            board_helper.starting_board.append(line.split())

    # Example BFS
    if val.method == 'bfs':
        bfs_solution, bfs_depth = bfs(board_helper)
        statistics = [bfs_solution, bfs_depth]
    # Example DFS
    elif val.method == 'dfs':
        dfs_solution, dfs_depth = dfs(board_helper)
        statistics = [dfs_solution, dfs_depth]
    # Example A*
    else:
        a_star_solution, a_star_depth = a_star(board_helper)
        statistics = [a_star_solution, a_star_depth]

    initialization_time = time_ns()
    elapsed_time = time_ns() - initialization_time
    statistics = [statistics[0]] + [board_helper.visited_states_len, board_helper.processed_states_len] + [statistics[1]]
    result_files(statistics, val.solution_file, val.stat_file, elapsed_time)


def result_files(statistics, solution_file, statistic_file, elapsed_time):

    path, *additional_statistics = statistics
    solution_length = len(path) if path != -1 else -1

    file = open(solution_file, 'w')

    file.write(str(solution_length))
    if path != -1:
        file.write('\n')
        file.write(''.join(path))
    file.close()

    file = open(statistic_file, 'w')
    file.write(str(solution_length))

    additional_statistics += [round(elapsed_time * 0.000001, 3)]  # NANO_TO_MILI

    for sts in additional_statistics:
        file.write('\n')
        file.write(str(sts))
    file.close()


if __name__ == "__main__":
    main()
