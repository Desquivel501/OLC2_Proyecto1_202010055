from models.misc.error import Error_
from models.instruccion.Instruccion import Instruccion

from models.tabla.Simbolo import Simbolo, Simbolos
from models.misc import driver
from models.expresion.Expresion import Expresion
from models.tabla.TablaSimbolos import TablaSimbolos
from models.tabla.Tipos import Tipo, definirTipo
from models.misc.driver import Driver

class Asignacion(Instruccion):
    
    def __init__(self, identificador: str, variable: Simbolo, tipo: Tipo, mut:bool, linea:int, columna: int ):
        self.identificador = identificador
        self.variable = variable
        self.tipo = tipo
        self.mut = mut
        self.linea = linea
        self.columna = columna
        
    def ejecutar(self, ts: TablaSimbolos):
        
        var_tipo = self.variable.valor.getTipo( ts)
        var_valor = self.variable.valor.getValor(ts)
        
        if self.tipo is not None:
            if self.tipo.tipo != var_tipo:
                print(f'El valor de la variable no coincide con su tipo')
                raise Error_("Semantica", "El valor de la variable no coincide con su tipo'", self.linea, self.columna)
        else:
            self.tipo = Tipo(var_tipo)
            
        simbolo = ts.buscar(self.identificador);
        
        if simbolo is None:
            nuevo = Simbolo(Simbolos.VARIABLE, self.tipo, self.identificador, var_valor, self.mut)
            ts.add(self.identificador, nuevo)
            
            print("creado: " + self.identificador)
        
        else:
            if simbolo.tipo.tipo != var_tipo:
                print(f'El valor de la variable no coincide con su tipo')
                
            elif simbolo.mut is False:
                print(f'No se puede cambiar el valor de una constante')
            else:
                simbolo.valor = var_valor
                ts.add(self.identificador, simbolo)
                
            
       
        
        
    