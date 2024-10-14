
"""Strategy checker"""

POSSIBLE_Methods = ['bfs', 'dfs', 'astr']

METHOD_map = {
    'bfs': 0,
    'dfs': 0,
    'astr': 1
}

BFS_DFS_Methods = {
    'data': ['L', 'R', 'U', 'D'],
    'value': lambda x: set(x) == set(BFS_DFS_Methods['data'])
}

A_STAR_Methods = {
    'data': ['hamm', 'manh'],
    'value': lambda x: x in A_STAR_Methods['data']
}

Strategy_Methods = {
    0: BFS_DFS_Methods,
    1: A_STAR_Methods
}

