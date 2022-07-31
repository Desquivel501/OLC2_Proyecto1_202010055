
from ply.yacc import yacc
from analizador import lexer
from models.ast.ast import Ast
from models.instruccion.Ejecutar import Ejecutar
from models.operacion.Aritmetica import Aritmetica
from models.expresion.Primitivo import Primitivo

tokens = lexer.tokens

precedence = (
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
    p[0] = p[1].append(p[2])
    
    
def p_instrucciones_instruccion(p):
    """
    instrucciones : instruccion PUNTOCOMA						
    """
    p[0] = [p[1]]
    
    
def p_instruccion_ejecutar(p):
    """
    instruccion : EJECUTAR PAR_I expresion PAR_D			
    """
    p[0] = Ejecutar(p[3], p.lineno(1),p.lexpos(1))


def p_expresion_aritmetica(p):
    """
    expresion : expresion MAS expresion
               | expresion MENOS expresion
               | expresion MULTI expresion
               | expresion DIV expresion
               | expresion MODULO expresion
    """
    p[0] = Aritmetica(p[1], p[2], p[3], p.lineno(1), p.lexpos(1), False)
    
    
def p_expresion_unario(p):
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
    print(type(p[1]))
    p[0] = Primitivo(p[1], p.lineno(1), p.lexpos(1))
    
    
def p_expresion_bool(p):
    """
    expresion : TRUE 
              | FALSE
    """
    
    val = True if p[1] == 'true' else False
    print("res: ", val)
    p[0] = Primitivo(val, p.lineno(1), p.lexpos(1))

# def p_expresion_relacional(p):
#     """
#     expresion : expresion MAS expresion
#                | expresion MENOS expresion
#                | expresion MULTI expresion
#                | expresion DIV expresion
#                | expresion MODULO expresion
#     """
#     p[0] = Aritmetica(p[1], p[2], p[3], p.lineno(1), p.lexpos(1), False)

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