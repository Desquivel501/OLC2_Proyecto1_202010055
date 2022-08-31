

from models.tabla.Simbolo import Simbolo
from models.instruccion.Statement import Statement
from models.misc.error import Error_
from models.tabla.Tipos import Tipo, Tipos
from models.instruccion.Instruccion import Instruccion

class Funcion(Instruccion):
    
    def __init__(self, identificador: str, lista_param, instrucciones: Statement, tipo: Tipo, linea:int, columna: int ):
        self.identificador = identificador
        self.lista_param = lista_param
        self.tipo = tipo
        self.linea = linea
        self.columna = columna
        self.instrucciones = instrucciones
        
    def ejecutar(self, ts):
        funcion = ts.obtenerFuncion(self.identificador)
        
        if funcion is None:
            ts.agregarFuncion(self.identificador, self)
        else:
            raise Error_("Semantico", f'Funcion {self.identificador} ya ha sido declarada', self.linea, self.columna)
        

    def ejecutarParametros(self, entorno, expresiones, entorno_padre):
        
        if len(self.lista_param) != len(expresiones):
            raise Error_("Semantico", f'Cantidad de parametros incorrecto', self.linea, self.columna)
        
        i = 0
        for expresion in expresiones:
            
            valor_exp = expresion.getValor(entorno_padre)
            tipo_exp = expresion.getTipo(entorno_padre)
            
            if self.lista_param[i].tipo.tipo != tipo_exp:
                print(self.lista_param[i].tipo.tipo , " - ", tipo_exp)
                
                raise Error_("Semantico", f'Tipo incorrecto en parametro {self.lista_param[i].identificador}', self.linea, self.columna)
                
            nuevo = Simbolo()
            nuevo.iniciarPrimitivo(self.lista_param[i].identificador, self.lista_param[i].tipo, valor_exp, True)            
            entorno.add(self.lista_param[i].identificador, nuevo)
            i += 1
        
        
            
    def ejecutarFuncion(self, ts_local):
        res = self.instrucciones.ejecutar(ts_local)
        print("res f - ", res)
            
        if self.tipo.tipo != Tipos.VOID:
               
            if res["tipo"] == "return":
                    
                if res["exp"] is None:
                    raise Error_("Semantico", f'La funcion {self.identificador} debe poseer un return', self.linea, self.columna)
                    
                valor_return = res["exp"].getValor(ts_local)
                tipo_return = res["exp"].getTipo(ts_local)
                            
                if tipo_return != self.tipo.tipo:
                    raise Error_("Semantico", f'Tipo de Return incorrecto', self.linea, self.columna)

                return valor_return
                
            else:
                raise Error_("Semantico", f'La funcion {self.identificador} debe poseer un return', self.linea, self.columna)
                
                

                

           
                
          