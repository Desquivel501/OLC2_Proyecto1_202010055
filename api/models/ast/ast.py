from models.expresion.Llamada import Llamada
from models.tabla.TablaSimbolos import TablaSimbolos
from models.instruccion import Instruccion
from models.tabla.Funcion import Funcion
from models.misc.error import Error_
from models.tabla.Struct import Struct


class Ast:

    def __init__(self, instrucciones=None):
        if instrucciones is None:
            instrucciones = []

        self.instrucciones = instrucciones
        self.ts = None

    def ejecutar(self, ts):
        for instruccion in self.instrucciones:
            
            if isinstance(instruccion, Funcion):
                fun = ts.obtenerFuncion(instruccion.identificador)
                if fun is None:
                    instruccion.ejecutar(ts)
            
            
            if isinstance(instruccion, Struct):
                struct = ts.obtenerStruct(instruccion.identificador)
                if struct is None:
                    instruccion.ejecutar(ts)

        main = ts.obtenerFuncion("main")
        
        if main is not None:
            main.instrucciones.ejecutar(ts)
        else:
            raise Error_('Semantico', f'No existe metodo main', 0, 0)
        
        self.ts = ts
    
    