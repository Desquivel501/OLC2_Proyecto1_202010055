from ply import lex

reservadas = {
    'ejecutar': 'EJECUTAR',
    'true': 'TRUE',
    'false':'FALSE',
    'pow':'POW_INT',
    'powf':'POW_FLOAT',
    'i64':'INT',
    'f64':'FLOAT'
     
}

tokens = [
             'DECIMAL',
             'ENTERO',
             'MAS',
             'MENOS',
             'MULTI',
             'MODULO',
             'DIV',
             'PAR_I',
             'PAR_D',
             'D_PUNTO',
             'PUNTOCOMA',
             'COMA',
             'MAYOR',
             'MENOR',
             'MAYOR_I',
             'MENOR_I',
             'D_IGUAL',
             'NO_IGUAL',
         ] + list(reservadas.values())

# Caracteres ignorados
t_ignore = '[\t ]'

# Tokens con Regex
t_MAS = r'\+'
t_MENOS = r'-'
t_DIV = r'/'
t_MULTI = r'\*'
t_PAR_I = r'\('
t_PAR_D = r'\)'
t_PUNTOCOMA = r'\;'
t_MODULO = r'%'
t_COMA = r','
t_D_PUNTO = r':'
t_MAYOR = r'>'
t_MENOR = r'<'
t_MAYOR_I = r'>='
t_MENOR_I = r'<='
t_D_IGUAL = r'=='
t_NO_IGUAL = r'!='


def t_DECIMAL(t):
    r'\d+.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Float value too large %d", t.value)
        t.value = 0
    return t

def t_ENTERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reservadas.get(t.value, 'ID')  # Check for reserved words
    return t

# Ignora y hace una accion
def t_ignorar_salto(t):
    r'\n+'
    t.lexer.lineno += t.value.count('\n')
    
def t_COMENTARIO_SIMPLE(t):
    r'//.*\n'
    t.lexer.lineno += 1


# Manejo de errores lexicos
def t_error(t):
    print(f'Caracter no reconocido {t.value[0]!r} en la linea {t.lexer.lineno}')
    t.lexer.skip(1)


lex.lex()