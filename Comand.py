
from dataclasses import dataclass

# #########################################################################
# CONSTANTS
# #########################################################################

DIGITS = ".0123456789"

# #########################################################################
# ERORRS
# #########################################################################

@dataclass
class Error:
    def __init__(self, pos_start, pos_end, error_name, error_description):
        self.pos_start = pos_start
        self.pos_end = pos_end
        self.error_name = error_name
        self.error_description = error_description

    def as_string(self):
        result = f"{self.error_name} : {self.error_description}"
        result += f"File {self.pos_start.file_name}, line {self.pos_start.line_number}"
        return result
    
@dataclass
class IllegalchaError(Error):
    def __init__(self, pos_start, pos_end, description):
        super().__init__(pos_start, pos_end, "Illegal charater", description)

# #########################################################################
# POSITION
# #########################################################################

@dataclass
class Position:
    def __init__(self, index, line_number, column_number, file_name, file_text):
        self.index = index
        self.line_number = line_number
        self.column_number = column_number
        self.file_name = file_name
        self.file_text = file_text

    def advance(self, current_char):
        self.index += 1
        self.column_number += 1

        if current_char == "\n":
            self.line_number += 1
            self.column_number = 0

        return self
    
    def copy(self):
        return Position(self.index, self.line_number, self.column_number, self.file_name, self.file_text)

# #########################################################################
# TOKENS
# #########################################################################

TT_INT = "INT"
TT_FLOAT = "FLOAT"
TT_PLUS = "PLUS"
TT_MINUS = "MINUS"
TT_MUL = "MUL"
TT_DIV = "DIV"
TT_LPAREN = "LPAREN"
TT_RPAREN = "RPAREN"

@dataclass
class Token:
    def __init__(self, type_, value=None):
        self.type = type_
        self.value = value

    def __repr__(self):
        if self.value:
            return f"{self.type} : {self.value}"
        else:
            return f"{self.type}"
    
# #########################################################################
# LEXER
# #########################################################################

@dataclass
class Lexer:
    def __init__(self, filename, text):
        self.filename = filename
        self.text = text
        self.position = Position(-1, 0, -1, filename, text)
        self.current_char = None
        self.advance()

    def advance(self):
        self.position.advance(self.current_char)
        self.current_char = self.text[self.position.index] if self.position.index < len(self.text) else None

    def make_tokens(self):
        tokens = []

        while self.current_char != None:
            if self.current_char in " \t":
                self.advance()
            elif self.current_char in DIGITS:
                tokens.append(self.make_number())
            elif self.current_char == "+":
                tokens.append(Token(TT_PLUS))
                self.advance()
            elif self.current_char == "-":
                tokens.append(Token(TT_MINUS))
                self.advance()
            elif self.current_char == "*":
                tokens.append(Token(TT_MUL))
                self.advance()
            elif self.current_char == "/":
                tokens.append(Token(TT_DIV))
                self.advance()
            elif self.current_char == "(":
                tokens.append(Token(TT_LPAREN))
                self.advance()
            elif self.current_char == ")":
                tokens.append(Token(TT_RPAREN))
                self.advance()
            else:
                pos_start = self.position.copy()
                char = self.current_char
                self.advance()
                return [], IllegalchaError(pos_start, self.position, "'" + char + "'")

        return tokens, None

    def make_number(self):
        num_str = ""
        dot_count = 0

        while ((self.current_char != None) and (self.current_char in DIGITS)):
            if self.current_char == ".":
                if dot_count == 1: break
                dot_count += 1
                num_str += "."
            else:
                num_str += self.current_char
            self.advance()

        if dot_count == 0:
            return Token(TT_INT, int(num_str))
        else:
            return Token(TT_FLOAT, float(num_str))

# #########################################################################
# RUN
# #########################################################################

def run(fn, text):
    lexer = Lexer(fn, text)
    tokens, error = lexer.make_tokens()

    return tokens, error
