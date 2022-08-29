
from models.instruccion.CrearArreglo import CrearArreglo
from models.misc.Dimension import Dimension
from models.instruccion.For import For
from models.misc.Rango import Rango
from models.instruccion.ModStruct import ModStruct
from models.expresion.AccesoStruct import AccesoStruct
from models.misc.Atributo import Atributo
from models.tabla.InstanciaStruct import InstanciaStruct
from models.instruccion.CrearInstanciaStruct import CrearInstanciaStruct
from models.misc.Campos import Campos
from models.tabla.Struct import Struct
from models.expresion.Llamada import Llamada
from models.tabla.Funcion import Funcion
from models.instruccion.Return import Return
from models.misc.Parametro import Parametro
from models.expresion.Casteo import Casteo
from models.expresion.ToString import ToString
from models.tabla.Tipos import Tipos
from models.instruccion.Print import Print_
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
    ('left', 'OR'),
    ('left', 'AND'),
    ('nonassoc', 'MAYOR','MENOR','MAYOR_I','MENOR_I', 'IGUAL','NO_IGUAL'),
    ('left', 'MENOS', 'MAS'),
    ('left', 'MULTI', 'DIV'),
    ('left', 'MODULO', 'POW_INT', 'POW_FLOAT'),
    ('left', 'PUNTO'),
    ('right', 'UMENOS'),
)

def p_ini(p):
    """
    ini : intrucciones_global
    """
    p[0] = Ast(p[1])


#----------------------------------------------------------------------------------------------------INSTRUCCIONES

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
    instruccion : asignacion PUNTOCOMA
                | if
                | match
                | while
                | loop
                | for
                | break PUNTOCOMA
                | continue PUNTOCOMA
                | return PUNTOCOMA
                | print PUNTOCOMA
                | llamada PUNTOCOMA
                | mod_struct PUNTOCOMA
                | declaracion_arreglo  PUNTOCOMA

    """
    p[0] = p[1]


def p_instruccion_no_pt(p):
    """
    instruccion_no_pt : if
                      | match
                      | print
                      | while
                      | loop
                      | break
                      | continue
                      | return
                      | llamada
                      | mod_struct
                      | asignacion
                      | for
    """
    p[0] = p[1]


def p_instrucciones_global(p):
    """
    intrucciones_global : intrucciones_global ins_global
                        | ins_global
    """
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[1].append(p[2])
        p[0] = p[1]


def p_instruccion_global(p):
    """
    ins_global : funcion
               | struct
    """
    p[0] = p[1]


#--------------------------------------------------------------------------------------------------------------------------PRINT


def p_instruccion_print(p):
    """
    print : PRINT NOT PAR_I expresion PAR_D
          | PRINT NOT PAR_I CADENA COMA exp_list PAR_D
    """

    if len(p) == 6:
         p[0] = Print_(p[4], None,p.lineno(1),p.lexpos(1))
    else:
        p[0] = Print_( Primitivo(p[4], Tipos.STR, p.lineno(1), p.lexpos(1)) , p[6],p.lineno(1),p.lexpos(1))


def p_exp_list(p):
    """
    exp_list : exp_list COMA expresion
             | expresion
    """
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[1].append(p[3])
        p[0] = p[1]


#-----------------------------------------------------------------------------------------------------------FUNCIONES

def p_funcion(p):
    """
    funcion : FN ID PAR_I lista_param PAR_D statement
            | FN ID PAR_I PAR_D statement
    """
    if len(p) == 7:
        p[0] = Funcion(p[2],p[4],p[6], Tipo(tipo = Tipos.VOID), p.lineno(1), p.lexpos(1))
    else:
        p[0] = Funcion(p[2],[],p[5], Tipo(tipo = Tipos.VOID), p.lineno(1), p.lexpos(1))


def p_funcion_tipo(p):
    """
    funcion : FN ID PAR_I lista_param PAR_D MENOS MAYOR tipo statement
            | FN ID PAR_I PAR_D MENOS MAYOR tipo statement
    """
    if len(p) == 10:
        p[0] = Funcion(p[2],p[4],p[9], p[8], p.lineno(1), p.lexpos(1))
    else:
        p[0] = Funcion(p[2],[],p[8], p[7], p.lineno(1), p.lexpos(1))


def p_lista_param(p):
    """
    lista_param : lista_param COMA ID D_PUNTO tipo
                | ID D_PUNTO tipo
    """
    if len(p) == 4:
        p[0] = [Parametro(p[1], p[3])]
    else:
        p[1].append(Parametro(p[3], p[5]))
        p[0] = p[1]


def p_return(p):
    """
    return : RETURN expresion
           | RETURN
    """
    if len(p) == 2:
        p[0] = Return(None, p.lineno(1), p.lexpos(1))
    else:
        p[0] = Return(p[2], p.lineno(1), p.lexpos(1))


def p_llamada(p):
    """
    llamada : ID PAR_I PAR_D
            | ID PAR_I exp_list PAR_D
    """
    if len(p) == 4:
        p[0] = Llamada(p[1],[],p.lineno(1), p.lexpos(1))
    else:
        p[0] = Llamada(p[1],p[3],p.lineno(1), p.lexpos(1))




#----------------------------------------------------------------------------------------------------IF


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
              | LLV_I  LLV_D
    """
    if len(p) == 3:
        p[0] = Statement(None,p.lineno(1),p.lexpos(1))
    else:
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


