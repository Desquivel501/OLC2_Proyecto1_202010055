
from models.expresion.Expresion import Expresion
from models.tabla.Tipos import Tipo

class Atributo():
    
    def __init__(self, identificador: str, valor: Expresion):
        self.identificador = identificador
        self.valor = valor
        self.tipo = None
