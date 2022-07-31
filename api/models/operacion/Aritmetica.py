from models.tabla.Tipos import Tipos, definirTipo
from models.operacion.Operacion import Operador, Operacion

class Aritmetica(Operacion):
    
    def getTipo(self,driver, ts):
        return definirTipo(self.getValor(driver,ts))
    
    def getValor(self, driver, ts):
        
        valor_left = self.left.getValor(driver,ts)
        valor_right = self.right.getValor(driver,ts) 
        
        tipo_left = self.left.getTipo(driver,ts)
        tipo_right = self.right.getTipo(driver,ts) 
        
        if self.unaria is True:
            return valor_left*(-1)
        
        if self.operador == Operador.SUMA:
            if tipo_left not in [Tipos.INT, Tipos.FLOAT] and tipo_right not in [Tipos.INT, Tipos.FLOAT]:
                print(f'No se puede realizar una suma entre {Tipos(tipo_left).name} y {Tipos(tipo_right).name}')
            elif tipo_left == tipo_right:
                return valor_left + valor_right
            else:
                print(f'No se puede realizar una suma entre {Tipos(tipo_left).name} y {Tipos(tipo_right).name}')
                
        if self.operador == Operador.RESTA:
            if tipo_left not in [Tipos.INT, Tipos.FLOAT] and tipo_right not in [Tipos.INT, Tipos.FLOAT]:
                print(f'No se puede realizar una resta entre {Tipos(tipo_left).name} y {Tipos(tipo_right).name}')
            elif tipo_left == tipo_right:
                return valor_left - valor_right
            else:
                print(f'No se puede realizar una resta entre {Tipos(tipo_left).name} y {Tipos(tipo_right).name}')
                
        if self.operador == Operador.MULTI:
            if tipo_left not in [Tipos.INT, Tipos.FLOAT] and tipo_right not in [Tipos.INT, Tipos.FLOAT]:
                print(f'No se puede realizar una multiplicacion entre {Tipos(tipo_left).name} y {Tipos(tipo_right).name}')
            elif tipo_left == tipo_right:
                return valor_left * valor_right
            else:
                print(f'No se puede realizar una multiplicacion entre {Tipos(tipo_left).name} y {Tipos(tipo_right).name}')
                
        if self.operador == Operador.DIV:
            if tipo_left not in [Tipos.INT, Tipos.FLOAT] and tipo_right not in [Tipos.INT, Tipos.FLOAT]:
                print(f'No se puede realizar una division entre {Tipos(tipo_left).name} y {Tipos(tipo_right).name}')
            elif valor_right == 0:
                 print(f'La division entre 0 no esta definida')
            elif tipo_left == tipo_right:
                return valor_left / valor_right
            else:
                print(f'No se puede realizar una division entre {Tipos(tipo_left).name} y {Tipos(tipo_right).name}')
        
        if self.operador == Operador.MODULO:
            if tipo_left not in [Tipos.INT, Tipos.FLOAT] and tipo_right not in [Tipos.INT, Tipos.FLOAT]:
                print(f'No se puede calcular el modulo entre {Tipos(tipo_left).name} y {Tipos(tipo_right).name}')
            elif tipo_left == tipo_right:
                return valor_left % valor_right
            else:
                print(f'No se puede calcular el modulo entre {Tipos(tipo_left).name} y {Tipos(tipo_right).name}')
                
        if self.operador == Operador.POW:
            if tipo_left != Tipos.INT or tipo_right != Tipos.INT:
                print(f'La operacion POW solo es valida con valores INT')
            elif tipo_left == tipo_right:
                return valor_left ** valor_right
        
        if self.operador == Operador.POWF:
            if tipo_left != Tipos.FLOAT or tipo_right != Tipos.FLOAT:
                print(f'La operacion POWF solo es valida con valores FLOAT')
            elif tipo_left == tipo_right:
                return valor_left ** valor_right