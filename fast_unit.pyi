class Unum:
    def __init__(self, val: float): ...
    def __str__(self) -> str: ...
    def __mul__(self, other: Unum) -> Unum: ...
    def __div__(self, other: Unum) -> Unum: ...
    def __truediv__(self, other: Unum) -> Unum: ...

def add_unit(name: str, long_name: str) -> Unum: ...