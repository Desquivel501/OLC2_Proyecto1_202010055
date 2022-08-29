from models.tabla.Tipos import Tipo
from models.tabla.Simbolo import Simbolo
from models.instruccion.Statement import Statement
from models.expresion.Expresion import Expresion
from models.tabla.TablaSimbolos import TablaSimbolos
from models.misc.Program import Program
from models.instruccion.Instruccion import Instruccion
from models.tabla.Tipos import Tipos
from models.misc.error import Error_


class For(Instruccion):

    def __init__(self, iterador, cuerpo: Statement, linea, columna, rango = None, arreglo = None , ):
        self.rango = rango
        self.arreglo = arreglo
        self.cuerpo = cuerpo
        self.linea = linea
        self.columna = columna
        self.iterador = iterador


    def ejecutar(self, ts):
        ts_local = TablaSimbolos(ts, "FOR")

        
        if self.rango is not None:
            
            valor_inicio = self.rango.inicio.getValor(ts)
            valor_fin = self.rango.fin.getValor(ts)
             
            tipo_inicio = self.rango.inicio.getTipo(ts)
            tipo_fin = self.rango.fin.getTipo(ts)
            
            print(valor_inicio, " - ", valor_fin)
            
            if tipo_inicio == Tipos.INT and tipo_fin == Tipos.INT:
                print("here")
                
                for i in range(valor_inicio, valor_fin):

                    nuevo = Simbolo()
                    nuevo.iniciarPrimitivo( self.iterador, Tipo(tipo=tipo_fin), i, True)
                    ts_local.add(self.iterador, nuevo)
                    
                    res = self.cuerpo.ejecutar(ts_local)

                    if res is not None:
                        if res["tipo"] == "break":
                            break
                        if res["tipo"] == "continue":
                           continue
            else:
                raise Error_("Semantico", "Rango de For debe de ser i64", self.linea, self.columna)
                    
        
        # res = None
        # ts_local = TablaSimbolos(ts, "WHILE")
        
        # condicion = self.condicion.getValor(ts)
        # tipo_condicion = self.condicion.getTipo(ts)
        
        # if tipo_condicion is not Tipos.BOOLEAN:
        #     raise Error_("Semantico", "La condicion en un WHILE debe ser de tipo BOOLEAN", self.linea, self.columna)
        
        # i = 0
        # while condicion:
            
        #     res = self.cuerpo.ejecutar(ts_local)
                
        #     if res is not None:
        #         if res["tipo"] == "break":
        #             break
        #         if res["tipo"] == "continue":
        #             continue
            
            
            
        #     condicion = self.condicion.getValor(ts)
        
