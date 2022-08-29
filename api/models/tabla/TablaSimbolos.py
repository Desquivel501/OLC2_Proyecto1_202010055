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
        self.variables = {}
        self.funciones = {}
        self.structs = {}
        self.instancias_structs = {}
        self.arreglos = {}

    def add(self, id: str, simbolo: Simbolo):
        self.variables[id] = simbolo
        Program.tabla[id] = (simbolo, self.env)

    def buscar(self, id: str) -> Simbolo:
        ts = self

        while ts is not None:
            exist = ts.variables.get(id)
            if exist is not None:
                return exist
            ts = ts.anterior
        return None

    def buscarActual(self, id: str) -> Simbolo:
        return self.variables.get(id)
    
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
    
    

