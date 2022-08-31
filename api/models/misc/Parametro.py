
from models.tabla.Tipos import Tipo

class Parametro():
    
    def __init__(self, identificador: str, tipo: Tipo, referencia:bool):
        self.identificador = identificador
        self.tipo = tipo
        self.referencia = referencia
