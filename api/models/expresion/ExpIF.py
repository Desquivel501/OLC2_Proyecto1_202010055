

from models.expresion.Expresion import Expresion
from models.tabla.Simbolo import Simbolo
from models.misc import driver
from models.expresion.Expresion import Expresion
from models.tabla.TablaSimbolos import TablaSimbolos
from models.expresion.Expresion import Expresion
from models.tabla.Tipos import definirTipo, Tipos
from models.misc.error import Error_


class ExpIf(Expresion):
    def __init__(self, condicion: Expresion, cuerpo: Expresion, else_ : Expresion, linea, columna):
        self.condicion = condicion
        self.cuerpo = cuerpo
        self.else_ = else_
        self.linea = linea
        self.columna = columna
        
        
    def getTipo(self, ts):
        return self.cuerpo.getTipo(ts)
    
    def getValor(self, ts):
        print("here")
        condicion = self.condicion.getValor(ts)
        tipo_condicion = self.condicion.getTipo(ts)
        
        if tipo_condicion is not Tipos.BOOLEAN:
            raise Error_("Semantica", "La condicion en in If debe ser de tipo BOOLEAN", self.linea, self.columna)
        
        
        print(self.cuerpo.getTipo(ts), " - ", self.else_.getTipo(ts))
        
        if self.cuerpo.getTipo(ts) != self.else_.getTipo(ts):
            raise Error_("Semantica", "Al usar un If como expresion, cada bloque debe de ser del mismo tipo", self.linea, self.columna)
        
        if condicion:
            return self.cuerpo.getValor(ts)
        elif self.else_ is not None:
            return self.else_.getValor(ts)