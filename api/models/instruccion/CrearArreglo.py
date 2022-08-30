
from models.tabla.InstanciaStruct import InstanciaStruct
from models.tabla.Struct import Struct
from models.misc.error import Error_
from models.instruccion.Instruccion import Instruccion
from models.tabla.Tipos import Tipo, Tipos
from models.tabla.TablaSimbolos import TablaSimbolos
from models.expresion.Expresion import Expresion


class CrearArreglo(Instruccion):
    def __init__(self, id_instancia:str, dimensiones, tipo, expresion, mut, linea:int, columna: int ):
        self.id_instancia = id_instancia
        self.dimensiones = dimensiones
        self.tipo = tipo
        self.linea = linea
        self.columna = columna
        self.expresion = expresion
        self.mut = mut
         
        
    def ejecutar(self, ts: TablaSimbolos):
                
        expresionArreglo = self.expresion.getValor(ts)
        self.dimensiones = self.obtenerDimendiones(ts)
        self.dimensiones.reverse()
        
        
        tipo = self.expresion.getTipo(ts)
        
        if tipo != Tipos.ARRAY_DATA:
            raise Error_("Semantico", f'Tipo incorrecto en arreglo', self.linea, self.columna)
        
        nueva_instancia = expresionArreglo
        
        if self.tipo.tipo != nueva_instancia.tipo:
            raise Error_("Semantico", f'Tipos en arreglo no coinciden', self.linea, self.columna)
        
                
        print("-------------LISTA---------------------------------")        
        print(nueva_instancia.valores)
        print("---------------------------------------------------") 
        
        print("-------------DIMENSION-----------------------------")        
        print(nueva_instancia.dimensiones)
        print("---------------------------------------------------") 
        
        print("-------------VALIDO--------------------------------")        
        print(self.validarDimension(nueva_instancia.dimensiones, self.dimensiones))
        print("---------------------------------------------------") 
        

        instancia = ts.obtenerArreglo(self.id_instancia)
        
        if instancia is not None:
            raise Error_("Semantico", f'Ya se ha declarado el arreglo', self.linea, self.columna)
        
        nueva_instancia.identificador = self.id_instancia
        nueva_instancia.mut = self.mut
        
        print("ID: ", nueva_instancia.identificador, " - Tipo: ", nueva_instancia.tipo, " - Valores: ", nueva_instancia.valores)
                
        ts.agregarArreglo(self.id_instancia, nueva_instancia)
        
        
    def obtenerDimendiones(self, ts):
        listaDimensiones = []
        for dim in self.dimensiones:
            valor = dim.getValor(ts)
            tipo = dim.getTipo(ts)
            if tipo != Tipos.INT:
                raise Error_("Semantico", f'Dimension de un arreglo debe de ser tipo i64', self.linea, self.columna)
            
            listaDimensiones.append(valor)
        
        return listaDimensiones

    
    def validarDimension(self, dimensiones, nuevas_dimensiones):
        
        if len(dimensiones) != len(nuevas_dimensiones):
            raise Error_("Semantico", f'Dimensiones del arreglo {self.id_instancia} no coinciden', self.linea, self.columna)
        
        for i in range(0, len(dimensiones)):
            if dimensiones[i] != nuevas_dimensiones[i]:
                raise Error_("Semantico", f'Dimensiones del arreglo {self.id_instancia} no coinciden', self.linea, self.columna)
        
        return True
    
    # def compararDimensiones(self, ts, dimensiones_compiladas):
        
        
    
            

