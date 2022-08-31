

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
        expresionInicial = self.listaExpresiones.pop(0)
        
        struct = ts.buscar(expresionInicial)
        
        if struct is None:
            raise Error_("Semantico", f'No se encontro el simbolo {expresionInicial}', self.linea, self.columna)
        
        if not isinstance(struct, InstanciaStruct):
            raise Error_("Semantico", f'Simbolo \'{self.identificador}\' no es de tipo Struct', self.linea, self.columna)
        
        if not struct.mut:
             raise Error_("Semantico", f'No se puede modificar un struct constante', self.linea, self.columna)
        
        self.acceso(self.listaExpresiones, struct, ts)
                    
        
    
    def acceso(self, listaExpresion, struct, ts):
        expresionInicial = self.listaExpresiones.pop(0)
        
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
                    raise Error_("Semantico", f'Tipo incorrecto en atributo {expresionInicial}', self.linea, self.columna)
 
            else:
                raise Error_("Semantico", f'No se encontro el atributo {expresionInicial}', self.linea, self.columna)
            
        else:
            nuevo_struct = struct.dic_atributos[expresionInicial].valor
            
            if not nuevo_struct.mut:
                raise Error_("Semantico", f'No se puede modificar un struct constante', self.linea, self.columna)
            
            if nuevo_struct is not None:
                struct.dic_atributos[expresionInicial].valor = self.acceso(self.listaExpresiones, nuevo_struct, ts)
                
                return struct
            
            else:
                raise Error_("Semantico", f'No se encontro el simbolo {expresionInicial}', self.linea, self.columna)
            
        
        
        
        
        
        