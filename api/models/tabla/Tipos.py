from enum import Enum

class Tipos(Enum):
    INT = 1
    FLOAT = 2
    BOOLEAN = 3
    STR = 4
    STRING = 5
    CHAR = 6
    VOID = 7


def getTipo(s: str):
    
    if s == "i64":
        return Tipos.INT
    if s == "f64":
        return Tipos.FLOAT
    if s == "bool":
        return Tipos.BOOLEAN
    if s == "&str":
        return Tipos.STR
    if s == "String":
        return Tipos.STRING
    if s == "char":
        return Tipos.CHAR
    if s == "void":
        return Tipos.VOID


def definirTipo(value):
    if type(value) == float:
        return Tipos.FLOAT
    elif type(value) == int:
        return Tipos.INT
    elif type(value) == bool:
        return Tipos.BOOLEAN
    else:
        return None
    


class Tipo:
    def __init__(self, stipo = None, tipo = None):
        if stipo is not None:
            self.stipo = stipo
            self.tipo = getTipo(stipo)
        else:
            self.stipo = None
            self.tipo = tipo
        

    def getSTipo(self):
        return self.stipo