from models.expresion.Expresion import Expresion
from models.tabla.Tipos import definirTipo

class Primitivo(Expresion):
    def __init__(self, primitivo,tipo, linea: int, columna: int):
        super().__init__()
        self.primitivo = primitivo
        self.linea = linea
        self.columna = columna
        self.tipo = tipo
        
    def getTipo(self, ts):
        if self.tipo is None:
            self.tipo = definirTipo(self.getValor(ts))
        return self.tipo
    
    def getValor(self, ts):
        return self.primitivo