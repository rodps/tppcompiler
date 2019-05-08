import sys
from ply import lex

tokens = [
    'ID',
    'ABRE_PARENTESE',
    'FECHA_PARENTESE',
    'ABRE_COLCHETE',
    'FECHA_COLCHETE',
    'DOIS_PONTOS',
    'MAIOR',
    'MENOR',
    'DIFERENTE',
    'MAIOR_IGUAL',
    'MENOR_IGUAL',
    'MAIS',
    'MENOS',
    'MULT',
    'DIVISAO',
    'IGUAL',
    'E_LOGICO',
    'OU_LOGICO',
    'NEGACAO',
    'NUM_INT',
    'NUM_FLUT',
    'NUM_NOTACAO',
    'VIRGULA',
    'ATRIBUICAO'
]
reserved = {
    'inteiro' : 'INTEIRO',
    'flutuante' : 'FLUTUANTE',
    'leia' : 'LEIA',
    'escreva' : 'ESCREVA',
    'se' : 'SE',
    'então' : 'ENTAO',
    'senão' : 'SENAO',
    'repita' : 'REPITA',
    'até': 'ATE',
    'retorna': 'RETORNA',
    'fim': 'FIM'
}
tokens += list(reserved.values())

# Expressões regulares para os tokens
t_ABRE_PARENTESE = r'\('
t_FECHA_PARENTESE = r'\)'
t_ABRE_COLCHETE = r'\['
t_FECHA_COLCHETE = r'\]'
t_DOIS_PONTOS = r':'
t_MAIOR = r'>'
t_MENOR = r'<'
t_DIFERENTE = r'<>'
t_MAIOR_IGUAL = r'>='
t_MENOR_IGUAL = r'<='
t_MAIS = r'\+'
t_MENOS = r'-'
t_MULT = r'\*'
t_DIVISAO = r'/'
t_IGUAL = r'='
t_E_LOGICO = r'&&'
t_OU_LOGICO = r'\|\|'
t_NEGACAO = r'!'
t_NUM_FLUT = r'\d+\.\d+'
t_NUM_INT = r'\d+'
t_NUM_NOTACAO = r'\d+(\.\d+)?e\d+'
t_VIRGULA = r','
t_ATRIBUICAO = r':='

def t_ID(t):
    r'[a-zA-Zãé_][a-zA-Zãé_0-9]*'
    t.type = reserved.get(t.value,'ID')    # Check for reserved words
    return t

# Caracteres ignorados
t_ignore  = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_comment(t):
    r'\{[^\}]+\}'
    for c in t.value:
        if(c == '\n'): t.lexer.lineno += 1
    pass

# Tratamento de erros
def t_error(t):
    print("Caracter ilegar '%s', %d" % (t.value[0], t.lineno))
    t.lexer.skip(1)

lexer = lex.lex()

try:
    arq_code = open(sys.argv[1], 'r')
except FileNotFoundError:
    sys.exit("arquivo nao encontrado")

# Give the lexer some input
lexer.input(arq_code.read())

# # Tokenize
while True:
    tok = lexer.token()
    if not tok: 
        break      # No more input
    print(tok.lineno, tok.type)

arq_code.close()