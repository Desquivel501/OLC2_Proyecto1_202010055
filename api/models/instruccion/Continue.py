from models.misc.Program import Program
from models.instruccion.Instruccion import Instruccion

class Continue(Instruccion):

    def __init__(self, linea, columna):
        self.linea = linea
        self.columna = columna


    def ejecutar(self, ts):        
         return {"tipo":"continue", "exp":None};
    