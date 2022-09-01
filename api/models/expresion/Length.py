
from models.tabla.InstanciaVector import InstanciaVector
from models.tabla.InstanciaArreglo import InstanciaArreglo
from models.expresion.Expresion import Expresion
from models.expresion.Expresion import Expresion
from models.tabla.TablaSimbolos import TablaSimbolos
from models.expresion.Expresion import Expresion
from models.tabla.Tipos import Tipos
from models.misc.error import Error_


class Length(Expresion):
    def __init__(self, expresion, linea, columna):
        self.expresion = expresion;
        self.linea = linea
        self.columna = columna
        
        
    def getTipo(self, ts: TablaSimbolos):
        return Tipos.INT
    
    def getValor(self, ts: TablaSimbolos):
   
  
        valor = self.expresion.getValor(ts)      

        if isinstance(valor,InstanciaArreglo):
            return len(valor.valores)
        
        if isinstance(valor,InstanciaVector):
            return len(valor.valores)
        
        if isinstance(valor,list):
            return len(valor)
        
        print(valor)

        raise Error_("Semantico", "Solo se puede usar la funcion 'len' con Arreglos o Vectores", ts.env, self.linea, self.columna)
