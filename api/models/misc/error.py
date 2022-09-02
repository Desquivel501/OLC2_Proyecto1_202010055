from models.misc.Program import Program
from models.misc.driver import Driver
from datetime import datetime

class Error_(Exception):
    def __init__(self, tipo: str, mensaje: str, ambito, linea: int, columna:int):
        
        date = datetime.now()
        dt_string = date.strftime("%d/%m/%Y %H:%M")
        
        
        self.tipo = tipo
        self.mensaje = mensaje
        self.linea = linea
        self.columna = columna
        
        
        Program.errores.append({"tipo":tipo, "mensaje": mensaje, "linea": linea, "columna": columna, "ambito":ambito, "fecha": dt_string});
        Program.console += self.getError() + "\n"
        
    def getError(self):
        print(self.tipo + ", " + self.mensaje)
        return "Error " + self.tipo + " - " + self.mensaje + " (Linea " + str(self.linea) + "; Columna " + str(self.columna) + ")"
    