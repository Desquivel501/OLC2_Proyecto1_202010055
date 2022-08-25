from models.misc.error import Error_
from models.instruccion.Instruccion import Instruccion

from models.tabla.Simbolo import Simbolo, Simbolos
from models.misc import driver
from models.expresion.Expresion import Expresion
from models.tabla.TablaSimbolos import TablaSimbolos
from models.tabla.Tipos import Tipo

class Asignacion(Instruccion):
    
    def __init__(self, identificador: str, valor: Expresion, tipo: Tipo, mut:bool, linea:int, columna: int ):
        self.identificador = identificador
        self.valor = valor
        self.tipo = tipo
        self.mut = mut
        self.linea = linea
        self.columna = columna
        
    def ejecutar(self, ts: TablaSimbolos):
        
        var_tipo = self.valor.getTipo(ts)
        var_valor = self.valor.getValor(ts)
        
        print("tipo: ", var_tipo)
        
        if self.tipo is not None:
            if self.tipo.tipo != var_tipo:
                print('Semantica', f'El valor de la variable no coincide con su tipo: {self.tipo.tipo} -> {var_tipo}')
                raise Error_('Semantica', f'El valor de la variable no coincide con su tipo: { self.tipo.tipo} -> {var_tipo}', self.linea, self.columna)
        else:
            
            self.tipo = Tipo(tipo = var_tipo)
            
        simbolo = ts.buscar(self.identificador);
        
        if simbolo is None:
            nuevo = Simbolo()
            nuevo.iniciarPrimitivo( self.identificador, self.tipo, var_valor, self.mut)
            ts.add(self.identificador, nuevo)
            
            print("creado: " + self.identificador)
        
        else:
            if simbolo.tipo.tipo != var_tipo:
                print(f'El valor de la variable no coincide con su tipo: {simbolo.tipo.tipo} -> {var_tipo}')
                raise Error_(f'Semantica", "El valor de la variable no coincide con su tipo: {simbolo.tipo.tipo} -> {var_tipo}', self.linea, self.columna)
                
            elif simbolo.mut is False:
                print(f'No se puede cambiar el valor de una constante')
                raise Error_("Semantica", "No se puede cambiar el valor de una constante", self.linea, self.columna)
            else:
                simbolo.valor = var_valor
                ts.add(self.identificador, simbolo)
                
            
       
        
        
    