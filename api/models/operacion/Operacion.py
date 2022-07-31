from enum import Enum
from mimetypes import init
from models.expresion.Expresion import Expresion


class Operador(Enum):
    SUMA = 1
    RESTA = 2
    MULTI = 3
    DIV = 4
    MODULO = 5
    POW = 6
    POWF = 7

def getOperador(op) -> Operador:
    if op == "+":
        return Operador.SUMA
    if op == "-":
        return Operador.RESTA
    if op == "*":
        return Operador.MULTI
    if op == "/":
        return Operador.DIV
    if op == "%":
        return Operador.MODULO
    if op == 'pow':
        return  Operador.POW
    if op == 'powf':
        return  Operador.POWF
        
    
class Operacion(Expresion):
    def __init__(self, left: Expresion, operador, right: Expresion, linea, columna, unaria):
        super().__init__()
        self.left = left
        self.right = right
        self.operador = getOperador(operador)
        self.unaria = unaria
        self.linea = linea
        self.columna = columna