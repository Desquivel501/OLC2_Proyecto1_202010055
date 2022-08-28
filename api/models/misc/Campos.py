from models.tabla.Struct import Struct
from models.expresion.Expresion import Expresion
from models.tabla.Tipos import Tipo

class Campos():
    
    def __init__(self, identificador: str, tipo):
        self.identificador = identificador
        self.tipo = tipo
        
