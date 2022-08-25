from models.tabla.Funcion import Funcion
from models.misc.Program import Program
from models.tabla.Simbolo import Simbolo

class TablaSimbolos:

    def __init__(self, anterior, env):
        self.env = env
        self.anterior = anterior
        self.variables = {}
        self.funciones = {}

    def add(self, id: str, simbolo: Simbolo):
        print("creado - ", id)
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
    

