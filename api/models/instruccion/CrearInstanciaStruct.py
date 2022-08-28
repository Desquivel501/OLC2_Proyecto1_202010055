

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
        
        nueva_instancia: InstanciaStruct = ts.obtenerInstancia(self.id_instancia)
        
        if nueva_instancia is None:

            nueva_instancia = self.instancia.getValor(ts)
            nueva_instancia.id_instancia = self.id_instancia
            nueva_instancia.mut = self.mut
            
            ts.agregarIntancia(self.id_instancia, nueva_instancia)
            
            print("Struct : ", nueva_instancia.id_struct)
            print("ID : ", self.id_instancia)
        
            
            for x in self.instancia.dic_atributos:
                print(x, " : ",self.instancia.dic_atributos[x].valor )
                
            print("")
            
        else:
            raise Error_("Semantico", f'Instancia {self.id_instancia} ya ha sido declarado', self.linea, self.columna)

        
            