#--------------------------------------------------------------------------------------------------------------------------MATCH



def p_instruccion_match(p):
    """
    match : MATCH expresion LLV_I case_list LLV_D
         | MATCH expresion LLV_I case_list default LLV_D
    """
    print("match")
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
    case : exp_list_c IGUAL MAYOR statement
         | exp_list_c IGUAL MAYOR instruccion_no_pt COMA
    """
    p[0] = Case(p[1],p[4], p.lineno(1),p.lexpos(1))


def p_default(p):
    """
    default : GUION_B IGUAL MAYOR statement
            | GUION_B IGUAL MAYOR instruccion_no_pt COMA
    """
    print("default")
    p[0] = p[4]


def p_exp_list_c(p):
    """
    exp_list_c : exp_list_c BARRA expresion
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
    case_exp : exp_list_c IGUAL MAYOR expresion
             | exp_list_c IGUAL MAYOR expresion COMA
    """
    p[0] = ExpCase(p[1],p[4], p.lineno(1),p.lexpos(1))


def p_exp_default(p):
    """
    default_exp : GUION_B IGUAL MAYOR expresion COMA
    """
    p[0] = p[4]


#-----------------------------------------------------------------------------------------------------------------------------WHILE


def p_while(p):
    """
    while : WHILE expresion statement
    """
    p[0] = While(p[2],p[3],p.lineno(1),p.lexpos(1))


def p_break(p):
    """
    break : BREAK
          | BREAK expresion
    """
    if len(p) == 2 :
        p[0] = Break(None,p.lineno(1),p.lexpos(1))
    else:
        p[0] = Break(p[2], p.lineno(1),p.lexpos(1))


def p_continue(p):
    """
    continue : CONTINUE
    """
    p[0] = Continue(p.lineno(1),p.lexpos(1))


#---------------------------------------------------------------------------------------------------------------------------------LOOP


def p_loop(p):
    """
    loop : LOOP statement
    """
    p[0] = Loop(p[2], False, p.lineno(1),p.lexpos(1))


def p_loop_exp(p):
    """
    loop_exp : LOOP statement
    """
    p[0] = Loop(p[2], True, p.lineno(1),p.lexpos(1))


#---------------------------------------------------------------------------------------------------------------------------------FOR


def p_for(p):
    """
    for : FOR ID IN rango statement
    """
    p[0] = For(p[2], p[5],p.lineno(1),p.lexpos(1),rango=p[4])


def p_rango_for(p):
    """
    rango : expresion PUNTO PUNTO expresion
    """
    p[0] = Rango(p[1], p[4])




#------------------------------------------------------------------------------------------------------------------------------ASIGNACION VARIABLE


def p_asignacion(p):
    """
    asignacion : LET ID IGUAL expresion
    """
    p[0] = Asignacion(p[2], p[4], None, False, p.lineno(1),p.lexpos(1))


def p_asignacion_mut(p):
    """
    asignacion : LET MUT ID IGUAL expresion
    """
    p[0] = Asignacion(p[3], p[5], None,True, p.lineno(1),p.lexpos(1))


def p_asignacion_tipo(p):
    """
    asignacion : LET ID D_PUNTO tipo IGUAL expresion
    """
    p[0] = Asignacion(p[2], p[6], p[4], False, p.lineno(1),p.lexpos(1))


def p_asignacion_mut_tipo(p):
    """
    asignacion : LET MUT ID D_PUNTO tipo IGUAL expresion
    """
    p[0] = Asignacion(p[3],p[7], p[5],True, p.lineno(1),p.lexpos(1))


def p_re_asignacion(p):
    """
    asignacion : ID IGUAL expresion
    """
    p[0] = Asignacion( p[1], p[3], None, True,  p.lineno(1),p.lexpos(1) )



def p_tipo(p):
    """
    tipo : INT
        | FLOAT
        | BOOL
        | AMP STR
        | STRING
        | CHAR
        | VOID
        | ID

    """
    print(p[1])
    if p.slice[1].type == 'ID':
        p[0] = Tipo(tipo=Tipos.STRUCT)
    elif len(p) == 2:
        p[0] = Tipo(stipo = p[1])
    else:
        p[0] = Tipo(stipo = "&str")


#----------------------------------------------------------------------------------------------------STRUCTS

def p_struct(p):
    """
    struct : STRUCT ID LLV_I lista_campos LLV_D
    """
    p[0] = Struct(p[2],p[4],p.lineno(1), p.lexpos(1))

def p_lista_campos(p):
    """
    lista_campos : lista_campos COMA campo
                 | campo
    """
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[1].append(p[3])
        p[0] = p[1]


def p_campo(p):
    """
    campo : ID D_PUNTO tipo
    """
    if p.slice[3].type == 'ID':
        p[0] = Campos(p[1], Tipo(tipo=Tipos.STRUCT))
    else:
        p[0] = Campos(p[1], p[3])


def p_instancia(p):
    """
    instancia : ID LLV_I lista_atributo LLV_D
    """
    print("instancia")
    p[0] = InstanciaStruct(p[1],p[3],p.lineno(1), p.lexpos(1))

def p_lista_atributo(p):
    """
    lista_atributo : lista_atributo COMA ID D_PUNTO expresion
                   | ID D_PUNTO expresion
    """
    if len(p) == 4:
        p[0] = [Atributo(p[1],p[3])]
    else:
        p[1].append(Atributo(p[3],p[5]))
        p[0] = p[1]


#----------------------------------------------------------------------------------------------------ARREGLOS

def p_arreglo(p):
    """
    declaracion_arreglo : LET ID D_PUNTO dimensiones_arreglo IGUAL datos_arreglo
    """
    lista = p[4].lista
    tipo = p[4].tipo
    p[0] = CrearArreglo(p[2],lista,tipo,p[6],p.lineno(1), p.lexpos(1))


def p_dimension_arreglo(p):
    """
    dimensiones_arreglo : COR_I dimensiones_arreglo PUNTOCOMA expresion COR_D
                        | COR_I tipo PUNTOCOMA expresion COR_D

    """
    if p[2].type == 'tipo':
        p[0] = Dimension(p[2], p[4])
    else:
        p[2].lista.append(p[4])
        p[0] = p[2]


# def p_dimension_arreglo_corte(p):
#     """
#     dimensiones_arreglo :
#     """
#     print(p[4])




