import sys
import tree
import ply.yacc as yacc
from scanner import tokens
from graphviz import Digraph

class Parser:

    def __init__(self, code):
        self.code = code
        self.parser = yacc.yacc()
        self.id = -1
    
    def parse(self):
        return self.parser.parse(code.read())
    
    def get_next_id(self):
        self.id += 1
        return self.id
        
def p_programa(p):
    'programa : lista_declaracoes'
    p[0] = tree.Node(parser.get_next_id(), 'programa', p[1:])

def p_lista_declaracoes(p):
    '''lista_declaracoes : lista_declaracoes declaracao
                         | declaracao'''
    p[0] = tree.Node(parser.get_next_id(), 'lista_declaracoes', p[1:])

def p_declaracao(p):
    '''declaracao : declaracao_variaveis
                  | inicializacao_variaveis
                  | declaracao_funcao'''
    p[0] = tree.Node(parser.get_next_id(), 'declaracao', p[1:])

def p_declaracao_variaveis(p):
    'declaracao_variaveis : tipo DOIS_PONTOS lista_variaveis'
    p[0] = tree.Node(parser.get_next_id(), 'declaracao_variaveis', p[1:])

def p_declaracao_variaveis_error(p):
    'declaracao_variaveis : tipo DOIS_PONTOS error'
    print("Ao declarar variável.")

def p_declaracao_variaveis_error2(p):
    'declaracao_variaveis : error DOIS_PONTOS lista_variaveis'
    print("Ao declarar variável.")

def p_inicializacao_variaveis(p):
    'inicializacao_variaveis : atribuicao'
    p[0] = tree.Node(parser.get_next_id(), 'inicializacao_variaveis', p[1:])

def p_lista_variaveis(p):
    '''lista_variaveis : lista_variaveis VIRGULA var
                       | var'''
    p[0] = tree.Node(parser.get_next_id(), 'lista_variaveis', p[1:])

def p_var(p):
    '''var : id 
           | id indice'''
    p[0] = tree.Node(parser.get_next_id(), 'var', p[1:])

def p_indice(p):
    '''indice : indice ABRE_COLCHETE expressao FECHA_COLCHETE
              | ABRE_COLCHETE expressao FECHA_COLCHETE'''
    p[0] = tree.Node(parser.get_next_id(), 'indice', p[1:])

def p_tipo(p):
    '''tipo : INTEIRO
            | FLUTUANTE'''
    p[0] = tree.Node(parser.get_next_id(), 'tipo', p[1:])

def p_declaracao_funcao(p):
    '''declaracao_funcao : tipo cabecalho
                         | cabecalho'''
    if len(p) > 2:
        p[0] = tree.Node(parser.get_next_id(), 'declaracao_funcao', p[1:])
    else:
        p[0] = tree.Node(parser.get_next_id(), 'declaracao_funcao', ['vazio', p[1]])

def p_declaracao_funcao_error(p):
    '''declaracao_funcao : error cabecalho'''
    print('Ao declarar função: tipo incorreto.')

def p_cabecalho(p):
    'cabecalho : id ABRE_PARENTESE lista_parametros FECHA_PARENTESE corpo FIM'
    p[0] = tree.Node(parser.get_next_id(), 'cabecalho', p[1:])

def p_cabecalho_error(p):
    'cabecalho : error ABRE_PARENTESE lista_parametros FECHA_PARENTESE corpo FIM'
    print('No identificador da função.')

def p_cabecalho_error2(p):
    'cabecalho : id ABRE_PARENTESE error FECHA_PARENTESE corpo FIM'
    print('Na lista de parametros.')


def p_lista_parametros(p):
    '''lista_parametros : lista_parametros VIRGULA parametro
                        | parametro
                        | empty'''
    if(p[1] != None):
        p[0] = tree.Node(parser.get_next_id(), 'lista_parametros', p[1:])
    else:
        p[0] = tree.Node(parser.get_next_id(), 'lista_parametros')

def p_parametro(p):
    '''parametro : tipo DOIS_PONTOS id
                 | parametro ABRE_COLCHETE FECHA_COLCHETE'''
    p[0] = tree.Node(parser.get_next_id(), 'parametro', p[1:])

def p_corpo(p):
    '''corpo : corpo acao
             | empty'''
    if(p[1] != None):
        p[0] = tree.Node(parser.get_next_id(), 'corpo', p[1:])
    else:
        p[0] = tree.Node(parser.get_next_id(), 'corpo')

def p_acao(p):
    '''acao : expressao
            | declaracao_variaveis
            | se
            | repita
            | leia
            | escreva
            | retorna'''
    p[0] = tree.Node(parser.get_next_id(), 'acao', p[1:])

def p_se(p):
    '''se : SE expressao ENTAO corpo FIM
          | SE expressao ENTAO corpo SENAO corpo FIM'''
    p[0] = tree.Node(parser.get_next_id(), 'se', p[1:])

def p_repita(p):
    'repita : REPITA corpo ATE expressao'
    p[0] = tree.Node(parser.get_next_id(), 'repita', p[1:])

def p_atribuicao(p):
    'atribuicao : var ATRIBUICAO expressao'
    p[0] = tree.Node(parser.get_next_id(), 'atribuicao', p[1:])

def p_leia(p):
    'leia : LEIA ABRE_PARENTESE var FECHA_PARENTESE'
    p[0] = tree.Node(parser.get_next_id(), 'leia', p[1:])

