
from models.misc.error import Error_
from models.tabla.Simbolo import Simbolo
from models.misc import driver
from models.expresion.Expresion import Expresion
from models.tabla.TablaSimbolos import TablaSimbolos
from models.tabla.Tipos import Tipo, Tipos

class Identificador(Expresion):
    
    def __init__(self, identificador: str, linea: int, columna: int):
        self.identificador = identificador
        self.linea = linea
        self.columna = columna
        
    def getTipo(self, ts: TablaSimbolos):
        simbolo = ts.buscar(self.identificador)
        struct = ts.obtenerInstancia(self.identificador)
        array = ts.obtenerArreglo(self.identificador)
        
        if simbolo is not None:
            return simbolo.tipo.tipo
        elif struct is not None:
            return Tipos.STRUCT
        elif array is not None:
            return Tipos.ARRAY
        else:
            raise Error_("Semantico", f'No se encontro el simbolo {self.identificador}', self.linea, self.columna)
             
        
    def getValor(self, ts: TablaSimbolos):
        simbolo = ts.buscar(self.identificador)
        struct = ts.obtenerInstancia(self.identificador)
        array = ts.obtenerArreglo(self.identificador)
        
        if simbolo is not None:
            return simbolo.valor;
        elif struct is not None:
            return struct
        elif array is not None:
            return array
        else:
            raise Error_("Semantico", f'No se encontro el simbolo {self.identificador}', self.linea, self.columna)