from models.tabla.InstanciaVector import InstanciaVector
from models.tabla.InstanciaStruct import InstanciaStruct
from models.instruccion.Instruccion import Instruccion
from models.tabla.Funcion import Funcion
from models.tabla.Tipos import Tipos
from models.misc.error import Error_
from models.tabla.Simbolo import Simbolo
from models.expresion.Expresion import Expresion
from models.tabla.TablaSimbolos import TablaSimbolos

class Insert(Instruccion):
    
    def __init__(self, id_instancia, expresion, indice,  linea, columna):
        self.expresion = expresion
        self.id_instancia = id_instancia
        self.linea = linea
        self.columna = columna
        self.indice = indice
        
             
    def ejecutar(self, ts: TablaSimbolos):

        vector = self.id_instancia.getValor(ts)
        if not isinstance(vector, InstanciaVector):
            raise Error_("Semantico", f'La instruccion \'Insert \' solo se puede ejecutar en vectores', ts.env, self.linea, self.columna)  
        
        valor_valor = self.expresion.getValor(ts)
        tipo_valor = self.expresion.getTipo(ts)
        
        valor_indice = self.indice.getValor(ts)
        tipo_indice = self.indice.getTipo(ts)
        
        if vector is not None:
            
            if (vector.tipo != tipo_valor):
                raise Error_("Semantico", f'Tipo de insert a vector incorrecto', ts.env, self.linea, self.columna)  
            
            if (tipo_indice != Tipos.INT):
                raise Error_("Semantico", f'Indice debe de ser de tipo i64', ts.env, self.linea, self.columna)  
            
            vector.insert(valor_valor, valor_indice, self.linea, self.columna)
            return
        
        
        raise Error_("Semantico", f'No se ha encontrado el simbolo {self.id_instancia}', ts.env, self.linea, self.columna)  
        
        
        
        