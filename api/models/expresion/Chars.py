from models.tabla.InstanciaVector import InstanciaVector
from models.tabla.InstanciaArreglo import InstanciaArreglo
from models.misc.error import Error_
from models.instruccion.Instruccion import Instruccion
from models.tabla.Tipos import Tipo, Tipos
from models.expresion.Expresion import Expresion



class Chars(Expresion):

    def __init__(self, expresion, linea:int, columna: int):
        self.expresion = expresion
        self.valores = []
        self.linea = linea
        self.columna = columna
    
    def getTipo(self, ts):
        return Tipos.ARRAY_DATA
    
    def getValor(self, ts):
        
        valor_expresion = self.expresion.getValor(ts)
        tipo_expresion = self.expresion.getTipo(ts)
    
        
        if tipo_expresion not in [Tipos.STR, Tipos.STRING] :
            raise Error_("Semantico", f'La funcion CHARS solo acepta valores tipo &str y String', self.linea, self.columna)
        
        listaValores = list(valor_expresion)
    
        instanciaArray = InstanciaArreglo(tipo_expresion, [len(listaValores)] , listaValores)
       
        return instanciaArray
        
        