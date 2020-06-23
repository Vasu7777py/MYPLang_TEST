
from dataclasses import dataclass

# #######################################################################
# GLOBAL
# #######################################################################

RUN_FILE = None
FILE_LOCATION = ""

# #######################################################################
# CONSTANTS
# #######################################################################


# #######################################################################
# TOKENS
# #######################################################################

@dataclass
class Token:
    def __init__(self, _type_, value=None):
        self._type_ = _type_
        self.value = value

    def __repr__(self):
        return f"\"_type_ : {self._type_}, value : {self.value}\""

# #######################################################################
# POSITION
# #######################################################################

@dataclass
class Position:
    def __init__(self, index, column_number, line_number, file_name):
        self.index = index
        self.column_number = column_number
        self.line_number = line_number
        self.file_name = file_name
    
    def copy(self):
        return Position(self.index, self.column_number, self.line_number, self.file_name)

    def __repr__(self):
        return f"index : {self.index}, column_number : {self.column_number}, line_number : {self.line_number}, file_name : {self.file_name}"

    def advance(self, current_char):
        self.index += 1
        self.column_number += 1

        if (current_char == "\n"):
            self.column_number = 0
            self.line_number += 1

# #######################################################################
# LEXER
# #######################################################################

@dataclass
class Lexer:
    def __init__(self, file_name, file):
        self.file = file
        self.lines = self.file.readlines()
        if (len(self.lines) < 1):
            exit()
        self.file_name = file_name
        self.position = Position(0, 0, 0, file_name)
        self.tokens = None
        self.current_line = self.lines[self.position.line_number]
        self.current_char = self.current_line[0]
    
    def advance(self):
        self.position.advance(self.current_char)
        if (self.current_char == "\n"):
            if (self.position.line_number < len(self.lines)):
                self.current_line = self.lines[self.position.line_number]
            else:
                self.current_char = None
                return
        self.current_char = self.current_line[self.position.column_number]

    def create_tokens(self):
        pass

# #######################################################################
# KEYWORDS
# #######################################################################

KEYWORDS = {
    "int" : {},
    "float" : {},
    "char" : {},
    "str" : {},
    "list" : {},
    "dict" : {},
    "bool" : {},
    "void" : {},
    "func" : {},
    "return" : {},
    "_type_" : {},
    "NULL" : {},
}

# #######################################################################
# RUN
# #######################################################################

def run(file_name, file_location):
    RUN_FILE = open(f"{file_location}/{file_name}.txt", "r")
    print(RUN_FILE.read())
    RUN_FILE.close()
