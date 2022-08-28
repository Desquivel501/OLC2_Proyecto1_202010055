

from models.instruccion.Instruccion import Instruccion
from models.tabla.Funcion import Funcion
from models.tabla.Tipos import Tipos
from models.misc.error import Error_
from models.tabla.Simbolo import Simbolo
from models.expresion.Expresion import Expresion
from models.tabla.TablaSimbolos import TablaSimbolos

class AccesoStruct(Expresion):
    
    def __init__(self, listaExpresiones, linea, columna):
        self.listaExpresiones = listaExpresiones
        self.tipo = None
        self.linea = linea
        self.columna = columna
        self.valor = None
        
    def getTipo(self, ts: TablaSimbolos):
        
        if self.tipo == None:
            self.getValor(ts)
        return self.tipo
        
             
    def getValor(self, ts: TablaSimbolos):
        
        if self.valor is not None:
            return self.valor
        
        expresionInicial = self.listaExpresiones.pop(0)
        
        struct = ts.obtenerInstancia(expresionInicial)
        
        if struct is None:
            print("here")
            raise Error_("Semantico", f'No se encontro el simbolo {expresionInicial}', self.linea, self.columna)
        
        return self.acceso(self.listaExpresiones, struct, ts)
                    
        
    
    def acceso(self, listaExpresion, struct, ts):
        print((listaExpresion))
        expresionInicial = self.listaExpresiones.pop(0)
        
        print(expresionInicial)
        
        if len(listaExpresion) == 0:
    
            valor = struct.dic_atributos.get(expresionInicial)
            
            if valor is not None:
                res = struct.dic_atributos[expresionInicial].valor
                self.tipo = struct.dic_atributos[expresionInicial].tipo
                print("res - ", res)
                self.valor = res
                return(res)
            else:
                raise Error_("Semantico", f'No se encontro el atributo {expresionInicial}', self.linea, self.columna)
            
        else:
            nuevo_struct = struct.dic_atributos[expresionInicial].valor
            
            if nuevo_struct is not None:
               return self.acceso(self.listaExpresiones, nuevo_struct, ts)
            
            else:
                raise Error_("Semantico", f'No se encontro el simbolo {expresionInicial}', self.linea, self.columna)
            
        
        
        
        
        
        