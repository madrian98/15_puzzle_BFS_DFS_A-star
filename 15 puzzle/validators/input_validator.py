import sys
import re
from os.path import exists
from helpers import strategy_methods as sm

"""Program validator"""


class Validator:


    def __init__(self):
        self.args = sys.argv[1:]

    def extraction_function(self) -> None:

        self.method = self.args[0]

        self.strategy = self.args[1]

        self.source = self.args[2]

        self.solution_file = self.args[3]

        self.stat_file = self.args[4]

        self.filenames = [self.source, self.solution_file, self.stat_file]

    def lenght_validator(self) -> bool:
        return len(self.args) == 5   # length of the argument

    def method_validator(self) -> bool:
        return self.method in sm.POSSIBLE_Methods

    def strategy_validator(self) -> bool:
        self.option = sm.METHOD_map[self.method]
        return sm.Strategy_Methods[self.option]['value'](self.strategy)

    def fileName_validator(self) -> bool:
        file_name = r'^[0-9]+[x][0-9]+_[0-9]+_[0-9]+[a-zA-Z_]*.txt'
        sample = re.compile(file_name, re.IGNORECASE)
        name_validator = all([re.fullmatch(sample, f) for f in self.filenames])
        exist = exists(self.source)

        if not name_validator:
            print('Incorrect files names', self.filenames)

        if not exist:
            print('Input file does not exist')

        return name_validator and exist

    def final_validator(self) -> bool:
        if not self.lenght_validator():
            print('Check number of input arguments')
            return False
        self.extraction_function()

        if not self.method_validator():
            print('Check name of input method')
            return False

        if not self.strategy_validator():
            print('Check name of input strategy')
            return False

        if self.fileName_validator():
            return True
        return False

