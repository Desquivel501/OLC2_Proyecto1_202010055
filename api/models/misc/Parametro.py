
from models.tabla.Tipos import Tipo

class Parametro():
    
    def __init__(self, identificador: str, tipo: Tipo):
        self.identificador = identificador
        self.tipo = tipo
