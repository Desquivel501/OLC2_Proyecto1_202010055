
from models.tabla.Funcion import Funcion
from models.instruccion.Statement import Statement
from models.misc.error import Error_
from models.instruccion.Instruccion import Instruccion

class Modulo(Instruccion):
    
    def __init__(self, identificador:str, instrucciones, linea:int, columna: int ):
        self.identificador = identificador
        self.instrucciones = instrucciones
        self.linea = linea
        self.columna = columna
        self.entorno = None
        self.publico = False
        self.esTabla = False
        
    def ejecutar(self, ts):
        
        modulo = ts.obtenerModulo(self.identificador)
        
        if modulo is not None:
            raise Error_("Semantico", f'Modulo {self.identificador} ya ha sido declarada', ts.env, self.linea, self.columna)
        
        self.entorno = ts.nuevoEntornoMod(self.identificador)
        
        for instruccion in self.instrucciones:
            
            if isinstance(instruccion, Funcion):
                if self.esTabla:
                    if instruccion.identificador == "crear_tabla":
                        print("here***************************************************************************************************************")
                        instruccion.esCrearTabla = True
            
            if isinstance(instruccion, Modulo):
                if not self.esTabla:
                    instruccion.esTabla = True
            
            
            instruccion.ejecutar(self.entorno)
        
        ts.agregarModulo(self.identificador, self)
        
        print("creado modulo")
    