from models.misc.Program import Program
from models.instruccion.Instruccion import Instruccion


class Statement(Instruccion):

    def __init__(self, codigo, linea, columna):
        self.codigo = codigo
        self.linea = linea
        self.columna = columna


    def ejecutar(self, ts):        
        for ins in self.codigo:
            try:
                ins.ejecutar(ts)
            except Exception as e:
                print(e)