

import copy
from struct import Struct
from models.tabla.Simbolo import Simbolo
from models.misc.error import Error_
from models.instruccion.Instruccion import Instruccion
from models.tabla.Tipos import Tipo, Tipos
from models.expresion.Expresion import Expresion


class InstanciaStruct(Expresion, Simbolo):
    def __init__(self, id_struct, lista_atributos, linea, columna):
        self.id_struct = id_struct
        self.lista_atributos = lista_atributos
        self.id_instancia = None
        self.mut = None
        self.linea = linea
        self.columna = columna
        self.dic_atributos = {}
        self.compilada = False
        
    def getTipo(self, ts):
        return Tipos.STRUCT
    
    def getValor(self, ts):
        
        copiaLista = copy.deepcopy(self.lista_atributos)

        struct:Struct = ts.obtenerStruct(self.id_struct)
        
        if struct is None:
            raise Error_("Semantico", f'Struct {self.id_struct } no ha sido declarado', self.linea, self.columna)
        
        
        for campo in struct.campos:
            if len(self.lista_atributos) == 0:
                print("es 0")
                raise Error_("Semantico", f'Numero incorrecto de atributos', self.linea, self.columna)
            
            atributo = self.lista_atributos[0]
            
            if campo.identificador == atributo.identificador:

                valor = atributo.valor.getValor(ts)
                tipo = atributo.valor.getTipo(ts)
                
                if tipo == campo.tipo.tipo:
                    
                    # print(campo.identificador, " - ", valor)
                    atributo.tipo = tipo
                    atributo.valor = valor
                    self.dic_atributos[campo.identificador] = atributo
                else:
                    raise Error_("Semantico", f'Tipo incorrecto en atributo \'{campo.identificador}\'', self.linea, self.columna)
            else:
                raise Error_("Semantico", f'Atributo \'{campo.identificador}\' no existe', self.linea, self.columna)
            
            self.lista_atributos.pop(0)

        self.lista_atributos = copiaLista
       
        return self


    