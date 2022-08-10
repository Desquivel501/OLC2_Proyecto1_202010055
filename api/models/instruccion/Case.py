from models.misc.Program import Program
from models.instruccion.Instruccion import Instruccion


class Case(Instruccion):

    def __init__(self, lista_exp, codigo: Instruccion, linea, columna):
        self.codigo = codigo
        self.linea = linea
        self.columna = columna
        self.lista_exp = lista_exp


    def ejecutar(self, ts):        
        pass
    
    