
from models.tabla.InstanciaStruct import InstanciaStruct
from models.tabla.Simbolo import Simbolo
from models.misc.error import Error_

from models.tabla.Tipos import Tipo, Tipos
from models.expresion.Expresion import Expresion

class InstanciaVector(Expresion, Simbolo):

    def __init__(self,tipo, dimensiones, valores):
        self.dimensiones = dimensiones
        self.valores = valores
        self.tipo = tipo
        self.capacidad = None
        self.identificador = None
        self.mut = False
        

    def getTipo(self, ts):
        return self.tipo
    
    def getValor(self, listaDimensiones, index, valores, linea, columna):
        indiceDimension:int = listaDimensiones.pop(0)
        
        if isinstance(self.valores[index], InstanciaStruct):
            tamanoDimension:int = len(self.valores)
        
        else:
            tamanoDimension:int = len(self.valores[index])
        

        if len(listaDimensiones) > 0:
            
            if indiceDimension > (tamanoDimension-1):
                print(indiceDimension, " - ", tamanoDimension)
                raise Error_("Semantico", f'Índice fuera de los límites', "", linea, columna)
            else:
                subArreglo = valores[indiceDimension]
                return self.getValor(listaDimensiones, index+1, subArreglo, linea, columna)

        else:
            if indiceDimension > (tamanoDimension-1):
                print(indiceDimension, " - ", tamanoDimension)
                raise Error_("Semantico", f'Índice fuera de los límites', "", linea, columna)
            else:
                return valores[indiceDimension]
        
        
    def push(self, valor, linea, columna):
        if self.capacidad == len(self.valores):
            self.capacidad += 1       
        self.valores.append(valor)

    def insert(self, valor, indice ,linea, columna):
        if self.capacidad == len(self.valores):
            self.capacidad += 1 
        self.valores.insert(indice, valor)
    
    def remove(self, indice ,linea, columna):  
        return self.valores.pop(indice)
    
    def contains(self, valor, linea, columna):
        if valor in self.valores:
            return True
        return False
        
    