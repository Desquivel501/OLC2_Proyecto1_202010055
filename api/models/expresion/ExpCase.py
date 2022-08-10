
from models.misc.Program import Program

from models.expresion.Expresion import Expresion


class ExpCase(Expresion):

    def __init__(self, lista_exp, codigo: Expresion, linea, columna):
        self.codigo = codigo
        self.linea = linea
        self.columna = columna
        self.lista_exp = lista_exp


    def getTipo(self, ts):
        return self.codigo.getTipo(ts)
    
    def getValor(self, ts):
        return self.codigo.getValor(ts)