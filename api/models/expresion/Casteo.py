

from models.expresion.Expresion import Expresion
from models.tabla.Simbolo import Simbolo
from models.misc import driver
from models.expresion.Expresion import Expresion
from models.tabla.TablaSimbolos import TablaSimbolos
from models.expresion.Expresion import Expresion
from models.tabla.Tipos import definirTipo, Tipos, Tipo
from models.misc.error import Error_


class Casteo(Expresion):
    def __init__(self, nuevo_tipo: Tipo,  exp: Expresion, linea, columna):
        self.exp = exp;
        self.linea = linea
        self.columna = columna
        self.nuevo_tipo = nuevo_tipo
        
        
    def getTipo(self, ts):
        return self.nuevo_tipo.tipo
    
    def getValor(self, ts):
        tipo = self.exp.getTipo(ts)
        valor = self.exp.getValor(ts)
        
        if tipo == self.nuevo_tipo.tipo:
            return valor
        
        if tipo == Tipos.INT and self.nuevo_tipo.tipo == Tipos.CHAR:
            return chr(valor)
        elif tipo == Tipos.INT and self.nuevo_tipo.tipo == Tipos.FLOAT:
            return float(valor)
        elif tipo == Tipos.FLOAT and self.nuevo_tipo.tipo == Tipos.INT:
            return round(valor)
        else:
            raise Error_("Semantico", f'No se puede castear de {tipo} a {self.nuevo_tipo.tipo}',self.linea, self.columna)
        
        
        # if tipo == Tipos.STR:
        #     return self.exp.getValor(ts)
        # else:
        #     raise Error_("Semantico", "Solo se puede usar la funcion 'to_string' con expresiones tipo &str", self.linea, self.columna)