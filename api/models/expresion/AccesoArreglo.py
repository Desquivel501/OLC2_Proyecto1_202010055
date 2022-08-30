

from models.tabla.InstanciaStruct import InstanciaStruct
from models.instruccion.Instruccion import Instruccion
from models.tabla.Funcion import Funcion
from models.tabla.Tipos import Tipos
from models.misc.error import Error_
from models.tabla.Simbolo import Simbolo
from models.expresion.Expresion import Expresion
from models.tabla.TablaSimbolos import TablaSimbolos

class AccesoArreglo(Expresion):
    
    def __init__(self, id_instancia, listaExpresiones, linea, columna):
        self.listaExpresiones = listaExpresiones
        self.id_instancia = id_instancia
        self.linea = linea
        self.columna = columna
        self.tipo = None
        
    def getTipo(self, ts: TablaSimbolos):
        
        if self.tipo == None:
            self.getValor(ts)
        return self.tipo
        
             
    def getValor(self, ts: TablaSimbolos):
                
        instancia = ts.obtenerArreglo(self.id_instancia)
        
        if instancia == None:
            raise Error_("Semantico", f'Arreglo {self.id_instancia} no existe', self.linea, self.columna)
        
        self.tipo = instancia.tipo
        
        dimensiones = self.obtenerDimensiones(ts)
        valor = instancia.getValor(dimensiones, 0, instancia.valores, self.linea, self.columna)
        
        print(valor)   

        return valor       
        
    
    def obtenerDimensiones(self, ts):
        listaDimensiones = []
        for dim in self.listaExpresiones:
            valor = dim.getValor(ts)
            tipo = dim.getTipo(ts)
            if tipo != Tipos.INT:
                raise Error_("Semantico", f'Dimension de un arreglo debe de ser tipo i64', self.linea, self.columna)
            
            listaDimensiones.append(valor)
        
        return listaDimensiones
            
        
        
        
        