
from models.instruccion.Continue import Continue
from models.instruccion.Loop import Loop
from models.instruccion.Break import Break
from models.instruccion.While import While
from models.misc.error import Error_
from models.instruccion.Match import Match
from models.instruccion.Case import Case
from models.expresion.ExpMatch import ExpMatch
from models.expresion.ExpIF import ExpIf
from models.expresion.ExpCase import ExpCase
from ply.yacc import yacc
from analizador import lexer
from models.instruccion.Statement import Statement
from models.instruccion.If import If

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
    instrucciones : instrucciones instruccion 						
    """
    p[1].append(p[2])
    p[0] = p[1]
    
    
def p_instrucciones_instruccion(p):
    """
    instrucciones : instruccion 						
    """
    p[0] = [p[1]]
    
def p_instruccion(p):
    """
    instruccion : ejecutar PUNTOCOMA
                | asignacion PUNTOCOMA
                | if
                | match
                | while 
                | loop
                | break
                | continue
    """
    p[0] = p[1]
    
    
def p_instruccion_no_pt(p):
    """
    instruccion_no_pt : ejecutar 
                      | asignacion
                      | if
                      | match
    """
    p[0] = p[1]
    
    
#--------------------------------------------------------------------------------------------------------------------------------------- 
#----------------------------------------------------------------------------------------------------------------------------------------  
    
    
def p_instruccion_ejecutar(p):
    """
    ejecutar : EJECUTAR PAR_I expresion PAR_D			
    """
    p[0] = Ejecutar(p[3], p.lineno(1),p.lexpos(1))
    
    
#--------------------------------------------------------------------------------------------------------------------------------------   
    
    
def p_instruccion_if(p):
    """
    if : IF expresion statement
    """
    p[0] = If(p[2], p[3], None, p.lineno(1), p.lexpos(1))
        

def p_instruccion_if_else(p):
    """
    if : IF expresion statement else
    """
    p[0] = If(p[2], p[3], p[4], p.lineno(1), p.lexpos(1))
    
    
def p_instruccion_else(p):
    """
    else : ELSE statement
         | ELSE if
    """
    p[0] = p[2]
    
    
def p_statement(p):
    """
    statement : LLV_I instrucciones LLV_D 
    """
    p[0] = Statement(p[2],p.lineno(1),p.lexpos(1))
    

def p_expresion_if_else(p):
    """
    exp_if : IF expresion LLV_I expresion LLV_D exp_else
    """
    p[0] = ExpIf(p[2],p[4],p[6],p.lineno(1),p.lexpos(1))
    
    
def p_expresion_else(p):
    """
    exp_else : ELSE LLV_I expresion LLV_D
             | ELSE exp_if
    """
    if p[2] == '{':
        p[0] = p[3]
    else:
        p[0] = p[2]
        

#---------------------------------------------------------------------------------------------------------------------------------------  
#----------------------------------------------------------------------------------------------------------------------------------------
        

def p_instruccion_match(p):
    """
    match : MATCH expresion LLV_I case_list LLV_D
         | MATCH expresion LLV_I case_list default LLV_D
    """
    if len(p) == 6:
        p[0] = Match(p[2],p[4],None,p.lineno(1),p.lexpos(1))
    else:
        p[0] = Match(p[2],p[4],p[5],p.lineno(1),p.lexpos(1))
    
    
def p_case_list(p):
    """
    case_list : case_list case
              | case 
    """
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[1].append(p[2])
        p[0] = p[1]
    
    
def p_case(p):
    """
    case : exp_list IGUAL MAYOR statement
         | exp_list IGUAL MAYOR instruccion_no_pt COMA
    """
    p[0] = Case(p[1],p[4], p.lineno(1),p.lexpos(1))
    
    
def p_default(p):
    """
    default : GUION_B IGUAL MAYOR statement
            | GUION_B IGUAL MAYOR instruccion
    """
    print("default")
    p[0] = p[4]
    
    
def p_exp_list(p):
    """
    exp_list : exp_list BARRA expresion
             | expresion
    """
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[1].append(p[3])
        p[0] = p[1]
        
        
def p_exp_match(p):
    """
    match_exp : MATCH expresion LLV_I case_list_exp LLV_D
              | MATCH expresion LLV_I case_list_exp default_exp LLV_D
    """
    print("match")
    if len(p) == 6:
        p[0] = ExpMatch(p[2],p[4],None,p.lineno(1),p.lexpos(1))
    else:
        p[0] = ExpMatch(p[2],p[4],p[5],p.lineno(1),p.lexpos(1))
    
    
def p_exp_case_list(p):
    """
    case_list_exp : case_list_exp case_exp
                  | case_exp 
    """
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[1].append(p[2])
        p[0] = p[1]
    
    
def p_exp_case(p):
    """
    case_exp : exp_list IGUAL MAYOR expresion
             | exp_list IGUAL MAYOR expresion COMA
    """
    p[0] = ExpCase(p[1],p[4], p.lineno(1),p.lexpos(1))
    
    
def p_exp_default(p):
    """
    default_exp : GUION_B IGUAL MAYOR expresion
    """
    p[0] = p[4]
    
    
#---------------------------------------------------------------------------------------------------------------------------------------  
#----------------------------------------------------------------------------------------------------------------------------------------
    
    
def p_while(p):
    """
    while : WHILE expresion statement
    """
    p[0] = While(p[2],p[3],p.lineno(1),p.lexpos(1))
    

def p_break(p):
    """
    break : BREAK PUNTOCOMA
          | BREAK expresion PUNTOCOMA
    """
    if len(p) == 3 :
        p[0] = Break(None,p.lineno(1),p.lexpos(1))
    else:
        p[0] = Break(p[2], p.lineno(1),p.lexpos(1))
        
        
def p_continue(p):
    """
    continue : CONTINUE PUNTOCOMA
    """
    p[0] = Continue(p.lineno(1),p.lexpos(1))
    
    
#---------------------------------------------------------------------------------------------------------------------------------------  
#----------------------------------------------------------------------------------------------------------------------------------------


def p_loop(p):
    """
    loop : LOOP statement
    """
    p[0] = Loop(p[2], False, p.lineno(1),p.lexpos(1))
    

def p_loop_exp(p):
    """
    loop_exp : LOOP statement
    """
    p[0] = Loop(p[2], False, p.lineno(1),p.lexpos(1))
    
    
    
#---------------------------------------------------------------------------------------------------------------------------------------  
#----------------------------------------------------------------------------------------------------------------------------------------


    
def p_asignacion(p):
    """
    asignacion : LET ID IGUAL expresion
    """
    p[0] = Asignacion(p[2], Simbolo(Simbolos.VARIABLE, None, p[2], p[4], False), None, False, p.lineno(1),p.lexpos(1))
                
                      
def p_asignacion_mut(p):
    """
    asignacion : LET MUT ID IGUAL expresion
    """
    p[0] = Asignacion(p[3],  Simbolo(Simbolos.VARIABLE, None, p[3], p[5], True), None,True, p.lineno(1),p.lexpos(1))


def p_asignacion_tipo(p):
    """
    asignacion : LET ID D_PUNTO tipo IGUAL expresion
    """
    p[0] = Asignacion(p[2], Simbolo(Simbolos.VARIABLE, p[4], p[2], p[6], False), p[4], False, p.lineno(1),p.lexpos(1))
          
                      
def p_asignacion_mut_tipo(p):
    """
    asignacion : LET MUT ID D_PUNTO tipo IGUAL expresion
    """
    p[0] = Asignacion(p[3],  Simbolo(Simbolos.VARIABLE, p[5], p[3], p[7], True), p[5],True, p.lineno(1),p.lexpos(1))
  

def p_re_asignacion(p):
    """
    asignacion : ID IGUAL expresion
    """
    p[0] = Asignacion( p[1], Simbolo(Simbolos.VARIABLE, None, p[1], p[3], True), None, True,  p.lineno(1),p.lexpos(1) )
   


def p_tipo(p):
    """
    tipo : INT
        | FLOAT
        | BOOL
    """
    p[0] = Tipo(p[1])
    

#---------------------------------------------------------------------------------------------------------------------------------------  
#----------------------------------------------------------------------------------------------------------------------------------------
      

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
              | ABS PAR_I expresion PAR_D
              | SQRT PAR_I expresion PAR_D
    """
    
    if p[4] == "pow":
        p[0] = Aritmetica(p[6], 'pow', p[8], p.lineno(1), p.lexpos(1), False)
    elif p[4] == "powf":
        p[0] = Aritmetica(p[6], 'powf', p[8], p.lineno(1), p.lexpos(1), False)
    elif p[1] == "abs":
        p[0] = Aritmetica(p[3], 'abs', p[3], p.lineno(1), p.lexpos(1), False)
    elif p[1] == "sqrt":
        p[0] = Aritmetica(p[3], 'sqrt', p[3], p.lineno(1), p.lexpos(1), False)
    


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
    
def p_expresion_sentencia(p):
    """
    expresion : exp_if
              | match_exp
    """
    p[0] = p[1]



# Error sintactico
def p_error(p):
    print(f'Error de sintaxis {p.value!r}')
    Error_("Sintactivo", f'Error de sintaxis {p.value!r}', p.lineno(1), p.lexpos(1))


# Build the parser
parser = yacc()