def p_datos_arreglo(p):
    """
    datos_arreglo : COR_I exp_list  COR_D
    """
    p[0] = p[2]


def p_dato_arreglo_exp(p):
    """
    expresion : datos_arreglo
    """
    p[0] = p[1]


#------------------------------------------------------------------------------------------------------------------------------EXPRESIONES


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


def p_expresion_ex(p):
    """
    expresion : INT D_PUNTO D_PUNTO POW_INT PAR_I expresion COMA expresion PAR_D
              | FLOAT D_PUNTO D_PUNTO POW_FLOAT PAR_I expresion COMA expresion PAR_D
              | expresion PUNTO ABS PAR_I  PAR_D
              | expresion PUNTO SQRT PAR_I  PAR_D
    """

    if p[4] == "pow":
        p[0] = Aritmetica(p[6], 'pow', p[8], p.lineno(1), p.lexpos(1), False)
    elif p[4] == "powf":
        p[0] = Aritmetica(p[6], 'powf', p[8], p.lineno(1), p.lexpos(1), False)

    elif p[3] == "abs":
        p[0] = Aritmetica(p[1], 'abs', p[1], p.lineno(1), p.lexpos(1), False)
    elif p[3] == "sqrt":
        p[0] = Aritmetica(p[1], 'sqrt', p[1], p.lineno(1), p.lexpos(1), False)


