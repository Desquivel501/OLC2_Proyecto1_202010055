from models.tabla.Struct import Struct
from models.expresion.Expresion import Expresion
from models.tabla.Tipos import Tipo

class Rango():
    
    def __init__(self, inicio: Expresion, fin: Expresion):
        self.inicio = inicio
        self.fin = fin
        
