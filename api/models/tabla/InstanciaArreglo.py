
from struct import Struct
from models.misc.error import Error_
from models.instruccion.Instruccion import Instruccion
from models.tabla.Tipos import Tipo, Tipos
from models.expresion.Expresion import Expresion

class InstanciaArreglo(Expresion):

    def __init__(self,tipo, dimensiones, valores):
        self.dimensiones = dimensiones
        self.valores = valores
        self.tipo = tipo
        self.identificador = None

    def getTipo(self, ts):
        return self.tipo
    
    def getValor(self, listaDimensiones, index, valores):
        print("Instancia - ", self.id_instancia)

        indiceDimension:int = listaDimensiones.pop(0)
        tamanoDimension:int = self.dimensiones[index]

        if len(listaDimensiones) > 0:

            if indiceDimension > (tamanoDimension-1):
                return None
            else:
                subArreglo = valores[indiceDimension]
                return self.getValor(listaDimensiones, index+1, subArreglo)

        else:
            if indiceDimension > (tamanoDimension-1):
                return None
            else:
                return valores[indiceDimension]