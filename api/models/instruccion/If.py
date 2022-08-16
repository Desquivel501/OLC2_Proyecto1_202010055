
from models.instruccion.Statement import Statement
from models.expresion.Expresion import Expresion
from models.tabla.TablaSimbolos import TablaSimbolos
from models.misc.Program import Program
from models.instruccion.Instruccion import Instruccion
from models.tabla.Tipos import Tipos
from models.misc.error import Error_


class If(Instruccion):

    def __init__(self, condicion: Expresion, cuerpo: Statement, else_ : Statement, linea, columna):
        self.condicion = condicion
        self.cuerpo = cuerpo
        self.else_ = else_
        self.linea = linea
        self.columna = columna


    def ejecutar(self, ts):
        
        ts_local = TablaSimbolos(ts, "IF")
        condicion = self.condicion.getValor(ts)
        tipo_condicion = self.condicion.getTipo(ts)
        
        if tipo_condicion is not Tipos.BOOLEAN:
            raise Error_("Semantico", "La condicion en in If debe ser de tipo BOOLEAN", self.linea, self.columna)
        
        if condicion:
            return self.cuerpo.ejecutar(ts_local)
        elif self.else_ is not None:
            return self.else_.ejecutar(ts_local)