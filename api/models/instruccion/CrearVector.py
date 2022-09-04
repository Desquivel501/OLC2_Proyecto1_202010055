from models.tabla.InstanciaVector import InstanciaVector
from models.misc.error import Error_
from models.instruccion.Instruccion import Instruccion
from models.tabla.Tipos import Tipo, Tipos
from models.tabla.TablaSimbolos import TablaSimbolos
from models.expresion.Expresion import Expresion


class CrearVector(Instruccion):
    def __init__(self, id_instancia:str, capacidad, tipo, expresion, mut, linea:int, columna: int ):
        self.id_instancia = id_instancia
        self.capacidad = capacidad
        self.tipo = tipo
        self.linea = linea
        self.columna = columna
        self.expresion = expresion
        self.mut = mut
    
    
    def ejecutar(self, ts: TablaSimbolos):
        
        if self.capacidad is not None:
            capacidad = self.capacidad.getValor(ts)
            capacidad_tipo = self.capacidad.getTipo(ts)
            
            if capacidad_tipo is not Tipos.INT:
                raise Error_("Semantico", f'Capacidad incorrecta', ts.env, self.linea, self.columna)
            
            
            instanciaVector = InstanciaVector(self.tipo.tipo, [] , [])
            instanciaVector.identificador = self.id_instancia
            instanciaVector.mut = self.mut
            instanciaVector.capacidad = capacidad
            
            ts.add(self.id_instancia, instanciaVector, self.linea, self.columna)
            return
        

        tipo = self.expresion.getTipo(ts)     
        expresionArreglo = self.expresion.getValor(ts)
        
        if tipo != Tipos.VECTOR_DATA:
            raise Error_("Semantico", f'Tipo incorrecto en arreglo', ts.env, self.linea, self.columna)
        
        nueva_instancia = expresionArreglo

        if self.tipo is not None:        
            if self.tipo.tipo != nueva_instancia.tipo:
                raise Error_("Semantico", f'Tipos en arreglo no coinciden', ts.env, self.linea, self.columna)
            
        nueva_instancia.identificador = self.id_instancia
        nueva_instancia.mut = self.mut
        nueva_instancia.capacidad = len(nueva_instancia.valores)
            
        ts.add(self.id_instancia, nueva_instancia, self.linea, self.columna)
        
        
    # def obtenerDimendiones(self, ts):
    #     listaDimensiones = []
    #     for dim in self.dimensiones:
    #         valor = dim.getValor(ts)
    #         tipo = dim.getTipo(ts)
    #         if tipo != Tipos.INT:
    #             raise Error_("Semantico", f'Dimension de un arreglo debe de ser tipo i64', ts.env, self.linea, self.columna)
            
    #         listaDimensiones.append(valor)
        
    #     return listaDimensiones

    
