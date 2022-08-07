
from ply.yacc import yacc
from analizador import lexer

from models.expresion.Identificador import Identificador
from models.instruccion.Asignacion import Asignacion
from models.tabla.Simbolo import Simbolo, Simbolos
from models.expresion.operacion.Relacional import Relacional
from models.expresion.operacion.Logica import Logica
from models.ast.ast import Ast
from models.instruccion.Ejecutar import Ejecutar
from models.expresion.operacion.Aritmetica import Aritmetica
from models.expresion.Primitivo import Primitivo
from models.tabla.Tipos import Tipo

tokens = lexer.tokens

precedence = (
    ('left', 'AND', 'OR','NOT'),
    ('left', 'MAYOR','MENOR','MAYOR_I','MENOR_I', 'IGUAL','NO_IGUAL'),
    ('left', 'MENOS', 'MAS'),
    ('left', 'MULTI', 'DIV'),
    ('left', 'MODULO', 'POW_INT', 'POW_FLOAT'),
    ('right', 'UMENOS'),
)

def p_ini(p):
    """
    ini : instrucciones
    """
    p[0] = Ast(p[1])
    
    
def p_instrucciones(p):
    """
    instrucciones : instrucciones instruccion PUNTOCOMA						
    """
    p[1].append(p[2])
    p[0] = p[1]
    
    
def p_instrucciones_instruccion(p):
    """
    instrucciones : instruccion PUNTOCOMA						
    """
    p[0] = [p[1]]
    
def p_instruccion(p):
    """
    instruccion : ejecutar
                | asignacion
    """
    p[0] = p[1]
    
    
def p_instruccion_ejecutar(p):
    """
    ejecutar : EJECUTAR PAR_I expresion PAR_D			
    """
    p[0] = Ejecutar(p[3], p.lineno(1),p.lexpos(1))
    
    
def p_asignacion(p):
    """
    asignacion : LET ID D_PUNTO tipo IGUAL expresion
    """
    p[0] = Asignacion(p[2], Simbolo(Simbolos.VARIABLE, p[4], p[2], p[6], False), p[4], False, p.lineno(1),p.lexpos(1))
                      
def p_asignacion_mut(p):
    """
    asignacion : LET MUT ID D_PUNTO tipo IGUAL expresion
    """
    p[0] = Asignacion(p[3],  Simbolo(Simbolos.VARIABLE, p[5], p[3], p[7], True), p[5],True, p.lineno(1),p.lexpos(1))

def p_tipo(p):
    """
    tipo : INT
        | FLOAT
        | BOOL
    """
    p[0] = Tipo(p[1])
      

def p_expresion_aritmetica(p):
    """
    expresion : expresion MAS expresion
               | expresion MENOS expresion
               | expresion MULTI expresion
               | expresion DIV expresion
               | expresion MODULO expresion
    """
    p[0] = Aritmetica(p[1], p[2], p[3], p.lineno(1), p.lexpos(1), False)
    
    
def p_expresion_unario_ar(p):
    """
    expresion : MENOS expresion %prec UMENOS
    """
    p[0] = Aritmetica(p[2], p[1], p[2], p.lineno(1), p.lexpos(1), True)
    
    
def p_expresion_pow(p):
    """
    expresion : INT D_PUNTO D_PUNTO POW_INT PAR_I expresion COMA expresion PAR_D
              | FLOAT D_PUNTO D_PUNTO POW_FLOAT PAR_I expresion COMA expresion PAR_D
    """
    if p[4] == "pow":
        p[0] = Aritmetica(p[6], 'pow', p[8], p.lineno(1), p.lexpos(1), False)
    else:
        p[0] = Aritmetica(p[6], 'powf', p[8], p.lineno(1), p.lexpos(1), False)


def p_expresion_numero(p):
    """
    expresion : ENTERO 
              | DECIMAL
    """
    p[0] = Primitivo(p[1], p.lineno(1), p.lexpos(1))
    
    
def p_expresion_bool(p):
    """
    expresion : TRUE 
              | FALSE
    """
    
    val = True if p[1] == 'true' else False
    p[0] = Primitivo(val, p.lineno(1), p.lexpos(1))
    

def p_expresion_id(p):
    """
    expresion : ID
    """
    p[0] = Identificador(p[1], p.lineno(1), p.lexpos(1))

def p_expresion_relacional(p):
    """
    expresion : expresion MAYOR expresion
              | expresion MENOR expresion
              | expresion MAYOR_I expresion
              | expresion MENOR_I expresion
              | expresion D_IGUAL expresion
              | expresion NO_IGUAL expresion
    """
    p[0] = Relacional(p[1], p[2], p[3], p.lineno(1), p.lexpos(1), False)
    
    
def p_expresion_logica(p):
    """
    expresion : expresion OR expresion
              | expresion AND expresion
    """
    p[0] = Logica(p[1], p[2], p[3], p.lineno(1), p.lexpos(1), False)
    
    
def p_expresion_unario_lo(p):
    """
    expresion : NOT expresion
    """
    p[0] = Logica(p[2], p[1], p[2], p.lineno(1), p.lexpos(1), True)
    

def p_factor_agrupacion(p):
    """
    expresion : PAR_I expresion PAR_D
    """
    p[0] = p[2]


# Error sintactico
def p_error(p):
    print(f'Error de sintaxis {p.value!r}')


# Build the parser
parser = yacc()