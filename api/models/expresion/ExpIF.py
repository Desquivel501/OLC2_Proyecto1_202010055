

from models.misc.Else import Else
from models.expresion.Expresion import Expresion
from models.tabla.Simbolo import Simbolo
from models.misc import driver
from models.expresion.Expresion import Expresion
from models.tabla.TablaSimbolos import TablaSimbolos
from models.expresion.Expresion import Expresion
from models.tabla.Tipos import definirTipo, Tipos
from models.misc.error import Error_


class ExpIf(Expresion):
    def __init__(self, condicion: Expresion, instrucciones , cuerpo: Expresion, else_ : Expresion, linea, columna):
        self.condicion = condicion
        self.cuerpo = cuerpo
        self.else_ = else_
        self.linea = linea
        self.columna = columna
        self.instrucciones = instrucciones
        self.tipo = None
        
        
    def getTipo(self, ts):
        return self.tipo
    
    def getValor(self, ts):

        condicion = self.condicion.getValor(ts)
        tipo_condicion = self.condicion.getTipo(ts)
        
        if tipo_condicion is not Tipos.BOOLEAN:
            raise Error_("Semantico", "La condicion en in If debe ser de tipo BOOLEAN",  ts.env, self.linea, self.columna)

        # if self.cuerpo.getTipo(ts) != self.else_.getTipo(ts):
        #     raise Error_("Semantico", "Al usar un If como expresion, cada bloque debe de ser del mismo tipo",  ts.env, self.linea, self.columna)
                
        if condicion:               
            if self.instrucciones is not None:
               
                for ins in self.instrucciones:
                    try:
                        element = ins.ejecutar(ts)
                        
                        if element is not None:
                            if element["tipo"] == "break":
                                return element
                            
                            if element["tipo"] == "continue":
                                return element
                            
                            if element["tipo"] == "return":
                                return element

                        
                    except Exception as e:
                        print(e)
            
            
            valor = self.cuerpo.getValor(ts)
            self.tipo = self.cuerpo.getTipo(ts)
            return valor

        elif self.else_ is not None:
            
            if isinstance(self.else_, Else):  
                inst_else = self.else_.instruccion
                
                if inst_else is not None:      
                    for ins in inst_else:
                        try:
                            element = ins.ejecutar(ts)
                            
                            if element is not None:
                                if element["tipo"] == "break":
                                    return element
                                
                                if element["tipo"] == "continue":
                                    return element
                                
                                if element["tipo"] == "return":
                                    return element

                            
                        except Exception as e:
                            print(e)
                            
            valor = self.else_.getValor(ts)
            self.tipo = self.else_.getTipo(ts)
            return valor
