from models.expresion.Identificador import Identificador
from models.tabla.InstanciaVector import InstanciaVector
from models.tabla.InstanciaStruct import InstanciaStruct
from models.instruccion.Instruccion import Instruccion
from models.tabla.Funcion import Funcion
from models.tabla.Tipos import Tipos
from models.misc.error import Error_
from models.tabla.Simbolo import Simbolo
from models.expresion.Expresion import Expresion
from models.tabla.TablaSimbolos import TablaSimbolos

class Remove(Instruccion, Expresion):
    
    def __init__(self, id_instancia, indice,  linea, columna):
        self.id_instancia = id_instancia
        self.linea = linea
        self.columna = columna
        self.indice = indice
        
    
    def getTipo(self, ts):
        
        if isinstance(self.id_instancia, Identificador):
            instancia = self.id_instancia.getValor(ts)
            vector = instancia
        else:
            vector = ts.buscar(self.id_instancia)
        
        if vector is None:
            raise Error_("Semantico", f'No se ha encontrado el simbolo {self.id_instancia}', self.linea, self.columna)  
        
        if not isinstance(vector,InstanciaVector):
            raise Error_("Semantico", f'Simbolo {self.id_instancia} no es de tipo Vector', self.linea, self.columna) 
        
        return vector.tipo
            
    
    def getValor(self, ts):
        vector = self.id_instancia.getValor(ts)
        

        valor_indice = self.indice.getValor(ts)
        tipo_indice = self.indice.getTipo(ts)
        
        if vector is not None:
            
            if not isinstance(vector, InstanciaVector):
                raise Error_("Semantico", f'La instruccion \'Remove \' solo se puede ejecutar en vectores', self.linea, self.columna)  
            
            if (tipo_indice != Tipos.INT):
                raise Error_("Semantico", f'Tipo de push a vector incorrecto', self.linea, self.columna)  
        
            return vector.remove(valor_indice,  self.linea, self.columna)
        
        
        raise Error_("Semantico", f'NO se ha encontrado el simbolo {self.id_instancia}', self.linea, self.columna)  
        
             
    def ejecutar(self, ts: TablaSimbolos):

        vector = ts.buscar(self.id_instancia)
        
        if not isinstance(vector,InstanciaVector):
            raise Error_("Semantico", f'Simbolo {self.id_instancia} no es de tipo Vector', self.linea, self.columna) 

        valor_indice = self.indice.getValor(ts)
        tipo_indice = self.indice.getTipo(ts)
        
        if vector is not None:
            
            if (tipo_indice != Tipos.INT):
                raise Error_("Semantico", f'Tipo de push a vector incorrecto', self.linea, self.columna)  
            
            vector.remove(valor_indice,  self.linea, self.columna)
            return
        
        
        raise Error_("Semantico", f'NO se ha encontrado el simbolo {self.id_instancia}', self.linea, self.columna)  
        
        
        
        