def p_escreva(p):
    'escreva : ESCREVA ABRE_PARENTESE expressao FECHA_PARENTESE'
    p[0] = tree.Node(parser.get_next_id(), 'escreva', p[1:])

def p_retorna(p):
    'retorna : RETORNA ABRE_PARENTESE expressao FECHA_PARENTESE'
    p[0] = tree.Node(parser.get_next_id(), 'retorna', p[1:])

def p_expressao(p):
    '''expressao : expressao_logica
                 | atribuicao'''
    p[0] = tree.Node(parser.get_next_id(), 'expressao', p[1:])

def p_expressao_logica(p):
    '''expressao_logica : expressao_simples
                        | expressao_logica operador_logico expressao_simples'''
    p[0] = tree.Node(parser.get_next_id(), 'expressao_logica', p[1:])

def p_expressao_simples(p):
    '''expressao_simples : expressao_aditiva
                         | expressao_simples operador_relacional expressao_aditiva'''
    p[0] = tree.Node(parser.get_next_id(), 'expressao_simples', p[1:])

def p_expressao_aditiva(p):
    '''expressao_aditiva : expressao_multiplicativa
                         | expressao_aditiva operador_soma expressao_multiplicativa'''
    p[0] = tree.Node(parser.get_next_id(), 'expressao_aditiva', p[1:])

def p_expressao_multiplicativa(p):
    '''expressao_multiplicativa : expressao_unaria
                                | expressao_multiplicativa operador_multiplicacao expressao_unaria'''
    p[0] = tree.Node(parser.get_next_id(), 'expressao_multiplicativa', p[1:])

def p_expressao_unaria(p):
    '''expressao_unaria : fator
                        | operador_soma fator
                        | operador_negacao fator'''
    p[0] = tree.Node(parser.get_next_id(), 'expressao_unaria', p[1:])

def p_operador_relacional(p):
    '''operador_relacional : MENOR
                           | MAIOR
                           | IGUAL
                           | DIFERENTE
                           | MENOR_IGUAL
                           | MAIOR_IGUAL'''
    p[0] = tree.Node(parser.get_next_id(), 'operador_relacional', p[1:])

def p_operador_soma(p):
    '''operador_soma : MAIS
                     | MENOS'''
    p[0] = tree.Node(parser.get_next_id(), 'operador_soma', p[1:])

def p_operador_logico(p):
    '''operador_logico : E_LOGICO
                       | OU_LOGICO'''
    p[0] = tree.Node(parser.get_next_id(), 'operador_logico', p[1:])

def p_operador_negacao(p):
    'operador_negacao : NEGACAO'
    p[0] = tree.Node(parser.get_next_id(), 'operador_negacao', p[1:])

def p_operador_multiplicacao(p):
    '''operador_multiplicacao : MULT
                              | DIVISAO'''
    p[0] = tree.Node(parser.get_next_id(), 'operador_multiplicacao', p[1:])

def p_fator(p):
    '''fator : ABRE_PARENTESE expressao FECHA_PARENTESE
             | var
             | chamada_funcao
             | numero'''
    p[0] = tree.Node(parser.get_next_id(), 'fator', p[1:])

def p_numero(p):
    '''numero : num_int
              | num_flut
              | num_notacao'''
    p[0] = tree.Node(parser.get_next_id(), 'numero', p[1:])

def p_chamada_funcao(p):
    'chamada_funcao : id ABRE_PARENTESE lista_argumentos FECHA_PARENTESE'
    p[0] = tree.Node(parser.get_next_id(), 'chamada_funcao', p[1:])

def p_lista_argumentos(p):
    '''lista_argumentos : lista_argumentos VIRGULA expressao
                        | expressao
                        | empty '''
    if(p[1] != None):
        p[0] = tree.Node(parser.get_next_id(), 'lista_argumentos', p[1:])
    else:
        p[0] = tree.Node(parser.get_next_id(), 'lista_argumentos')

def p_id(p):
    'id : ID'
    p[0] = tree.Node(parser.get_next_id(), 'ID', p[1:])

def p_num_int(p):
    'num_int : NUM_INT'
    p[0] = tree.Node(parser.get_next_id(), 'NUM_INT', p[1:])

def p_num_flut(p):
    'num_flut : NUM_FLUT'
    p[0] = tree.Node(parser.get_next_id(), 'NUM_FLUT', p[1:])

def p_num_notacao(p):
    'num_notacao : NUM_NOTACAO'
    p[0] = tree.Node(parser.get_next_id(), 'NUM_NOTACAO', p[1:])

def p_empty(p):
    'empty :'
    pass

def p_error(p):
    if p:
        print("Erro de sintaxe: '%s' na linha %d." % (p.value, p.lineno))
    else:
        print("Syntax error at EOF")

# Abrir o arquivo código
try:
    code = open(sys.argv[1], 'r')
except FileNotFoundError:
    sys.exit("arquivo nao encontrado")

parser = Parser(code)
root = parser.parse()
if root == None:
    sys.exit()

dot = Digraph() # Função da biblioteca Graphviz responsável por criar um grafo.
tree.make_graph(dot, root) # Constrói o grafo que representa a árvore sintática.
dot.render('graph-output/arvore-sintatica.gv', view=False) # Salva o grafo na pasta especificada.