from models.tabla.InstanciaArreglo import InstanciaArreglo
from models.misc.error import Error_
from models.instruccion.Instruccion import Instruccion
from models.tabla.Tipos import Tipo, Tipos
from models.expresion.Expresion import Expresion



class ArrayDataIntervalo(Expresion):

    def __init__(self, expresion, cantidad, linea:int, columna: int):
        self.cantidad = cantidad
        self.expresion = expresion
        self.listaDimensiones = []
        self.expresionesCompiladas = []
        self.valores = []
        self.linea = linea
        self.columna = columna
    
    def getTipo(self, ts):
        return Tipos.ARRAY_DATA
    
    def getValor(self, ts):
        
        valor_expresion = self.expresion.getValor(ts)
        tipo_expresion = self.expresion.getTipo(ts)
        
        valor_cantidad = self.cantidad.getValor(ts)
        tipo_cantidad = self.cantidad.getTipo(ts)
        
        if tipo_cantidad != Tipos.INT:
            raise Error_("Semantico", f'La cantidad que se repite una expresion debe de ser tipo i64', self.linea, self.columna)
        
        listaValores = []
        for i in range(0, valor_cantidad):
            listaValores.append(valor_expresion)

        instanciaArray = InstanciaArreglo(tipo_expresion, [valor_cantidad] , listaValores)
       
        return instanciaArray
        
        