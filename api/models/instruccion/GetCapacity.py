from models.tabla.InstanciaVector import InstanciaVector
from models.tabla.InstanciaStruct import InstanciaStruct
from models.instruccion.Instruccion import Instruccion
from models.tabla.Funcion import Funcion
from models.tabla.Tipos import Tipos
from models.misc.error import Error_
from models.tabla.Simbolo import Simbolo
from models.expresion.Expresion import Expresion
from models.tabla.TablaSimbolos import TablaSimbolos

class GetCapacity(Expresion):
    
    def __init__(self, id_instancia,  linea, columna):
        self.id_instancia = id_instancia
        self.linea = linea
        self.columna = columna
        
    def getTipo(self, ts):
        return Tipos.INT
    
    def getValor(self, ts):
        
        vector = self.id_instancia.getValor(ts)
        if not isinstance(vector, InstanciaVector):
            raise Error_("Semantico", f'La instruccion \'Capacity \' solo se puede ejecutar en vectores', ts.env, self.linea, self.columna)  
        
        if vector is not None:
            return vector.capacidad
        
        raise Error_("Semantico", f'NO se ha encontrado el simbolo {self.id_instancia}', ts.env, self.linea, self.columna)  
        
   