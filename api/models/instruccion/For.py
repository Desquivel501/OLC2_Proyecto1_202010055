from models.tabla.InstanciaStruct import InstanciaStruct
from models.tabla.InstanciaVector import InstanciaVector
from models.tabla.InstanciaArreglo import InstanciaArreglo
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

    def __init__(self, iterador, cuerpo: Statement, linea, columna, rango = None, lista = None):
        self.rango = rango
        self.lista = lista
        self.cuerpo = cuerpo
        self.linea = linea
        self.columna = columna
        self.iterador = iterador


    def ejecutar(self, ts : TablaSimbolos):
        ts_local = TablaSimbolos(ts, "for")

        
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
                    ts_local.add(self.iterador, nuevo, self.linea, self.columna)
                    
                    res = self.cuerpo.ejecutar(ts_local)

                    if res is not None:
                        if res["tipo"] == "break":
                            break
                        if res["tipo"] == "continue":
                           continue
            else:
                raise Error_("Semantico", "Rango de For debe de ser i64", ts.env, self.linea, self.columna)
        
        if self.lista is not None:
            lista = self.lista.getValor(ts)
            lista_tipo = self.lista.getTipo(ts)
            
            if isinstance(lista, InstanciaArreglo):
                
                for i in range(0, len(lista.valores)):

                    nuevo = Simbolo()
                    nuevo.iniciarPrimitivo( self.iterador, Tipo(tipo=lista.tipo), lista.valores[i], True)
                    ts_local.add(self.iterador, nuevo, self.linea, self.columna)
                    
                    res = self.cuerpo.ejecutar(ts_local)

                    if res is not None:
                        if res["tipo"] == "break":
                            break
                        if res["tipo"] == "continue":
                           continue
            
            
            if isinstance(lista, InstanciaVector):
               
                for i in range(0, len(lista.valores)):
                    
                    if isinstance(lista.valores[i], InstanciaStruct):
                        lista.valores[i].id_instancia = self.iterador
                        
                        ts_local.add(self.iterador, lista.valores[i], self.linea, self.columna)
                    
                        for x in lista.valores[i].dic_atributos:
                            print(lista.valores[i].dic_atributos[x].valor)
                            
                        
                        prueba = ts_local.buscar(self.iterador)
                        
                        for x in prueba.dic_atributos:
                            print(prueba.dic_atributos[x].valor)
                        
                    else:
                        nuevo = Simbolo()
                        nuevo.iniciarPrimitivo( self.iterador, Tipo(tipo=lista.tipo), lista.valores[i], True)
                        ts_local.add(self.iterador, nuevo)
                    
                    res = self.cuerpo.ejecutar(ts_local)

                    if res is not None:
                        if res["tipo"] == "break":
                            break
                        if res["tipo"] == "continue":
                           continue
        
        
                    