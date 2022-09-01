

from models.tabla.InstanciaVector import InstanciaVector
from models.tabla.InstanciaStruct import InstanciaStruct
from models.instruccion.Instruccion import Instruccion
from models.tabla.Funcion import Funcion
from models.tabla.Tipos import Tipos
from models.misc.error import Error_
from models.tabla.Simbolo import Simbolo
from models.expresion.Expresion import Expresion
from models.tabla.TablaSimbolos import TablaSimbolos

class Push(Instruccion):
    
    def __init__(self, id_instancia, expresion, linea, columna):
        self.expresion = expresion
        self.id_instancia = id_instancia
        self.linea = linea
        self.columna = columna
        self.tipo = None
        
             
    def ejecutar(self, ts: TablaSimbolos):

        vector = self.id_instancia.getValor(ts)
        if not isinstance(vector, InstanciaVector):
            raise Error_("Semantico", f'La instruccion \'Push \' solo se puede ejecutar en vectores', ts.env, self.linea, self.columna) 
        
        valor = self.expresion.getValor(ts)
        tipo = self.expresion.getTipo(ts)
        
        if vector is not None:
            
            print(vector.tipo, " - ", tipo)
            
            if(tipo == Tipos.VECTOR_DATA):
                valor = valor.valores
            
            print(vector.tipo, " - ", tipo)
            
           
            
            if (vector.tipo != tipo):
                raise Error_("Semantico", f'Tipo de push a vector incorrecto', ts.env, self.linea, self.columna)  
            
            vector.push(valor, self.linea, self.columna)
            return
        
        
        raise Error_("Semantico", f'NO se ha encontrado el simbolo {self.id_instancia}', ts.env, self.linea, self.columna)  
        
        
        
        
        