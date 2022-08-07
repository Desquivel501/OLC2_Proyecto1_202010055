from models.misc.error import Error_
from models.tabla.Tipos import Tipos, definirTipo
from models.expresion.operacion.Operacion import Operador, Operacion

class Relacional(Operacion):
    
    def getTipo(self, ts):
        return definirTipo(self.getValor(ts))
    
    def getValor(self, ts):
        valor_left = self.left.getValor(ts)
        valor_right = self.right.getValor(ts)
        
        tipo_left = self.left.getTipo(ts)
        tipo_right = self.right.getTipo(ts) 
        
        
        if tipo_left not in [Tipos.INT, Tipos.FLOAT, Tipos.BOOLEAN] and tipo_right not in [Tipos.INT, Tipos.FLOAT,Tipos.BOOLEAN]:
                print(f'No se puede realizar operacion "{self.getOperacion(self.operador)}" entre {Tipos(tipo_left).name} y {Tipos(tipo_right).name}')
                raise Error_("Semantico",f'No se puede realizar operacion "{self.getOperacion(self.operador)}" entre {Tipos(tipo_left).name} y {Tipos(tipo_right).name}',self.linea,self.columna)
                

        if self.operador == Operador.IGUAL:
            if tipo_left == tipo_right:
                return valor_left == valor_right
            else:
                print(f'No se puede realizar operacion "{self.getOperacion(self.operador)}" entre {Tipos(tipo_left).name} y {Tipos(tipo_right).name}')
                raise Error_("Semantico",f'No se puede realizar operacion "{self.getOperacion(self.operador)}" entre {Tipos(tipo_left).name} y {Tipos(tipo_right).name}',self.linea,self.columna)
                
                
        if self.operador == Operador.NO_IGUAL:
            if tipo_left == tipo_right:
                return valor_left != valor_right
            else:
                print(f'No se puede realizar operacion "{self.getOperacion(self.operador)}" entre {Tipos(tipo_left).name} y {Tipos(tipo_right).name}')
                raise Error_("Semantico",f'No se puede realizar operacion "{self.getOperacion(self.operador)}" entre {Tipos(tipo_left).name} y {Tipos(tipo_right).name}',self.linea,self.columna)
                
                
        #------------------------------------------------------------------------------------------------------------------------------------------------------------------
        #------------------------------------------------------------------------------------------------------------------------------------------------------------------
                
        
        if tipo_left not in [Tipos.INT, Tipos.FLOAT] and tipo_right not in [Tipos.INT, Tipos.FLOAT]:
                print(f'No se puede realizar operacion "{self.getOperacion(self.operador)}" entre {Tipos(tipo_left).name} y {Tipos(tipo_right).name}')
                raise Error_("Semantico",f'No se puede realizar operacion "{self.getOperacion(self.operador)}" entre {Tipos(tipo_left).name} y {Tipos(tipo_right).name}',self.linea,self.columna)
                
        
        if self.operador == Operador.MAYOR:
            if tipo_left == tipo_right:
                return valor_left > valor_right
            else:
                print(f'No se puede realizar operacion "{self.getOperacion(self.operador)}" entre {Tipos(tipo_left).name} y {Tipos(tipo_right).name}')
                raise Error_("Semantico",f'No se puede realizar operacion "{self.getOperacion(self.operador)}" entre {Tipos(tipo_left).name} y {Tipos(tipo_right).name}',self.linea,self.columna)
                
                
        if self.operador == Operador.MENOR:
            if tipo_left == tipo_right:
                return valor_left < valor_right
            else:
                print(f'No se puede realizar operacion "{self.getOperacion(self.operador)}" entre {Tipos(tipo_left).name} y {Tipos(tipo_right).name}')
                raise Error_("Semantico",f'No se puede realizar operacion "{self.getOperacion(self.operador)}" entre {Tipos(tipo_left).name} y {Tipos(tipo_right).name}',self.linea,self.columna)
                
                
        if self.operador == Operador.MAYOR_I:
            if tipo_left == tipo_right:
                return valor_left >= valor_right
            else:
                print(f'No se puede realizar operacion "{self.getOperacion(self.operador)}" entre {Tipos(tipo_left).name} y {Tipos(tipo_right).name}')
                raise Error_("Semantico",f'No se puede realizar operacion "{self.getOperacion(self.operador)}" entre {Tipos(tipo_left).name} y {Tipos(tipo_right).name}',self.linea,self.columna)
                

        if self.operador == Operador.MENOR_I:
            if tipo_left == tipo_right:
                return valor_left <= valor_right
            else:
                print(f'No se puede realizar operacion "{self.getOperacion(self.operador)}" entre {Tipos(tipo_left).name} y {Tipos(tipo_right).name}')
                raise Error_("Semantico",f'No se puede realizar operacion "{self.getOperacion(self.operador)}" entre {Tipos(tipo_left).name} y {Tipos(tipo_right).name}',self.linea,self.columna)
               
                
    def getOperacion(op:Operador):
        if op == Operador.IGUAL:
            return "Igualacion"
        if op == Operador.NO_IGUAL:
            return "Distinto"
        if op == Operador.MAYOR:
            return "Mayor que"
        if op == Operador.MAYOR_I:
            return "Mayor o igual que"
        if op == Operador.MENOR:
            return "Menor que"
        if op == Operador.MENOR_I:
            return "Menor o igual que"
    