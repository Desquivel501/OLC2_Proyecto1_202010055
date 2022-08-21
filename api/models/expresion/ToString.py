

from models.expresion.Expresion import Expresion
from models.tabla.Simbolo import Simbolo
from models.misc import driver
from models.expresion.Expresion import Expresion
from models.tabla.TablaSimbolos import TablaSimbolos
from models.expresion.Expresion import Expresion
from models.tabla.Tipos import definirTipo, Tipos
from models.misc.error import Error_


class ToString(Expresion):
    def __init__(self, exp: Expresion, linea, columna):
        self.exp = exp;
        self.linea = linea
        self.columna = columna
        
        
    def getTipo(self, ts):
        tipo = self.exp.getTipo(ts)
        if tipo == Tipos.STR:
            return Tipos.STRING
        else:
            raise Error_("Semantico", "Solo se puede usar la funcion 'to_string' con expresiones tipo &str", self.linea, self.columna)
    
    def getValor(self, ts):
        tipo = self.exp.getTipo(ts)
        
        if tipo == Tipos.STR:
            return self.exp.getValor(ts)
        else:
            raise Error_("Semantico", "Solo se puede usar la funcion 'to_string' con expresiones tipo &str", self.linea, self.columna)