from models.expresion.Expresion import Expresion
from models.tabla.Tipos import definirTipo

class Primitivo(Expresion):
    def __init__(self, primitivo,linea: int, columna: int):
        super().__init__()
        self.primitivo = primitivo
        self.linea = linea
        self.columna = columna
        
    def getTipo(self, ts):
        return definirTipo(self.getValor(ts))
    
    def getValor(self, ts):
        return self.primitivo