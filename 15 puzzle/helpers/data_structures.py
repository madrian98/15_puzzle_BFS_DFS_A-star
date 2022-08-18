from typing import List, Union
from node import Node

"""Data structure function init"""


class DataStructure:

    def __init__(self):
        self.structure:List[Node] = []

    def __iter__(self):
        for itr in self.structure:
            yield itr

    def __repr__(self) -> str:
        return '\n'.join(str(itr) for itr in self.structure)

    def push(self, value):
        self.structure.append(value)

    def __len__(self) -> int:
        return len(self.structure)


class Stack(DataStructure):
    def __init__(self):
        super(Stack, self).__init__()

    def pop(self) -> Union[Node, None]:
        if self.__len__() > 0:
            return self.structure.pop()
        return None


class Queue(DataStructure):
    def __init__(self):
        super(Queue, self).__init__()

    def pop(self) -> Union[Node, None]:
        if self.__len__() > 0:
            return self.structure.pop(0)
        return None


