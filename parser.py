import ply.yacc as yacc
import sys
from scanner import tokens
from graphviz import Digraph

class Node:
    def __init__(self, name, childs=[]):
        self.name = name
        self.childs = childs
    def __str__(self):
        return self.name

def p_programa(p):
    'programa : lista_declaracoes'
    p[0] = Node('programa', [p[1]])

def p_lista_declaracoes(p):
    '''lista_declaracoes : lista_declaracoes declaracao
                         | declaracao'''
    if(len(p) > 2):
        p[0] = Node('lista_declaracoes', [p[1], p[2]])
    else:
        p[0] = Node('lista_declaracoes', [p[1]])

def p_declaracao(p):
    '''declaracao : declaracao_variaveis
                  | inicializacao_variaveis
                  | declaracao_funcao'''
    p[0] = Node('declaracao', [p[1]])

def p_declaracao_variaveis(p):
    'declaracao_variaveis : tipo DOIS_PONTOS lista_variaveis'
    p[0] = Node('declaracao_variaveis', [p[1], p[2], p[3]])

def p_inicializacao_variaveis(p):
    'inicializacao_variaveis : atribuicao'
    p[0] = Node('inicializacao_variaveis', [p[1]])

def p_lista_variaveis(p):
    '''lista_variaveis : lista_variaveis VIRGULA var
                       | var'''
    if(len(p) > 2):
        p[0] = Node('lista_variaveis', [p[1], p[2], p[3]])
    else:
        p[0] = Node('lista_variaveis', [p[1]])

def p_var(p):
    '''var : ID 
           | ID indice'''

def p_indice(p):
    '''indice : indice ABRE_COLCHETE expressao FECHA_COLCHETE
              | ABRE_COLCHETE expressao FECHA_COLCHETE'''

def p_tipo(p):
    '''tipo : INTEIRO
            | FLUTUANTE'''

def p_declaracao_funcao(p):
    '''declaracao_funcao : tipo cabecalho
                         | cabecalho'''

def p_cabecalho(p):
    'cabecalho : ID ABRE_PARENTESE lista_parametros FECHA_PARENTESE corpo FIM'

def p_lista_parametros(p):
    '''lista_parametros : lista_parametros VIRGULA parametro
                        | parametro
                        | empty'''

def p_parametro(p):
    '''parametro : tipo DOIS_PONTOS ID
                 | parametro ABRE_COLCHETE FECHA_COLCHETE'''

def p_corpo(p):
    '''corpo : corpo acao
             | empty'''

def p_acao(p):
    '''acao : expressao
            | declaracao_variaveis
            | se
            | repita
            | leia
            | escreva
            | retorna'''

def p_se(p):
    '''se : SE expressao ENTAO corpo FIM
          | SE expressao ENTAO corpo SENAO corpo FIM'''

def p_repita(p):
    'repita : REPITA corpo ATE expressao'

def p_atribuicao(p):
    'atribuicao : var ATRIBUICAO expressao'

def p_leia(p):
    'leia : LEIA ABRE_PARENTESE var FECHA_PARENTESE'

def p_escreva(p):
    'escreva : ESCREVA ABRE_PARENTESE expressao FECHA_PARENTESE'

def p_retorna(p):
    'retorna : RETORNA ABRE_PARENTESE expressao FECHA_PARENTESE'

def p_expressao(p):
    '''expressao : expressao_logica
                 | atribuicao'''

def p_expressao_logica(p):
    '''expressao_logica : expressao_simples
                        | expressao_logica operador_logico expressao_simples'''

def p_expressao_simples(p):
    '''expressao_simples : expressao_aditiva
                         | expressao_simples operador_relacional expressao_aditiva'''

def p_expressao_aditiva(p):
    '''expressao_aditiva : expressao_multiplicativa
                         | expressao_aditiva operador_soma expressao_multiplicativa'''

def p_expressao_multiplicativa(p):
    '''expressao_multiplicativa : expressao_unaria
                                | expressao_multiplicativa operador_multiplicacao expressao_unaria'''

def p_expressao_unaria(p):
    '''expressao_unaria : fator
                        | operador_soma fator
                        | operador_negacao fator'''

def p_operador_relacional(p):
    '''operador_relacional : MENOR
                           | MAIOR
                           | IGUAL
                           | DIFERENTE
                           | MENOR_IGUAL
                           | MAIOR_IGUAL'''

def p_operador_soma(p):
    '''operador_soma : MAIS
                     | MENOS'''

def p_operador_logico(p):
    '''operador_logico : E_LOGICO
                       | OU_LOGICO'''

def p_operador_negacao(p):
    'operador_negacao : NEGACAO'

def p_operador_multiplicacao(p):
    '''operador_multiplicacao : MULT
                              | DIVISAO'''

def p_fator(p):
    '''fator : ABRE_PARENTESE expressao FECHA_PARENTESE
             | var
             | chamada_funcao
             | numero'''

def p_numero(p):
    '''numero : NUM_INT
              | NUM_FLUT
              | NUM_NOTACAO'''

def p_chamada_funcao(p):
    'chamada_funcao : ID ABRE_PARENTESE lista_argumentos FECHA_PARENTESE'

def p_lista_argumentos(p):
    '''lista_argumentos : lista_argumentos VIRGULA expressao
                        | expressao
                        | empty '''

def p_empty(p):
    'empty :'
    pass

def p_error(p):
    if p:
        print("Syntax error: '%s' na linha %d" % (p.value, p.lineno))
    else:
        print("Syntax error at EOF")

# Build the parser
parser = yacc.yacc()

code = open(sys.argv[1], 'r')
parser.parse(code.read())