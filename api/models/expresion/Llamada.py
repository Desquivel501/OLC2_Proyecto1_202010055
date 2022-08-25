

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
           raise Error_("Semantico", f'No se encontro la funcion {self.identificador}', self.linea, self.columna)
             
    
    def ejecutar(self, ts: TablaSimbolos):
        self.getValor(ts)
    
    
    def getValor(self, ts: TablaSimbolos):
        funcion : Funcion = ts.obtenerFuncion(self.identificador)
        
        if funcion is not None:
            
            ts_local = TablaSimbolos(ts, "funcion")
            
            
            if len(funcion.lista_param) != len(self.listaExpresiones):
                raise Error_("Semantico", f'Cantidad de parametros incorrecto', self.linea, self.columna)
            
            i = 0
            for exp in self.listaExpresiones:
                valor_exp = exp.getValor(ts)
                tipo_exp = exp.getTipo(ts)
                
                print("--------------------------", tipo_exp)
                
                if funcion.lista_param[i].tipo.tipo != tipo_exp:
                    raise Error_("Semantico", f'Tipo incorrecto en parametro {funcion.lista_param[i].identificador}', self.linea, self.columna)
                

                nuevo = Simbolo()
                nuevo.iniciarPrimitivo(funcion.lista_param[i].identificador, funcion.lista_param[i].tipo, valor_exp, True)
                
                
                print(funcion.lista_param[i].identificador)
                ts_local.add(funcion.lista_param[i].identificador, nuevo)
                
                i += 1
            
            res = funcion.instrucciones.ejecutar(ts_local, "funcion")
            
            
            if funcion.tipo.tipo != Tipos.VOID:
               
                if res["tipo"] == "return":
                    
                    if res["exp"] is None:
                        raise Error_("Semantico", f'La funcion {self.identificador} debe poseer un return', self.linea, self.columna)
                    
                    valor_return = res["exp"].getValor(ts_local)
                    tipo_return = res["exp"].getTipo(ts_local)
                            
                    if tipo_return != funcion.tipo.tipo:
                        raise Error_("Semantico", f'Tipo de Return incorrecto', self.linea, self.columna)
                            
                    return valor_return
                
                else:
                    raise Error_("Semantico", f'La funcion {self.identificador} debe poseer un return', self.linea, self.columna)

            
            
        else:
            raise Error_("Semantico", f'No se encontro la funcion {self.identificador}', self.linea, self.columna)