
import copy
from models.tabla.InstanciaVector import InstanciaVector
from models.tabla.InstanciaArreglo import InstanciaArreglo
from models.expresion.Expresion import Expresion
from models.expresion.Expresion import Expresion
from models.tabla.TablaSimbolos import TablaSimbolos
from models.expresion.Expresion import Expresion
from models.tabla.Tipos import Tipos
from models.misc.error import Error_


class Clone(Expresion):
    def __init__(self, expresion, linea, columna):
        self.expresion = copy.deepcopy(expresion);
        self.linea = linea
        self.columna = columna
        
        
    def getTipo(self, ts: TablaSimbolos):
        return self.expresion.getTipo(ts)
    
    def getValor(self, ts: TablaSimbolos):
        return self.expresion.getValor(ts)
        
