from re import L
from models.misc.Program import Program
from models.misc.error import Error_
from ply import lex

reservadas = {
    'true': 'TRUE',
    'false':'FALSE',
    'pow':'POW_INT',
    'powf':'POW_FLOAT',
    'i64':'INT',
    'f64':'FLOAT',
    'mut':'MUT',
    'let':'LET',
    'if':'IF',
    'else':'ELSE',
    'bool':'BOOL',
    'String':'STRING',
    'str':'STR',
    'char':'CHAR',
    'println':'PRINT',
    'abs':"ABS",
    'sqrt':'SQRT', 
    'to_string':'TO_STRING',
    'match':'MATCH',
    'while':'WHILE',
    'break':'BREAK',
    'continue':'CONTINUE',
    'loop':'LOOP',
    'as':'AS',
    'fn': 'FN',
    'return': 'RETURN',
    'void':'VOID',
    'struct':'STRUCT',
    'in': 'IN',
    'for': 'FOR',
    'to_owned' : 'TO_OWNED',
    'len' : 'LEN',
    'contains' : 'CONTAINS',
    'Vec' : 'VEC_U',
    'vec' : 'VEC_L',
    'new' : 'NEW',
    'with_capacity' : 'WITH_CAPACITY',
    'push':'PUSH',
    'insert':'INSERT',
    'remove': 'REMOVE',
    'contains':'CONTAINS',
    'capacity':'CAPACITY',
    'chars':'CHARS',
    'usize':'USIZE',
    'clone':'CLONE'

}

tokens = [
             'DECIMAL',
             'ENTERO',
             'ID',
             'MAS',
             'MENOS',
             'MULTI',
             'MODULO',
             'DIV',
             'PAR_I',
             'PAR_D',
             'LLV_I',
             'LLV_D',
             'D_PUNTO',
             'PUNTOCOMA',
             'COMA',
             'MAYOR',
             'MENOR',
             'MAYOR_I',
             'MENOR_I',
             'NO_IGUAL',
             'OR',
             'AND',
             'NOT',
             'IGUAL',
             'D_IGUAL',
             'GUION_B',
             'BARRA',
             'PUNTO',
             'CADENA',
             'AMP',
             'CHAR_S',
             'COR_I',
             'COR_D'
         ] + list(reservadas.values())

# Caracteres ignorados
t_ignore = '\r\t '

# Tokens con Regex
t_MAS = r'\+'
t_MENOS = r'-'
t_DIV = r'/'
t_MULTI = r'\*'
t_PAR_I = r'\('
t_PAR_D = r'\)'
t_LLV_I = r'\{'
t_LLV_D = r'\}'

t_COR_I = r'\['
t_COR_D = r'\]'

t_PUNTOCOMA = r';'
t_MODULO = r'%'
t_COMA = r','
t_D_PUNTO = r'\:'
t_MAYOR = r'\>'
t_MENOR = r'\<'
t_MAYOR_I = r'\>\='
t_MENOR_I = r'\<\='
t_D_IGUAL = r'\=\='
t_IGUAL = r'\='
t_NO_IGUAL = r'\!\='
t_OR = r'\|\|'
t_AND = r'&&'
t_NOT = r'!'
t_GUION_B = r'\_'
t_BARRA = r'\|'
t_PUNTO = r'\.'
t_AMP = r'&'



def t_ID(t):
    r'[a-zA-Z][a-zA-Z_0-9]*'
    t.type = reservadas.get(t.value, 'ID')  # Check for reserved words
    return t


def t_DECIMAL(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Float value too large %d", t.value)
        t.value = 0.0
    return t

def t_ENTERO(t):
    r"""\d+"""
    try:
        t.value = int(t.value)
    except ValueError:
        t.value = 0
    return t

def t_CADENA(t):
    r'"([^"]*)"'
    t.value = str(t.value).replace('"', '')
    return t

def t_CHAR_S(t):
    r'\'[^\']\''
    t.value = str(t.value).replace('\'', '')
    return t



def t_ID_(t):
    r'[a-zA-Z_][a-zA-Z_0-9]+'
    t.type = reservadas.get(t.value, 'ID')  # Check for reserved words
    return t

# Ignora y hace una accion
def t_ignorar_salto(t):
    r"""\n+"""
    t.lexer.lineno += t.value.count('\n')
    
    
def t_COMENTARIO_SIMPLE(t):
    r'//.*\n'
    t.lexer.lineno += 1
    

def t_COMENTARIO_MULTILINEA(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')


# Manejo de errores lexicos
def t_error(t):
    print(f'Caracter no reconocido {t.value[0]!r} en la linea {t.lexer.lineno}')
    t.lexer.skip(1)
    error = Error_("Lexico", f'Caracter {t.value[0]!r} no reconocido', t.lexer.lineno,0)
    Program.errores.append(error)
    


lexer = lex.lex()
