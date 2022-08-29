from models.misc.Program import Program
from models.instruccion.Instruccion import Instruccion


class Statement(Instruccion):

    def __init__(self, codigo, linea, columna):
        self.codigo = codigo
        self.linea = linea
        self.columna = columna


    def ejecutar(self, ts):  
        element = None;
        
        if self.codigo is None:
            return None
        
        # for ins in self.codigo:
        #     try:
        #         element = ins.ejecutar(ts)
                
        #         if element is not None:
        #             if element["tipo"] == "break" and tipo != "funcion":
        #                 return element
                    
        #             if element["tipo"] == "continue" and tipo != "funcion":
        #                 return element
                    
        #             if element["tipo"] == "return":
        #                 return element

                
        #     except Exception as e:
        #         print(e)
        
        for ins in self.codigo:
            element = ins.ejecutar(ts)
                    
            if element is not None:
                if element["tipo"] == "break":
                    return element
                        
                if element["tipo"] == "continue":
                    return element
                        
                if element["tipo"] == "return":
                    return element
                
        return None

    