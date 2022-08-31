from models.tabla.InstanciaVector import InstanciaVector
from models.tabla.InstanciaStruct import InstanciaStruct
from models.instruccion.Instruccion import Instruccion
from models.tabla.Funcion import Funcion
from models.tabla.Tipos import Tipos
from models.misc.error import Error_
from models.tabla.Simbolo import Simbolo
from models.expresion.Expresion import Expresion
from models.tabla.TablaSimbolos import TablaSimbolos

class Contains_(Expresion):
    
    def __init__(self, id_instancia, expresion,  linea, columna):
        self.id_instancia = id_instancia
        self.linea = linea
        self.columna = columna
        self.expresion = expresion
        
    
    def getTipo(self, ts):
        return Tipos.BOOLEAN
    
    def getValor(self, ts):
        

        valor = self.expresion.getValor(ts)
        tipo = self.expresion.getTipo(ts)
        
        vector = self.id_instancia.getValor(ts)
        if not isinstance(vector, InstanciaVector):
            raise Error_("Semantico", f'La instruccion \'Contains \' solo se puede ejecutar en vectores', self.linea, self.columna)  
        
        if vector is not None:
            
            if (vector.tipo != tipo):
                raise Error_("Semantico", f'Tipo de insert a vector incorrecto', self.linea, self.columna)  
        
            return vector.contains(valor,  self.linea, self.columna)
        
        
        raise Error_("Semantico", f'NO se ha encontrado el simbolo {self.id_instancia}', self.linea, self.columna)  
        
   