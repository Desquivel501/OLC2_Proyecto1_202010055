from enum import Enum

class Tipos(Enum):
    INT = 1
    FLOAT = 2
    BOOLEAN = 3


def getTipo(s: str):
    if s == "INT":
        return Tipos.INT
    if s == "FLOAT":
        return Tipos.FLOAT
    if s == "BOOLEAN":
        return Tipos.BOOLEAN


def definirTipo(value):
    if type(value) == float:
        return Tipos.FLOAT
    elif type(value) == int:
        return Tipos.INT
    elif value == "true" or value == "false":
        return Tipos.BOOLEAN
    else:
        return None


class Tipo:
    def __init__(self, stipo: str):
        self.stipo = stipo
        self.tipo = getTipo(stipo)

    def getSTipo(self):
        return self.stipo