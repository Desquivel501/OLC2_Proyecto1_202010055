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
    MAYOR = 8
    MENOR = 9
    MAYOR_I = 10
    MENOR_I = 11
    IGUAL = 12
    NO_IGUAL = 13
    OR = 14
    AND = 15
    NOT = 16
    ABS = 17
    SQRT = 18


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
    if op == '>':
        return Operador.MAYOR
    if op == '<':
        return Operador.MENOR
    if op == '>=':
        return Operador.MAYOR_I
    if op == '<=':
        return Operador.MENOR_I
    if op == '==':
        return Operador.IGUAL
    if op == '!=':
        return Operador.NO_IGUAL
    if op == "||":
        return Operador.OR
    if op == "&&":
        return Operador.AND
    if op == "!":
        return Operador.NOT
    if op == "abs":
        return Operador.ABS
    if op == "sqrt":
        return Operador.SQRT
                
    
class Operacion(Expresion):
    def __init__(self, left: Expresion, operador, right: Expresion, linea, columna, unaria):
        super().__init__()
        self.left = left
        self.right = right
        self.operador = getOperador(operador)
        self.unaria = unaria
        self.linea = linea
        self.columna = columna