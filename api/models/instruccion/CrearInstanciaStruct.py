

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
        # struct = ts.obtenerStruct(self.)
        
        # nueva_instancia: InstanciaStruct = ts.buscar(self.id_instancia)
        
        # if nueva_instancia is None:
            
            # print("nueva")
            
            # nueva_instancia = self.instancia.getValor(ts)
            # nueva_instancia.id_instancia = self.id_instancia
            # nueva_instancia.mut = self.mut
            
            # ts.add(self.id_instancia, nueva_instancia)
            
            # print("Struct : ", nueva_instancia.id_struct)
            # print("ID : ", self.id_instancia)
            # print("Instancia : ", nueva_instancia)
            
            # for x in self.instancia.dic_atributos:
            #     print(x, " : ",self.instancia.dic_atributos[x].valor )
                
        #     print("")
            
        # else:
            # if not isinstance(nueva_instancia, InstanciaStruct):
            #     raise Error_("Semantico", f'Simbolo \'{self.identificador}\' no es de tipo struct', self.linea, self.columna)
            
            # print("no nueva")
            
            # nueva_instancia = self.instancia.getValor(ts)
            # nueva_instancia.id_instancia = self.id_instancia
            # nueva_instancia.mut = self.mut
            
            # ts.add(self.id_instancia, nueva_instancia)

        
            

