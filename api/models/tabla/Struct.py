from models.instruccion.Statement import Statement
from models.misc.error import Error_
from models.instruccion.Instruccion import Instruccion

class Struct(Instruccion):
    
    def __init__(self, identificador:str, campos, linea:int, columna: int ):
        self.identificador = identificador
        self.campos = campos
        self.linea = linea
        self.columna = columna
        self.publico = False
        
    def ejecutar(self, ts):
        struct = ts.obtenerStruct(self.identificador)
        if struct is not None:
            raise Error_("Semantico", f'Struct {self.identificador} ya ha sido declarado', ts.env, self.linea, self.columna)
        
        ts.agregarStruct(self.identificador, self)
        
        
    