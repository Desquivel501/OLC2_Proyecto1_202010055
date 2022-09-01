
from models.tabla.InstanciaVector import InstanciaVector
from models.tabla.InstanciaStruct import InstanciaStruct
from models.tabla.InstanciaArreglo import InstanciaArreglo
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
        
        if simbolo is not None:
            if isinstance(simbolo, InstanciaArreglo):
                return  simbolo.tipo
            
            if isinstance(simbolo, InstanciaStruct):
                return  Tipos.STRUCT
            
            if isinstance(simbolo, InstanciaVector):
                return  Tipos.VECTOR_DATA
            
            return simbolo.tipo.tipo;

        else:
            print("here")
            raise Error_("Semantico", f'No se encontro el simbolo {self.identificador}', ts.env, self.linea, self.columna)
             
        
    def getValor(self, ts: TablaSimbolos):
        simbolo = ts.buscar(self.identificador)
        
        if simbolo is not None:
            
            if isinstance(simbolo, InstanciaArreglo):
                return simbolo
            
            if isinstance(simbolo, InstanciaStruct):
                return  simbolo
            
            if isinstance(simbolo, InstanciaVector):
                return  simbolo
            
            return simbolo.valor;

        else:
            raise Error_("Semantico", f'No se encontro el simbolo {self.identificador}', ts.env, self.linea, self.columna)