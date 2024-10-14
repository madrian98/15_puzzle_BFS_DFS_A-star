import sys
import re
from os.path import exists
from helpers import strategy_methods as sm

"""
Program validator.
"""

class Validator:
    """
    A class to validate the input arguments for the program.
    """

    def __init__(self):
        """
        Initialize the Validator with command-line arguments.
        """
        self.args = sys.argv[1:]

    def extraction_function(self) -> None:
        """
        Extract method, strategy, source, solution file, and stat file from arguments.
        """
        self.method = self.args[0]
        self.strategy = self.args[1]
        self.source = self.args[2]
        self.solution_file = self.args[3]
        self.stat_file = self.args[4]
        self.filenames = [self.source, self.solution_file, self.stat_file]

    def length_validator(self) -> bool:
        """
        Validate the length of the arguments.

        Returns:
            bool: True if the length of the arguments is 5, False otherwise.
        """
        return len(self.args) == 5

    def method_validator(self) -> bool:
        """
        Validate the method argument.

        Returns:
            bool: True if the method is in POSSIBLE_Methods, False otherwise.
        """
        return self.method in sm.POSSIBLE_Methods

    def strategy_validator(self) -> bool:
        """
        Validate the strategy argument.

        Returns:
            bool: True if the strategy is valid for the given method, False otherwise.
        """
        self.option = sm.METHOD_map[self.method]
        return sm.Strategy_Methods[self.option]['value'](self.strategy)

    def filename_validator(self) -> bool:
        """
        Validate the filenames.

        Returns:
            bool: True if the filenames are valid and the source file exists, False otherwise.
        """
        file_name_pattern = r'^[0-9]+[x][0-9]+_[0-9]+_[0-9]+[a-zA-Z_]*.txt'
        sample = re.compile(file_name_pattern, re.IGNORECASE)
        name_validator = all([re.fullmatch(sample, f) for f in self.filenames])
        source_exists = exists(self.source)

        if not name_validator:
            print('Incorrect file names:', self.filenames)

        if not source_exists:
            print('Input file does not exist')

        return name_validator and source_exists

    def final_validator(self) -> bool:
        """
        Perform all validations.

        Returns:
            bool: True if all validations pass, False otherwise.
        """
        if not self.length_validator():
            print('Check number of input arguments')
            return False

        if not self.method_validator():
            print('Invalid method:', self.method)
            return False

        if not self.strategy_validator():
            print('Invalid strategy:', self.strategy)
            return False

        if not self.filename_validator():
            return False

        return True
