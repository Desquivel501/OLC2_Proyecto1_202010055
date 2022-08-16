from models.misc.Program import Program
from models.instruccion.Instruccion import Instruccion


class Statement(Instruccion):

    def __init__(self, codigo, linea, columna):
        self.codigo = codigo
        self.linea = linea
        self.columna = columna


    def ejecutar(self, ts):  
        element = None;
        
        for ins in self.codigo:
            try:
                element = ins.ejecutar(ts)
                
                if element is not None:
                    if element["tipo"] == "break":
                        return element
                    
                    if element["tipo"] == "continue":
                        return element

                
            except Exception as e:
                print(e)
                
        return None

    