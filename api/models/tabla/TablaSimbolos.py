from models.tabla.Modulo import Modulo
from models.tabla.Tipos import Tipo
from models.tabla.Tipos import Tipos
from models.tabla.InstanciaVector import InstanciaVector
from models.tabla.InstanciaArreglo import InstanciaArreglo
from models.tabla.InstanciaStruct import InstanciaStruct
from models.tabla.Struct import Struct
from models.tabla.Funcion import Funcion
from models.misc.Program import Program
from models.tabla.Simbolo import Simbolo

class TablaSimbolos:

    def __init__(self, anterior, env):
        self.env = env
        self.anterior = anterior
        self.tabla = {}
        self.variables = {}
        self.funciones = {}
        self.structs = {}
        self.instancias_structs = {}
        self.arreglos = {}
        self.vectores = {}
        self.modulos = {}

    def add(self, id: str, simbolo: Simbolo, linea, columna):
        # print("ID: ", id)
        # print("SIMBOLO: ", simbolo)
        self.tabla[id] = simbolo
        
        data = self.getTipos(simbolo)
        
        tipo = data[0]
        tipo_s = data[1]
        
        Program.tabla.append({"id":id, "simbolo": tipo_s, "tipo":tipo,  "ambito":self.env, "linea": linea, "columna": columna})

    def buscar(self, id: str) -> Simbolo:
        ts = self

        while ts is not None:
            exist = ts.tabla.get(id)
            if exist is not None:
                return exist
            ts = ts.anterior
        return None

    def buscarActual(self, id: str) -> Simbolo:
        return self.tabla.get(id)

    def getGlobal(self):
        env = self
        while env.anterior is not None:
            env = env.anterior
        return env

    #-------------------------------------------FUNCIONES-----------------------------------------------

    def agregarFuncion(self, id: str,  func: Funcion):
        self.funciones[id] = func


    def obtenerFuncion(self, id: str):
        ts = self
        while ts is not None:
            exist = ts.funciones.get(id)
            if exist is not None:
                return exist
            ts = ts.anterior
        return None

     #-------------------------------------------STRUCTS-----------------------------------------------

    def agregarStruct(self, id: str,  struct: Struct):
        self.structs[id] = struct


    def obtenerStruct(self, id: str):
        ts = self
        while ts is not None:
            exist = ts.structs.get(id)
            if exist is not None:
                return exist
            ts = ts.anterior
        return None

    def obtenerInstancia(self, id:str):
        ts = self
        while ts is not None:
            exist = ts.instancias_structs.get(id)
            if exist is not None:
                return exist
            ts = ts.anterior
        return None

    def agregarIntancia(self, id: str,  struct: InstanciaStruct):
        self.instancias_structs[id] = struct


    #-------------------------------------------ARREGLOS-----------------------------------------------

    def agregarArreglo(self, id: str,  arreglo: InstanciaArreglo):
        self.arreglos[id] = arreglo


    def obtenerArreglo(self, id: str):
        ts = self
        while ts is not None:
            exist = ts.arreglos.get(id)
            if exist is not None:
                return exist
            ts = ts.anterior
        return None

        #-----------------------------------------VECTORES-----------------------------------------------

    def agregarVector(self, id: str,  vector: InstanciaVector):
        self.vectores[id] = vector


    def obtenerVector(self, id: str):
        ts = self
        while ts is not None:
            exist = ts.vectores.get(id)
            if exist is not None:
                return exist
            ts = ts.anterior
        return None
    

#-------------------------------------------MODULOS-----------------------------------------------

    def agregarModulo(self, id: str,  mod: Modulo):
        self.modulos[id] = mod


    def obtenerModulo(self, id: str):
        ts = self
        while ts is not None:
            exist = ts.modulos.get(id)
            if exist is not None:
                return exist
            ts = ts.anterior
        return None
    
    def nuevoEntornoMod(self, identificador):
        ts_modulo = TablaSimbolos(self, identificador)
        return ts_modulo


#-------------------------------------------TIPOS REPORTE-----------------------------------------------

    def getTiposNombre(self, s):
        
        if isinstance(s, Tipo):
            s = s.tipo
        
        if s == Tipos.INT:
            return "i64"
        if s == Tipos.FLOAT:
            return "f64"
        if s == Tipos.BOOLEAN:
            return "bool"
        if s == Tipos.STR:
            return "&str"
        if s == Tipos.STRING:
            return "String"
        if s == Tipos.CHAR:
            return "char"
        if s == Tipos.ARRAY_DATA:
            return "Arreglo "
        if s == Tipos.VECTOR_DATA:
            return "Vector"
        if s == Tipos.STRUCT:
            return "Struct"
        else:
            return ""
            

    def getTipos(self, simbolo):
        if isinstance(simbolo, InstanciaVector):
            tipo = self.getTiposNombre(simbolo.tipo)
            tipo_s = "Vector"
        elif isinstance(simbolo, InstanciaVector):
            tipo = self.getTiposNombre(simbolo.tipo)
            tipo_s = "Vector"
        elif isinstance(simbolo, InstanciaArreglo):
            tipo = self.getTiposNombre(simbolo.tipo)
            tipo_s = "Arreglo"
        elif isinstance(simbolo, InstanciaStruct):
            tipo = ""
            tipo_s = "Struct"
        else:
            if isinstance(simbolo.valor, InstanciaVector):
                tipo = self.getTiposNombre(simbolo.tipo)
                tipo_s = "Vector"
            elif isinstance(simbolo.valor, InstanciaVector):
                tipo = self.getTiposNombre(simbolo.tipo)
                tipo_s = "Vector"
            elif isinstance(simbolo.valor, InstanciaArreglo):
                tipo = self.getTiposNombre(simbolo.tipo)
                tipo_s = "Arreglo"
            elif isinstance(simbolo.valor, InstanciaStruct):
                tipo = ""
                tipo_s = "Struct"
            else:
                tipo = self.getTiposNombre(simbolo.tipo.tipo)
                tipo_s = "Primitivo"

        return (tipo, tipo_s)
    
    