

import copy
from models.tabla.InstanciaStruct import InstanciaStruct
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
        
    def getTipo(self, ts: TablaSimbolos):
        
        if self.tipo == None:
            self.getValor(ts)
        return self.tipo
        
             
    def getValor(self, ts: TablaSimbolos):
        
        copiaLista = copy.deepcopy(self.listaExpresiones)
        
        expresionInicial = self.listaExpresiones.pop(0)
        expresionInicial = expresionInicial.getValor(ts)
         
        if isinstance(expresionInicial, InstanciaStruct):
            val = self.acceso(self.listaExpresiones, expresionInicial, ts)
            self.listaExpresiones = copiaLista
            return val
        
        else:
            raise Error_("Semantico", f'NOSE', self.linea, self.columna)
                    
        
    
    def acceso(self, listaExpresion, struct, ts):
        expresionInicial = self.listaExpresiones.pop(0)
        
        if len(listaExpresion) == 0:

            expresionInicial = expresionInicial.identificador
            valor = struct.dic_atributos.get(expresionInicial)
            
            if valor is not None:
                res = struct.dic_atributos[expresionInicial].valor
                self.tipo = struct.dic_atributos[expresionInicial].tipo
                return(res)
            else:
                raise Error_("Semantico", f'No se encontro el atributo {expresionInicial}', self.linea, self.columna)
            
        else:
            expresionInicial = expresionInicial.identificador
            nuevo_struct = struct.dic_atributos[expresionInicial].valor
            
            if nuevo_struct is not None:
               return self.acceso(self.listaExpresiones, nuevo_struct, ts)
            
            else:
                raise Error_("Semantico", f'No se encontro el simbolo {expresionInicial}', self.linea, self.columna)
            
        
        
        
        
        
        