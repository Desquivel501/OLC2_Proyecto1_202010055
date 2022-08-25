from models.expresion.Expresion import Expresion
from models.tabla.Tipos import Tipo
from enum import Enum

class Simbolos(Enum):
    VARIABLE = 1
    ARREGLO = 2
    FUNCION = 3

def getSimbolo(s):
    if(s == 1):
        return Simbolos.VARIABLE
    if(s == 2):
        return Simbolos.ARREGLO

class Simbolo:
    def __init__(self):
        self.valor = None
        self.id = None
        self.tipo = None
        self.simbolo = None
        self.mut = None
        
    
    def iniciarPrimitivo(self, id: str, tipo: Tipo, valor:Expresion, mut:bool):
        self.valor = valor
        self.id = id
        self.tipo = tipo
        self.simbolo = Simbolos.VARIABLE
        self.mut = mut
