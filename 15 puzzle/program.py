from algorithms.a_star_strategy import astr
from algorithms.bfs_strategy import bfs
from validators.input_validator import Validator
from helpers.strategy_methods import BFS_DFS_Methods
from algorithms.dfs_strategy import dfs
from time import time_ns
from helpers.board_helper import BoardHelper

"""Main program function"""


def main():

    val = Validator()
    if not val.final_validator():
        return

    order = list(val.strategy) if val.option == 0 else BFS_DFS_Methods['data']

    solver = BoardHelper(order)

    # getting initial board
    with open(val.source) as input_board:
        solver.solved_board_generation(
            list(map(int, input_board.readline().split()))
        )
        for line in input_board:
            solver.starting_board.append(line.split())

    statistics = bfs(solver) \
        if val.method == 'bfs' \
        else dfs(solver) if val.method == 'dfs' \
        else astr(solver, val.strategy)

    initialization_time = time_ns()
    elapsed_time = time_ns() - initialization_time
    statistics = [statistics[0]] + [solver.visited_states_len, solver.processed_states_len] + [statistics[1]]
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


if __name__ == '__main__':
    main()