def p_expresion_relacional(p):
    """
    expresion : expresion MAYOR expresion
              | expresion MENOR expresion
              | expresion MAYOR_I expresion
              | expresion MENOR_I expresion
              | expresion D_IGUAL expresion
              | expresion NO_IGUAL expresion
    """
    print("here r")
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


def p_expresion_numero(p):
    """
    expresion : ENTERO
              | DECIMAL
    """
    print(p.slice[1].type)
    p[0] = Primitivo(p[1], None, p.lineno(1), p.lexpos(1))


def p_expresion_bool(p):
    """
    expresion : TRUE
              | FALSE
    """

    val = True if p[1] == 'true' else False
    p[0] = Primitivo(val, Tipos.BOOLEAN, p.lineno(1), p.lexpos(1))


def p_expresion_char(p):
    """
    expresion : CHAR_S
    """
    p[0] = Primitivo(p[1], Tipos.CHAR, p.lineno(1), p.lexpos(1))


def p_expresion_str(p):
    """
    expresion : CADENA
    """
    p[0] = Primitivo(p[1], Tipos.STR, p.lineno(1), p.lexpos(1))


def p_expresion_id(p):
    """
    expresion : ID
    """
    print("ID")
    p[0] = Identificador(p[1], p.lineno(1), p.lexpos(1))



def p_to_string(p):
    """
    expresion : expresion PUNTO TO_STRING PAR_I PAR_D
    """
    p[0] = ToString(p[1], p.lineno(1), p.lexpos(1))



 #-------------------------------------------------------------------------ACCESO STRUCT

def p_mod_struct(p):
    """
    mod_struct : acceso_struct IGUAL expresion
    """
    p[0] = ModStruct(p[1],p[3],p.lineno(1), p.lexpos(1))


def p_acceso_struct_exp(p):
    """
    acceso_struct_exp : acceso_struct
    """
    p[0] = AccesoStruct(p[1],p.lineno(1), p.lexpos(1))



def p_acceso_struct(p):
    """
    acceso_struct : acceso_struct PUNTO expresion
    """
    p[1].append(p[3])
    p[0] = p[1]


def p_acceso_corte(p):
    """
    acceso_struct  : expresion PUNTO expresion
    """
    lista = [p[1]]
    lista.append(p[3])
    p[0] = lista

#-------------------------------------------------------------------------

def p_cast(p):
    """
    expresion : expresion AS tipo
    """
    p[0] = Casteo(p[3],p[1], p.lineno(1), p.lexpos(1))




def p_expresion_sentencia(p):
    """
    expresion : exp_if
              | match_exp
              | loop_exp
              | llamada
    """
    p[0] = p[1]


def p_otras_expresiones(p):
    """
    expresion : instancia
              | acceso_struct_exp
    """
    p[0] = p[1]



# Error sintactico
def p_error(p):
    print(f'Error de sintaxis {p.value!r}, linea {p.lineno}')
    raise Error_("Sintactivo", f'Error de sintaxis {p.value!r}',p.lineno,0)


    # while True:
    #      tok = parser.token()
    #      if not tok or tok.type == 'SEMI': break
    # parser.errok()

    # return tok



# Build the parser
parser = yacc()