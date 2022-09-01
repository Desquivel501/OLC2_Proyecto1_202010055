


import copy
from models.expresion.AccesoStruct import AccesoStruct
from models.expresion.AccesoArreglo import AccesoArreglo
from models.expresion.Identificador import Identificador
from models.tabla.InstanciaStruct import InstanciaStruct
from models.instruccion.Instruccion import Instruccion
from models.misc.error import Error_
from models.expresion.Expresion import Expresion
from models.tabla.TablaSimbolos import TablaSimbolos

class ModStruct(Instruccion):
    
    def __init__(self, listaExpresiones, valor:Expresion, linea:int, columna:int):
        self.listaExpresiones = listaExpresiones
        self.linea = linea
        self.columna = columna
        self.valor = valor
        
     
    def ejecutar(self, ts: TablaSimbolos):
        print("MOD********************************************")
        
        copia = copy.deepcopy(self.listaExpresiones)
        
        expresionInicial = self.listaExpresiones.pop(0)
        
        struct = ts.buscar(expresionInicial)

        identificador = ""
        if isinstance(expresionInicial, Identificador):
            print("id")
            identificador = expresionInicial.getValor(ts)

            if isinstance(identificador, InstanciaStruct):
                print("struct")
                struct = identificador
            
            else:
                struct = ts.buscar(expresionInicial)
        
        if isinstance(expresionInicial, AccesoArreglo):
            print("arreglo")
            val = expresionInicial.getValor(ts)
            print("VALOR -- ", )
            
            if isinstance(val, InstanciaStruct):
                print("struct")
                struct = val
                
            
        if struct is None:
            raise Error_("Semantico", f'No se encontro el simbolo {expresionInicial}', ts.env, self.linea, self.columna)
        
        if not isinstance(struct, InstanciaStruct):
            raise Error_("Semantico", f'Simbolo \'{self.identificador}\' no es de tipo Struct', ts.env, self.linea, self.columna)
        
        # if not struct.mut:
        #      raise Error_("Semantico", f'No se puede modificar un struct constante', ts.env, self.linea, self.columna)
        
        self.acceso(self.listaExpresiones, struct, ts)
        
        self.listaExpresiones = copia
                    
        
    
    def acceso(self, listaExpresion, struct, ts):
        expresionInicial = self.listaExpresiones.pop(0)
        
        if isinstance(expresionInicial, Identificador):
            expresionInicial = expresionInicial.identificador
        
        if len(listaExpresion) == 0:
            
            valor = struct.dic_atributos.get(expresionInicial)
            
            if valor is not None:
                viejo_valor = struct.dic_atributos[expresionInicial].valor
                viejo_tipo = struct.dic_atributos[expresionInicial].tipo
                
                nuevo_valor = self.valor.getValor(ts)
                nuevo_tipo = self.valor.getTipo(ts)
                
                print(viejo_tipo, " - ", nuevo_tipo)
                
                if viejo_tipo == nuevo_tipo:
                    struct.dic_atributos[expresionInicial].valor = nuevo_valor
                    return struct
                
                else:
                    raise Error_("Semantico", f'Tipo incorrecto en atributo {expresionInicial}', ts.env, self.linea, self.columna)
 
            else:
                raise Error_("Semantico", f'No se encontro el atributo {expresionInicial}', ts.env, self.linea, self.columna)
            
        else:
            nuevo_struct = struct.dic_atributos[expresionInicial].valor
            
            # if not nuevo_struct.mut:
            #     raise Error_("Semantico", f'No se puede modificar un struct constante', ts.env, self.linea, self.columna)
            
            if nuevo_struct is not None:
                struct.dic_atributos[expresionInicial].valor = self.acceso(self.listaExpresiones, nuevo_struct, ts)
                
                return struct
            
            else:
                raise Error_("Semantico", f'No se encontro el simbolo {expresionInicial}', ts.env, self.linea, self.columna)
            
        
        
        
        
        
        