from models.instruccion.Instruccion import Instruccion
from models.expresion.Expresion import Expresion
from models.misc.Program import Program


class Ejecutar(Instruccion):

    def __init__(self, exp: Expresion, linea, columna):
        self.columna = columna
        self.linea = linea
        self.exp = exp

    def ejecutar(self, ts):
        Program.console += str(self.exp.getValor(ts)) + "\n"