
import copy
from models.tabla.Modulo import Modulo
from models.tabla.InstanciaStruct import InstanciaStruct
from models.instruccion.Instruccion import Instruccion
from models.tabla.Funcion import Funcion
from models.tabla.Tipos import Tipos
from models.misc.error import Error_
from models.tabla.Simbolo import Simbolo
from models.expresion.Expresion import Expresion
from models.tabla.TablaSimbolos import TablaSimbolos

class AccesoModulo(Expresion, Instruccion):
    
    def __init__(self, listaExpresiones, linea, columna):
        self.listaExpresiones = listaExpresiones
        self.tipo = None
        self.linea = linea
        self.columna = columna
        
    def ejecutar(self, ts):
        self.getValor(ts)
        
    def getTipo(self, ts: TablaSimbolos):
        if self.tipo == None:
            self.getValor(ts)
        return self.tipo
        
             
    def getValor(self, ts: TablaSimbolos):
        
        copiaLista = copy.deepcopy(self.listaExpresiones)
        
        expresionInicial = self.listaExpresiones.pop(0)
        modulo = ts.obtenerModulo(expresionInicial)

        if modulo is None:
            raise Error_("Semantico", f'No se encontro el modulo {expresionInicial}',   ts.env, self.linea, self.columna)

        entorno = modulo.entorno
        val = self.acceso(self.listaExpresiones, expresionInicial, entorno)
        self.listaExpresiones = copiaLista
        return val
        

    
    def acceso(self, listaExpresion, struct, ts):
        expresionInicial = self.listaExpresiones.pop(0)
        
        if len(listaExpresion) == 0:  
            publico = expresionInicial.checkPub(ts)

            if not publico:
                raise Error_("Semantico", f'La funcion {expresionInicial.identificador} no es publica',   ts.env, self.linea, self.columna)
            
            res = expresionInicial.getValor(ts)
            self.tipo = expresionInicial.getTipo(ts)
            return res
            
        else:
            modulo = ts.obtenerModulo(expresionInicial) 

            if modulo is None:
                raise Error_("Semantico", f'No se encontro el modulo {expresionInicial}',   ts.env, self.linea, self.columna)
            
            entorno = modulo.entorno
            return self.acceso(self.listaExpresiones, expresionInicial, entorno)
            
        
            
        
        
        
        
        
        