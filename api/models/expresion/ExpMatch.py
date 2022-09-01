

from models.expresion.Expresion import Expresion
from models.tabla.Simbolo import Simbolo
from models.misc import driver
from models.expresion.Expresion import Expresion
from models.tabla.TablaSimbolos import TablaSimbolos
from models.expresion.Expresion import Expresion
from models.tabla.Tipos import definirTipo, Tipos
from models.misc.error import Error_


class ExpMatch(Expresion):
    def __init__(self, condicion: Expresion, case_list, default, linea, columna):
        self.condicion = condicion
        self.case_list = case_list
        self.default = default
        self.linea = linea
        self.columna = columna
        self.correcto = True
        
        
    def getTipo(self, ts):
        incorrecto = False
        tipo_res = None         
        for case in self.case_list:
            if tipo_res is None:
                tipo_res = case.getTipo(ts)
            elif  tipo_res != case.getTipo(ts):
                incorrecto = True
                    
        if incorrecto :
            raise Error_("Semantico", "Todas las opciones de un Match deben de ser del mismo tipo",   ts.env, self.linea, self.columna)
        
        return tipo_res
    
    def getValor(self, ts):
        condicion = self.condicion.getValor(ts)
        tipo_condicion = self.condicion.getTipo(ts)
        
        incorrecto = False
        
        for case in self.case_list:
            for opcion in case.lista_exp:
                if tipo_condicion != opcion.getTipo(ts):
                    incorrecto = True
           
        tipo_res = None         
        for case in self.case_list:
            if tipo_res is None:
                tipo_res = case.getTipo(ts)
            elif  tipo_res != case.getTipo(ts):
                incorrecto = True
                    
        if incorrecto :
            raise Error_("Semantico", "Todas las opciones de un Match deben de ser del mismo tipo",   ts.env, self.linea, self.columna)
        
        
        found = False
        for case in self.case_list:  
            found_case = False
            for opcion in case.lista_exp:
                if opcion.getValor(ts) == condicion:
                    found_case = True
                    break
            if found_case is True:
                return case.getValor(ts)
        
        if not found and self.default is not None:
            return self.default.getValor(ts)
