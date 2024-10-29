from algorithms.a_star_strategy import a_star
from algorithms.bfs_strategy import bfs
from algorithms.dfs_strategy import dfs
from validators.input_validator import Validator
from helpers.strategy_methods import STRATEGY_METHODS
from time import time_ns
from helpers.board_helper import BoardHelper
from typing import List, Tuple, Union

"""
Main program for solving the 15-puzzle problem using different search strategies.
"""

def main() -> None:
    """
    Main function to run the 15-puzzle solver.
    """
    validator = Validator()
    if not validator.final_validator():
        return

    order = list(validator.strategy) if validator.option == 0 else STRATEGY_METHODS[0]['data']
    board_helper = BoardHelper(order)

    # Getting initial board
    with open(validator.source) as input_board:
        board_helper.solved_board_generation(
            tuple(map(int, input_board.readline().split()))
        )
        for line in input_board:
            board_helper.starting_board.append(line.split())

    # Select and run the appropriate algorithm
    if validator.method == 'bfs':
        solution, depth = bfs(board_helper)
    elif validator.method == 'dfs':
        solution, depth = dfs(board_helper)
    else:
        solution, depth = a_star(board_helper)

    initialization_time = time_ns()
    elapsed_time = time_ns() - initialization_time
    statistics = [solution, board_helper.visited_states_len, board_helper.processed_states_len, depth]
    write_result_files(statistics, validator.solution_file, validator.stat_file, elapsed_time)


def write_result_files(statistics: List[Union[List[str], int]], solution_file: str, statistic_file: str, elapsed_time: int) -> None:
    """
    Write the results to the solution and statistic files.

    Args:
        statistics (List[Union[List[str], int]]): The statistics to write.
        solution_file (str): The path to the solution file.
        statistic_file (str): The path to the statistic file.
        elapsed_time (int): The elapsed time in nanoseconds.
    """
    path, visited_states_len, processed_states_len, solution_length = statistics
    solution_length = len(path) if path != -1 else -1

    with open(solution_file, 'w') as sol_file:
        sol_file.write(f"{solution_length}\n")
        if path != -1:
            sol_file.write(' '.join(path) + '\n')

    with open(statistic_file, 'w') as stat_file:
        stat_file.write(f"{solution_length}\n")
        stat_file.write(f"{visited_states_len}\n")
        stat_file.write(f"{processed_states_len}\n")
        stat_file.write(f"{elapsed_time}\n")


if __name__ == "__main__":
    main()
