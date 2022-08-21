from cmath import sqrt
from models.misc.error import Error_
from models.tabla.Tipos import Tipos, definirTipo
from models.expresion.operacion.Operacion import Operador, Operacion

class Aritmetica(Operacion):
    
    def getTipo(self, ts):
        return definirTipo(self.getValor(ts))
    
    def getValor(self, ts):
        
        valor_left = self.left.getValor(ts)
        valor_right = self.right.getValor(ts) 
        
        tipo_left = self.left.getTipo(ts)
        tipo_right = self.right.getTipo(ts) 
        
        if self.unaria is True:
            return valor_left*(-1)
            
        
        if self.operador == Operador.POW:
            if tipo_left != Tipos.INT or tipo_right != Tipos.INT:
                print(f'La operacion POW solo es valida con valores INT')
                raise Error_("Semantico",f'La operacion POW solo es valida con valores INT',self.linea,self.columna)
            elif tipo_left == tipo_right:
                return valor_left ** valor_right
        
        if self.operador == Operador.POWF:
            if tipo_left != Tipos.FLOAT or tipo_right != Tipos.FLOAT:
                print(f'La operacion POWF solo es valida con valores FLOAT')
                raise Error_("Semantico",f'La operacion POWF solo es valida con valores FLOAT',self.linea,self.columna)
            elif tipo_left == tipo_right:
                return valor_left ** valor_right
            
        
        
        if self.operador == Operador.SUMA and tipo_left in [Tipos.STRING, Tipos.STR] and tipo_right in [Tipos.STR, Tipos.STRING] :
            if tipo_left == Tipos.STR and tipo_right == Tipos.STRING:
                return valor_left + valor_right
            else:
                print(f'No se puede realizar una suma entre {Tipos(tipo_left).name} y {Tipos(tipo_right).name}')
                raise Error_("Semantico",f'No se puede realizar una suma entre {Tipos(tipo_left).name} y {Tipos(tipo_right).name}',self.linea,self.columna)
            
        
        
        if tipo_left not in [Tipos.INT, Tipos.FLOAT] and tipo_right not in [Tipos.INT, Tipos.FLOAT]:
            print(f'No se puede realizar una operacion entre {Tipos(tipo_left).name} y {Tipos(tipo_right).name}')
            raise Error_("Semantico",f'No se puede realizar una operacion entre {Tipos(tipo_left).name} y {Tipos(tipo_right).name}',self.linea,self.columna)
        
        if self.operador == Operador.SUMA:
            if tipo_left == tipo_right:
                return valor_left + valor_right
            else:
                print(f'No se puede realizar una suma entre {Tipos(tipo_left).name} y {Tipos(tipo_right).name}')
                raise Error_("Semantico",f'No se puede realizar una suma entre {Tipos(tipo_left).name} y {Tipos(tipo_right).name}',self.linea,self.columna)
                
        if self.operador == Operador.RESTA:
            if tipo_left == tipo_right:
                return valor_left - valor_right
            else:
                print(f'No se puede realizar una resta entre {Tipos(tipo_left).name} y {Tipos(tipo_right).name}')
                raise Error_("Semantico",f'No se puede realizar una resta entre {Tipos(tipo_left).name} y {Tipos(tipo_right).name}',self.linea,self.columna)
                
        if self.operador == Operador.MULTI:
            if tipo_left == tipo_right:
                return valor_left * valor_right
            else:
                print(f'No se puede realizar una multiplicacion entre {Tipos(tipo_left).name} y {Tipos(tipo_right).name}')
                raise Error_("Semantico",f'No se puede realizar una multiplicacion entre {Tipos(tipo_left).name} y {Tipos(tipo_right).name}',self.linea,self.columna)
                
        if self.operador == Operador.DIV:
            if valor_right == 0:
                 print(f'La division entre 0 no esta definida')
                 raise Error_("Semantico",f'La division entre 0 no esta definida',self.linea,self.columna)
            elif tipo_left == tipo_right:
                return valor_left / valor_right
            else:
                print(f'No se puede realizar una division entre {Tipos(tipo_left).name} y {Tipos(tipo_right).name}')
                raise Error_("Semantico",f'No se puede realizar una division entre {Tipos(tipo_left).name} y {Tipos(tipo_right).name}',self.linea,self.columna)
        
        if self.operador == Operador.MODULO:
            if tipo_left == tipo_right:
                return valor_left % valor_right
            else:
                print(f'No se puede calcular el modulo entre {Tipos(tipo_left).name} y {Tipos(tipo_right).name}')
                raise Error_("Semantico",f'No se puede calcular el modulo entre {Tipos(tipo_left).name} y {Tipos(tipo_right).name}',self.linea,self.columna)
             
                
        if self.operador == Operador.ABS:
            return abs(valor_left)
        
        if self.operador == Operador.SQRT:
            if valor_left < 0:
                raise Error_("Semantico",f'La raiz cuadrada de negativos no esta definida',self.linea,self.columna)
            else:
                return valor_left ** 0.5