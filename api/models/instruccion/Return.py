from models.misc.Program import Program
from models.instruccion.Instruccion import Instruccion
from models.expresion.Expresion import Expresion

class Return(Instruccion):

    def __init__(self, expresion: Expresion, linea, columna):
        self.linea = linea
        self.columna = columna
        self.expresion = expresion


    def ejecutar(self, ts):        
        return {"tipo":"return", "exp":self.expresion};
    
    