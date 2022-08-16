
from operator import truediv
from models.instruccion.Statement import Statement
from models.expresion.Expresion import Expresion
from models.tabla.TablaSimbolos import TablaSimbolos
from models.misc.Program import Program
from models.instruccion.Instruccion import Instruccion
from models.instruccion.Case import Case
from models.tabla.Tipos import Tipos
from models.misc.error import Error_


class Match(Instruccion):

    def __init__(self, condicion: Expresion, case_list, default, linea, columna):
        self.condicion = condicion
        self.case_list = case_list
        self.default = default
        self.linea = linea
        self.columna = columna


    def ejecutar(self, ts):
        
        ts_local = TablaSimbolos(ts, "MATCH")
        condicion = self.condicion.getValor(ts)
        tipo_condicion = self.condicion.getTipo(ts)
       
        incorrecto = False
        tipo = tipo_condicion
        for case in self.case_list:
            for opcion in case.lista_exp:
                if tipo != opcion.getTipo(ts):
                    incorrecto = True
            
        if incorrecto :
            raise Error_("Semantico", "Todas las opciones de un Match deben de ser del mismo tipo", self.linea, self.columna)
            
            
        found = False
        for case in self.case_list:
            found_case = False

            for opcion in case.lista_exp:
                
                if opcion.getValor(ts) == condicion:
                    found_case = True
                    print("Found")
                    break
                
            if found_case is True:
                print("Ejecutar")
                return case.codigo.ejecutar(ts_local)
        
        if not found and self.default is not None:
            print("Default")
            return self.default.ejecutar(ts_local)
            
            
        