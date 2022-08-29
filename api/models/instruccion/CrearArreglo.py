
from models.tabla.InstanciaStruct import InstanciaStruct
from models.tabla.Struct import Struct
from models.misc.error import Error_
from models.instruccion.Instruccion import Instruccion
from models.tabla.Tipos import Tipo, Tipos
from models.tabla.TablaSimbolos import TablaSimbolos
from models.expresion.Expresion import Expresion


class CrearArreglo(Instruccion):
    def __init__(self, id_instancia:str, dimensiones, tipo, expresion, linea:int, columna: int ):
        self.id_instancia = id_instancia
        self.dimensiones = dimensiones
        self.tipo = tipo
        self.linea = linea
        self.columna = columna
         
        
    def ejecutar(self, ts: TablaSimbolos):
        
        expresionArreglo = self.expresion.getValor(ts)
        tipo = self.expresion.getTipo(ts)
        
        if tipo != Tipos.ARRAY_DATA:
            raise Error_("Semantico", f'Tipo incorrecto en arreglo', self.linea, self.columna)
        
        nueva_instancia = expresionArreglo.getValor(ts)
        
        if nueva_instancia.tipo != self.tipo:
            raise Error_("Semantico", f'Tipo incorrecto en arreglo', self.linea, self.columna)
        
        
        instancia = ts.obtenerArreglo(self.id_instancia)
        
        if instancia is not None:
            raise Error_("Semantico", f'Ya se ha declarado el arreglo', self.linea, self.columna)
        
        nueva_instancia.identificador = self.id_instancia
        
        print("ID: ", nueva_instancia.identificador, " - Tipo: ", nueva_instancia.tipo, " - Valores: ", nueva_instancia.valores)
        
        
        ts.agregarArreglo(self.id_instancia, nueva_instancia)

        
            

