


from models.tabla.Tipos import Tipo
from models.misc.error import Error_
from models.tabla.Simbolo import Simbolo
from models.misc import driver
from models.expresion.Expresion import Expresion
from models.tabla.TablaSimbolos import TablaSimbolos

class Parametro():
    
    def __init__(self, identificador: str, tipo: Tipo):
        self.identificador = identificador
        self.tipo = tipo
