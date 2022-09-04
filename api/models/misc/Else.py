
from models.expresion.Expresion import Expresion


class Else():
    
    def __init__(self, instruccion, expresion ):
        self.instruccion = instruccion
        self.expresion = expresion
        
        
    def getTipo(self, ts):
        return self.expresion.getTipo(ts) 
        
    def getValor(self, ts):
        return self.expresion.getValor(ts)