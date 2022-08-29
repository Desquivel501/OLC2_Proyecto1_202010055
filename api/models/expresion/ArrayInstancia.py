from models.tabla.InstanciaArreglo import InstanciaArreglo
from models.misc.error import Error_
from models.instruccion.Instruccion import Instruccion
from models.tabla.Tipos import Tipo, Tipos
from models.expresion.Expresion import Expresion



class ArrayInstancia(Expresion):

    def __init__(self, tipo, dimensiones):
        self.dimensiones = dimensiones
        self.tipo = tipo
    
    def getTipo(self, ts):
        return self.tipo
    
    def getValor(self, ts):
        
        dimencionesCompiladas = self.obtenerDimendiones(ts)
        dimendionesInt = []
        
        for exp in dimencionesCompiladas:
            dimendionesInt = exp

    
    def obtenerDimendiones(self, ts):
        listaDimensiones = []
        for dim in self.dimensiones:
            valor = dim.getValor(ts)
            tipo = dim.getTipo(ts)
            if valor.tipo != Tipos.INT:
                raise Error_("Semantico", f'Dimension de un arreglo debe de ser tipo i64', self.linea, self.columna)
            
            listaDimensiones.append(valor)
        
        return listaDimensiones
    
    
    def agregarValores(self, dimensionesCompiladas):
        anchoNuevo = dimensionesCompiladas.pop(0)
        
        valores = []
        
        if len(dimensionesCompiladas) > 0:
            subArreglo = self.agregarValores(dimensionesCompiladas)
            for i in range(0, anchoNuevo):
                valores.insert(i, subArreglo)