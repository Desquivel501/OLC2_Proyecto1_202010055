from ast import Expression

from models.misc.error import Error_
from models.tabla.InstanciaVector import InstanciaVector
from models.tabla.Tipos import Tipos
from models.tabla.Tipos import Tipo

class Capacidad(Expression):
    
    def __init__(self, expresion):
        self.expresion = expresion
        
    def getValor(self, ts):
        capacidad = self.expresion.getValor(ts)
        capacidad_tipo = self.expresion.getTipo(ts)
            
        if capacidad_tipo is not Tipos.INT:
            raise Error_("Semantico", f'Capacidad incorrecta', ts.env, self.linea, self.columna)
            
            
        instanciaVector = InstanciaVector(Tipos.STRUCT, [] , [])
        instanciaVector.identificador = None
        instanciaVector.mut = True
        instanciaVector.capacidad = capacidad
                
        return instanciaVector
    
    
    
    def getTipo(self, ts):
        return Tipos.VECTOR_DATA
