from models.misc.Program import Program
from models.misc.driver import Driver

class Error_(Exception):
    def __init__(self, tipo: str, mensaje: str, ambito, linea: int, columna:int):
        
        self.tipo = tipo
        self.mensaje = mensaje
        self.linea = linea
        self.columna = columna
        
        Program.errores.append({"tipo":tipo, "mensaje": mensaje, "linea": linea, "columna": columna, "ambito":ambito});
        Program.console += self.getError() + "\n"
        
    def getError(self):
        print(self.tipo + ", " + self.mensaje)
        return "Error " + self.tipo + " - " + self.mensaje + " (Linea " + str(self.linea) + "; Columna " + str(self.columna) + ")"
    