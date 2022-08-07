from models.instruccion import Instruccion


class Ast:

    def __init__(self, instrucciones=None):
        if instrucciones is None:
            instrucciones = []

        self.instrucciones = instrucciones

    def ejecutar(self, ts):
        for instruccion in self.instrucciones:
            instruccion.ejecutar(ts)