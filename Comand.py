
from dataclasses import dataclass

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

print(KEYWORDS, "\n", KEYWORDS.keys())
