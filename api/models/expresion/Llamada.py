

from models.instruccion.Instruccion import Instruccion
from models.tabla.Funcion import Funcion
from models.tabla.Tipos import Tipos
from models.misc.error import Error_
from models.tabla.Simbolo import Simbolo
from models.expresion.Expresion import Expresion
from models.tabla.TablaSimbolos import TablaSimbolos

class Llamada(Expresion, Instruccion):
    
    def __init__(self, identificador: str, listaExpresiones, linea: int, columna: int):
        self.identificador = identificador
        self.linea = linea
        self.columna = columna
        self.listaExpresiones = listaExpresiones
        
    def getTipo(self, ts: TablaSimbolos):
        funcion = ts.obtenerFuncion(self.identificador)
        
        if funcion is not None:
            return funcion.tipo.tipo
        else:
           raise Error_("Semantico", f'No se encontro la funcion {self.identificador}', ts.env, self.linea, self.columna)
             
    
    def ejecutar(self, ts: TablaSimbolos):
        self.getValor(ts)
    
    
    def getValor(self, ts: TablaSimbolos):
        funcion : Funcion = ts.obtenerFuncion(self.identificador)
        
        if funcion is not None:
            
            ts_local = TablaSimbolos(ts, "funcion")
            
            funcion.ejecutarParametros(ts_local,self.listaExpresiones,ts)
            
            retorno = funcion.ejecutarFuncion(ts_local)
            
            if retorno is not None:
                return retorno
            
            
        else:
            raise Error_("Semantico", f'No se encontro la funcion {self.identificador}', ts.env, self.linea, self.columna)