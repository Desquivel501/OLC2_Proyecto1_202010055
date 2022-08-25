
from models.misc.error import Error_
from models.tabla.Simbolo import Simbolo
from models.misc import driver
from models.expresion.Expresion import Expresion
from models.tabla.TablaSimbolos import TablaSimbolos

class Identificador(Expresion):
    
    def __init__(self, identificador: str, linea: int, columna: int):
        self.identificador = identificador
        self.linea = linea
        self.columna = columna
        
    def getTipo(self, ts: TablaSimbolos):
        simbolo = ts.buscar(self.identificador)
        
        if simbolo is not None:
            print(simbolo.tipo)
            return simbolo.tipo.tipo
        else:
            raise Error_("Semantico", f'No se encontro el simbolo {self.identificador}', self.linea, self.columna)
             
        
    def getValor(self, ts: TablaSimbolos):
        simbolo = ts.buscar(self.identificador)
        
        if simbolo is not None:
            return simbolo.valor;
        else:
            raise Error_("Semantico", f'No se encontro el simbolo {self.identificador}', self.linea, self.columna)