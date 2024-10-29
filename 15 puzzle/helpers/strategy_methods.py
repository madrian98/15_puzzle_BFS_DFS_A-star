"""
Strategy methods for the 15-puzzle problem.
"""

# Possible methods for solving the 15-puzzle problem
POSSIBLE_METHODS = ['bfs', 'dfs', 'astr']

# Mapping of methods to their respective strategy types
METHOD_MAP = {
    'bfs': 0,
    'dfs': 0,
    'astr': 1
}

# Strategies for BFS and DFS methods
BFS_DFS_METHODS = {
    'data': ['L', 'R', 'U', 'D'],
    'value': lambda x: set(x) == set(BFS_DFS_METHODS['data'])
}

# Strategies for A* methods
A_STAR_METHODS = {
    'data': ['hamm', 'manh'],
    'value': lambda x: x in A_STAR_METHODS['data']
}

# Combined strategy methods
STRATEGY_METHODS = {
    0: BFS_DFS_METHODS,
    1: A_STAR_METHODS
}
