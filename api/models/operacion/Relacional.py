from models.tabla.Tipos import Tipos, definirTipo
from models.operacion.Operacion import Operador, Operacion

class Relacional(Operacion):
    
    def getTipo(self,driver, ts):
        return definirTipo(self.getValor(driver,ts))
    
    def getValor(self, driver, ts):
        valor_left = self.left.getValor(driver,ts)
        valor_right = self.right.getValor(driver,ts)