from models.misc.error import Error_
from models.instruccion.Instruccion import Instruccion
from models.expresion.Expresion import Expresion
from models.misc.Program import Program


class Print_(Instruccion):

    def __init__(self, cadena: Expresion, list_exp, linea, columna):
        self.columna = columna
        self.linea = linea
        self.cadena = cadena
        self.list_exp = list_exp

    def ejecutar(self, ts):
        
        cadena = str(self.cadena.getValor(ts))
        
        if self.list_exp is not None:
            
            for exp in self.list_exp:
               
                x = cadena.find("{}")
                if x == -1:
                    raise Error_("Semantico", "Numero incorrecto de parametros en Println!", self.linea, self.columna)
                else:
                    cadena = cadena.replace("{}", str(exp.getValor(ts)),1)
           
            
        x  = cadena.find("{}")
        if x != -1:
            raise Error_("Semantico", "Numero incorrecto de parametros en Println!", self.linea, self.columna)
            

            
        Program.console += cadena + "\n"