

from models.instruccion.Statement import Statement
from models.misc.error import Error_
from models.tabla.Tipos import Tipo, Tipos
from models.instruccion.Instruccion import Instruccion

class Funcion(Instruccion):
    
    def __init__(self, identificador: str, lista_param, instrucciones: Statement, tipo: Tipo, linea:int, columna: int ):
        self.identificador = identificador
        self.lista_param = lista_param
        self.tipo = tipo
        self.linea = linea
        self.columna = columna
        self.instrucciones = instrucciones
        
    def ejecutar(self, ts):
        funcion = ts.obtenerFuncion(self.identificador)
        
        if funcion is None:
            ts.agregarFuncion(self.identificador, self)
        else:
            raise Error_("Semantico", f'Funcion {self.identificador} ya ha sido declarada', self.linea, self.columna)
        
    