from models.expresion.AccesoStruct import AccesoStruct
from models.instruccion.CrearInstanciaStruct import CrearInstanciaStruct
from models.tabla.InstanciaStruct import InstanciaStruct
from models.misc.error import Error_
from models.instruccion.Instruccion import Instruccion

from models.tabla.Simbolo import Simbolo, Simbolos
from models.misc import driver
from models.expresion.Expresion import Expresion
from models.tabla.TablaSimbolos import TablaSimbolos
from models.tabla.Tipos import Tipo

class Asignacion(Instruccion):
    
    def __init__(self, identificador: str, valor: Expresion, tipo: Tipo, mut:bool, linea:int, columna: int , referencia = False):
        self.identificador = identificador
        self.valor = valor
        self.tipo = tipo
        self.mut = mut
        self.linea = linea
        self.columna = columna
        self.referencia = referencia
        self.valorCompilado = None
        
    def ejecutar(self, ts: TablaSimbolos):
        
        var_valor = self.valor.getValor(ts)
        var_tipo = self.valor.getTipo(ts)
        
        
        if isinstance(var_valor, InstanciaStruct):
            print("STRUCT/////////////////////////////////////////////////")
            # struct = CrearInstanciaStruct(self.identificador,self.valor,self.mut,ts.env, self.linea, self.columna)
            # struct.ejecutar(ts)

            var_valor.id_instancia = self.identificador
            var_valor.mut = self.mut
            ts.add(self.identificador, var_valor, self.linea, self.columna)
            
            return

        if self.tipo is not None:
            if self.tipo.tipo != var_tipo:
                print('Semantico', f'El valor de la variable no coincide con su tipo: {self.tipo.tipo} -> {var_tipo}')
                raise Error_('Semantico', f'El valor de la variable no coincide con su tipo: { self.tipo.tipo} -> {var_tipo}', ts.env, self.linea, self.columna)
        else:
            
            self.tipo = Tipo(tipo = var_tipo)
            
        simbolo = ts.buscar(self.identificador);
        
        if simbolo is None:

            nuevo = Simbolo()
            nuevo.iniciarPrimitivo( self.identificador, self.tipo, var_valor, self.mut)
            ts.add(self.identificador, nuevo, self.linea, self.columna)
        
        else:
            if simbolo.tipo.tipo != var_tipo:
                print(f'El valor de la variable no coincide con su tipo: {simbolo.tipo.tipo} -> {var_tipo}')
                raise Error_('Semantico', f'El valor de la variable no coincide con su tipo: {simbolo.tipo.tipo} -> {var_tipo}', ts.env, self.linea, self.columna)
                
            elif simbolo.mut is False:
                print(f'No se puede cambiar el valor de una constante')
                raise Error_("Semantico", "No se puede cambiar el valor de una constante", ts.env, self.linea, self.columna)
            else:
                simbolo.valor = var_valor
                print("var: ",self.identificador, " - ", var_valor, "Tipo: " ,  self.tipo.tipo)
                
            
       
        
        
    