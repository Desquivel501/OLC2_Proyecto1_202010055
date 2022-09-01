
from models.tabla.InstanciaArreglo import InstanciaArreglo
from models.tabla.InstanciaStruct import InstanciaStruct
from models.instruccion.Instruccion import Instruccion
from models.tabla.Funcion import Funcion
from models.tabla.Tipos import Tipos
from models.misc.error import Error_
from models.tabla.Simbolo import Simbolo
from models.expresion.Expresion import Expresion
from models.tabla.TablaSimbolos import TablaSimbolos

class ModArreglo(Instruccion):
    
    def __init__(self, id_instancia, listaExpresiones, expresion ,linea, columna):
        self.listaExpresiones = listaExpresiones
        self.id_instancia = id_instancia
        self.linea = linea
        self.columna = columna
        self.tipo = None
        self.expresion = expresion
        
             
    def ejecutar(self, ts: TablaSimbolos):
                
        instancia = ts.buscar(self.id_instancia)

        nuevo_valor = self.expresion.getValor(ts)
        
        if isinstance(instancia, Simbolo):
            instancia = instancia.valor
        
        if isinstance(nuevo_valor, InstanciaArreglo):
            nuevo_valor = nuevo_valor.valores
        
        if instancia == None:
            raise Error_("Semantico", f'Arreglo {self.id_instancia} no existe', ts.env, self.linea, self.columna)
        
        if not isinstance(instancia, InstanciaArreglo):
            
            print(instancia)
            
            raise Error_("Semantico", f'Simbolo \'{self.identificador}\' no es de tipo Arreglo', ts.env, self.linea, self.columna)
        
        self.tipo = instancia.tipo
        
        dimensiones = self.obtenerDimensiones(ts)
        instancia.modValor(dimensiones, 0, instancia.valores, nuevo_valor, self.linea, self.columna)
        
        print(nuevo_valor)   

    
    def obtenerDimensiones(self, ts):
        listaDimensiones = []
        for dim in self.listaExpresiones:
            valor = dim.getValor(ts)
            tipo = dim.getTipo(ts)
            if tipo != Tipos.INT:
                raise Error_("Semantico", f'Dimension de un arreglo debe de ser tipo i64', ts.env, self.linea, self.columna)
            
            listaDimensiones.append(valor)
        
        return listaDimensiones
            
        