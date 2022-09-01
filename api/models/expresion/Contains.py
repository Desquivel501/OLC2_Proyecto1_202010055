

from models.tabla.InstanciaArreglo import InstanciaArreglo
from models.expresion.Expresion import Expresion
from models.expresion.Expresion import Expresion
from models.tabla.TablaSimbolos import TablaSimbolos
from models.expresion.Expresion import Expresion
from models.tabla.Tipos import Tipos
from models.misc.error import Error_


class Contains(Expresion):
    def __init__(self, id, expresion, linea, columna):
        self.id = id
        self.expresion = expresion;
        self.linea = linea
        self.columna = columna
        
        
    def getTipo(self, ts: TablaSimbolos):
        return Tipos.INT
    
    def getValor(self, ts: TablaSimbolos):
   
        valor = self.expresion.getValor(ts)
        lista = self.id.getValor(ts)

        if isinstance(lista,InstanciaArreglo):
            if valor in lista.valores:
                return True
            else:
                return False
        
        if isinstance(lista,list):
            if valor in lista:
                return True
            else:
                return False
            
             

        raise Error_("Semantico", "Solo se puede usar la funcion 'len' con Arreglos o Vectores",  ts.env, self.linea, self.columna)
