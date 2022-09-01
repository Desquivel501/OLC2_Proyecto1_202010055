

from models.tabla.InstanciaStruct import InstanciaStruct
from models.tabla.Struct import Struct
from models.misc.error import Error_
from models.instruccion.Instruccion import Instruccion
from models.tabla.Tipos import Tipo, Tipos
from models.tabla.TablaSimbolos import TablaSimbolos
from models.expresion.Expresion import Expresion


class CrearInstanciaStruct(Instruccion):
    def __init__(self, id_instancia:str, instancia, mut:bool, linea:int, columna: int ):
        self.id_instancia = id_instancia
        self.instancia = instancia
        self.mut = mut
        self.linea = linea
        self.columna = columna
        
         
        
    def ejecutar(self, ts: TablaSimbolos):
        pass
