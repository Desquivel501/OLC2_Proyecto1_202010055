from models.instruccion.Statement import Statement
from models.expresion.Expresion import Expresion
from models.tabla.TablaSimbolos import TablaSimbolos
from models.misc.Program import Program
from models.instruccion.Instruccion import Instruccion
from models.tabla.Tipos import Tipos
from models.misc.error import Error_


class While(Instruccion):

    def __init__(self, condicion: Expresion, cuerpo: Statement, linea, columna):
        self.condicion = condicion
        self.cuerpo = cuerpo
        self.linea = linea
        self.columna = columna


    def ejecutar(self, ts):
        res = None
        ts_local = TablaSimbolos(ts, "while")
        
        condicion = self.condicion.getValor(ts)
        tipo_condicion = self.condicion.getTipo(ts)
        
        if tipo_condicion is not Tipos.BOOLEAN:
            raise Error_("Semantico", "La condicion en un While debe ser de tipo BOOLEAN", ts.env, self.linea, self.columna)
        
        i = 0
        while condicion:
            
            res = self.cuerpo.ejecutar(ts_local)
                
            if res is not None:
                if res["tipo"] == "break":
                    break
                if res["tipo"] == "continue":
                    continue
            
            
            
            condicion = self.condicion.getValor(ts)
        
