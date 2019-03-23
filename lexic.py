from ply.ply import lex

tokenTable = list();

tokens = [
    'ID',
    'ABRE_PARENTESE',
    'FECHA_PARENTESE',
    'ABRE_COLCHETE',
    'FECHA_COLCHETE',
    'ABRE_CHAVE',
    'FECHA_CHAVE',
    'DOIS_PONTOS',
    'MAIOR',
    'MENOR',
    'MAIS',
    'MENOS',
    'MULT',
    'DIVISAO',
    'IGUAL',
    'NUM_INT',
    'NUM_FLUT',
    'COMENTARIO',
    'PRINCIPAL',
    'VIRGULA'
]
reserved = {
    'inteiro' : 'INTEIRO',
    'flutuante' : 'FLUTUANTE',
    'vazio' : 'VAZIO',
    'se' : 'SE',
    'então' : 'ENTAO',
    'senão' : 'SENAO',
    'repita' : 'REPITA',
    'até': 'ATE',
    'retorna': 'RETORNA',
}
tokens += list(reserved.values())

# Expressões regulares para os tokens
t_ABRE_PARENTESE = r'\('
t_FECHA_PARENTESE = r'\)'
t_ABRE_COLCHETE = r'\['
t_FECHA_COLCHETE = r'\]'
t_ABRE_CHAVE = r'\{'
t_FECHA_CHAVE = r'\}'
t_DOIS_PONTOS = r':'
t_MAIOR = r'>'
t_MENOR = r'<'
t_MAIS = r'\+'
t_MENOS = r'-'
t_MULT = r'\*'
t_DIVISAO = r'/'
t_IGUAL = r'='
t_NUM_FLUT = r'\d+.\d+'
t_NUM_INT = r'\d+'
t_COMENTARIO = r'\{[^\}]+\}'
t_VIRGULA = r','

def t_ID(t):
    r'[a-zA-Zãé_][a-zA-Zãé_0-9]*'
    t.type = reserved.get(t.value,'ID')    # Check for reserved words
    tokenTable.append({
        'token_type': 'ID',
        'line': t.lineno,
        'type': '',
        'lexema': t.value
    })
    return t

# Caracteres ignorados
t_ignore  = ' \t\n'

# Tratamento de erros
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

arq_code = open('teste/bubble.tpp', 'r')
 
# Give the lexer some input
lexer.input(arq_code.read())
 
# # Tokenize
while True:
    tok = lexer.token()
    if not tok: 
        break      # No more input
    print(tok)

print(tokenTable)