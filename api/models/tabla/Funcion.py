

from models.misc.Program import Program
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
        self.publico = False
        self.esCrearTabla = False
        
    def ejecutar(self, ts):
        funcion = ts.obtenerFuncion(self.identificador)
        
        if funcion is None:
            ts.agregarFuncion(self.identificador, self)
        else:
            raise Error_("Semantico", f'Funcion {self.identificador} ya ha sido declarada', ts.env, self.linea, self.columna)
        

    def ejecutarParametros(self, entorno, expresiones, entorno_padre):
        
        if len(self.lista_param) != len(expresiones):
            raise Error_("Semantico", f'Cantidad de parametros incorrecto', "", self.linea, self.columna)
        
        i = 0
        for expresion in expresiones:
            
            valor_exp = expresion.getValor(entorno_padre)
            tipo_exp = expresion.getTipo(entorno_padre)
            
            if self.lista_param[i].tipo.tipo != tipo_exp:
                
                raise Error_("Semantico", f'Tipo incorrecto en parametro {self.lista_param[i].identificador}', entorno.env, self.linea, self.columna)
                
            nuevo = Simbolo()
            nuevo.iniciarPrimitivo(self.lista_param[i].identificador, self.lista_param[i].tipo, valor_exp, True)            
            entorno.add(self.lista_param[i].identificador, nuevo, self.linea, self.columna)
            i += 1
        
        
            
    def ejecutarFuncion(self, ts_local):
        
        if(self.esCrearTabla):
            
            base_datos = ts_local.anterior.anterior.env
            tabla = ts_local.anterior.env
            
            instancia_base = ts_local.obtenerModulo(base_datos)
            instancia_tabla = ts_local.obtenerModulo(tabla)
            
            if len(Program.lista_bases) == 0:
                linea = instancia_base.linea
                Program.lista_bases.append({"nombre_base":base_datos, "cantidad": 1, "linea":linea})

            else:
                for base in Program.lista_bases:
                    
                    if base_datos == base.get("nombre_base"):
                        base["cantidad"] += 1
                    
                    else:
                        linea = instancia_base.linea
                        Program.lista_bases.append({"nombre_base":base_datos, "cantidad": 1, "linea":linea})

            Program.lista_tablas.append({"nombre_base":base_datos, "nombre_tablas":tabla, "linea":instancia_tabla.linea})
            
                
        
        codigo = self.instrucciones.codigo
        
        for ins in codigo:
            
            if ins is None:
                continue
            
            try:
                element = ins.ejecutar(ts_local)
                
                if element is not None:
                    if element["tipo"] == "break":
                        raise Error_("Semantico", f'No se puede ejecutar un Break fuera de un ciclo', ts_local.env, self.linea, self.columna)
                    
                    if element["tipo"] == "continue":
                        raise Error_("Semantico", f'No se puede ejecutar un Continue fuera de un ciclo', ts_local.env, self.linea, self.columna)
                    
                    if element["tipo"] == "return":
                        
                        if self.tipo.tipo != Tipos.VOID:
                            if element["exp"] is None:
                                raise Error_("Semantico", f'La funcion {self.identificador} debe poseer un return', ts_local.env, self.linea, self.columna)
                            
                            valor_return = element["exp"].getValor(ts_local)
                            tipo_return = element["exp"].getTipo(ts_local)
                            
                            if tipo_return != self.tipo.tipo:
                                raise Error_("Semantico", f'Tipo de Return incorrecto', ts_local.env, self.linea, self.columna)

                            return valor_return
                        else:
                            raise Error_("Semantico", f'La funcion {self.identificador} debe poseer un return tipo {ts_local.getTiposNombre(self.tipo.tipo)}', ts_local.env, self.linea, self.columna)

                
            except Exception as e:
                print(e)
        
        
            
        # for ins in codigo:
        #         element = ins.ejecutar(ts_local)
                
        #         if element is not None:
        #             if element["tipo"] == "break":
        #                 raise Error_("Semantico", f'No se puede ejecutar un Break fuera de un ciclo', ts_local.env, self.linea, self.columna)
                    
        #             if element["tipo"] == "continue":
        #                 raise Error_("Semantico", f'No se puede ejecutar un Continue fuera de un ciclo', ts_local.env, self.linea, self.columna)
                    
        #             if element["tipo"] == "return":
                        
        #                 if self.tipo.tipo != Tipos.VOID:
        #                     if element["exp"] is None:
        #                         raise Error_("Semantico", f'La funcion {self.identificador} debe poseer un return', ts_local.env, self.linea, self.columna)
                            
        #                     valor_return = element["exp"].getValor(ts_local)
        #                     tipo_return = element["exp"].getTipo(ts_local)
                            
        #                     if tipo_return != self.tipo.tipo:
        #                         raise Error_("Semantico", f'Tipo de Return incorrecto', ts_local.env, self.linea, self.columna)

        #                     return valor_return
        #                 else:
        #                     raise Error_("Semantico", f'La funcion {self.identificador} debe poseer un return tipo {ts_local.getTiposNombre(self.tipo.tipo)}', ts_local.env, self.linea, self.columna)
                        

        

                

           
                
          