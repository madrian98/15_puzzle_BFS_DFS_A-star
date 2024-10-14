from typing import List, Union
from node import Node

"""
Data structures for the 15-puzzle problem.
"""

class DataStructure:
    """
    Base class for data structures used in the 15-puzzle problem.
    """

    def __init__(self):
        """
        Initialize the data structure.
        """
        self.structure: List[Node] = []

    def __iter__(self):
        """
        Iterate over the elements in the data structure.
        """
        for element in self.structure:
            yield element

    def __repr__(self) -> str:
        """
        Return a string representation of the data structure.
        """
        return '\n'.join(str(element) for element in self.structure)

    def push(self, value: Node) -> None:
        """
        Push a value onto the data structure.

        Args:
            value (Node): The value to push.
        """
        self.structure.append(value)

    def __len__(self) -> int:
        """
        Return the number of elements in the data structure.

        Returns:
            int: The number of elements.
        """
        return len(self.structure)


class Stack(DataStructure):
    """
    Stack data structure for the 15-puzzle problem.
    """

    def __init__(self):
        """
        Initialize the stack.
        """
        super().__init__()

    def pop(self) -> Union[Node, None]:
        """
        Pop a value from the stack.

        Returns:
            Union[Node, None]: The popped value, or None if the stack is empty.
        """
        if len(self) > 0:
            return self.structure.pop()
        return None


class Queue(DataStructure):
    """
    Queue data structure for the 15-puzzle problem.
    """

    def __init__(self):
        """
        Initialize the queue.
        """
        super().__init__()

    def pop(self) -> Union[Node, None]:
        """
        Pop a value from the queue.

        Returns:
            Union[Node, None]: The popped value, or None if the queue is empty.
        """
        if len(self) > 0:
            return self.structure.pop(0)
        return None