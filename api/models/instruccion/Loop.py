from xmlrpc.client import Boolean
from models.instruccion.Statement import Statement
from models.expresion.Expresion import Expresion
from models.tabla.TablaSimbolos import TablaSimbolos
from models.misc.Program import Program
from models.instruccion.Instruccion import Instruccion
from models.tabla.Tipos import Tipos
from models.misc.error import Error_


class Loop(Instruccion):

    def __init__(self, cuerpo: Statement, expresion: Boolean ,linea, columna):
        self.expresion = expresion
        self.cuerpo = cuerpo
        self.linea = linea
        self.columna = columna


    def ejecutar(self, ts):
        res = None
        ts_local = TablaSimbolos(ts, "loop")
        
        while True:
            
            res = self.cuerpo.ejecutar(ts_local)
                
            if res is not None:
                if res["tipo"] == "break":
                    if self.expresion:
                        return res["exp"]
                    break
                if res["tipo"] == "continue":
                    continue
                
            
        