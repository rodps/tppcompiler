import ply.yacc as yacc
import sys
from scanner import tokens
from graphviz import Digraph

# dot = Digraph(comment='teste')
# dot.node('A', 'King Arthur')
# dot.node('B', 'Sir Bedevere the Wise')
# dot.node('L', 'Sir Lancelot the Brave')

# dot.edges(['AB', 'AL'])
# dot.edge('B', 'L', constraint='false')

# print(dot.source)
# dot.render('test-output/round-table.gv', view=True)

def printTree(root):
    if(root == None):
        return
    print("pai: ", root)
    for child in root.childs:
            print(child)
    for child in root.childs:
        if(isinstance(child, Node)):
            printTree(child)

def makeGraph(dot, parent, id=0):
    print("pai: " + parent.name)
    if(id == 0):
        dot.node(str(id), parent.name)
    c = id
    for child in parent.childs:
        c += 1
        if(isinstance(child, Node)):
            dot.node(str(c), child.name)
            print(child.name)
        else:
            dot.node(str(c), child)
            print(child)
        dot.edge(str(id), str(c))
        if(isinstance(child, Node)):
            c = makeGraph(dot, child, c)
    return c + 1

class Node:
    def __init__(self, name, childs=[]):
        self.name = name
        self.childs = childs

    def __str__(self):
        return self.name
        
def p_programa(p):
    'programa : lista_declaracoes'
    p[0] = Node('programa', p[1:])

def p_lista_declaracoes(p):
    '''lista_declaracoes : lista_declaracoes declaracao
                         | declaracao'''
    p[0] = Node('lista_declaracoes', p[1:])

def p_declaracao(p):
    '''declaracao : declaracao_variaveis
                  | inicializacao_variaveis
                  | declaracao_funcao'''
    p[0] = Node('declaracao', p[1:])

def p_declaracao_variaveis(p):
    'declaracao_variaveis : tipo DOIS_PONTOS lista_variaveis'
    p[0] = Node('declaracao_variaveis', p[1:])

def p_inicializacao_variaveis(p):
    'inicializacao_variaveis : atribuicao'
    p[0] = Node('inicializacao_variaveis', p[1:])

def p_lista_variaveis(p):
    '''lista_variaveis : lista_variaveis VIRGULA var
                       | var'''
    p[0] = Node('lista_variaveis', p[1:])

def p_var(p):
    '''var : ID 
           | ID indice'''
    p[0] = Node('var', p[1:])

def p_indice(p):
    '''indice : indice ABRE_COLCHETE expressao FECHA_COLCHETE
              | ABRE_COLCHETE expressao FECHA_COLCHETE'''
    p[0] = Node('indice', p[1:])

def p_tipo(p):
    '''tipo : INTEIRO
            | FLUTUANTE'''
    p[0] = Node('tipo', p[1:])

def p_declaracao_funcao(p):
    '''declaracao_funcao : tipo cabecalho
                         | cabecalho'''
    p[0] = Node('declaracao_funcao', p[1:])

def p_cabecalho(p):
    'cabecalho : ID ABRE_PARENTESE lista_parametros FECHA_PARENTESE corpo FIM'
    p[0] = Node('cabecalho', p[1:])

def p_lista_parametros(p):
    '''lista_parametros : lista_parametros VIRGULA parametro
                        | parametro
                        | empty'''
    p[0] = Node('lista_parametros', p[1:])

def p_parametro(p):
    '''parametro : tipo DOIS_PONTOS ID
                 | parametro ABRE_COLCHETE FECHA_COLCHETE'''
    p[0] = Node('parametro', p[1:])

def p_corpo(p):
    '''corpo : corpo acao
             | empty'''
    p[0] = Node('corpo', p[1:])

def p_acao(p):
    '''acao : expressao
            | declaracao_variaveis
            | se
            | repita
            | leia
            | escreva
            | retorna'''
    p[0] = Node('acao', p[1:])

def p_se(p):
    '''se : SE expressao ENTAO corpo FIM
          | SE expressao ENTAO corpo SENAO corpo FIM'''
    p[0] = Node('se', p[1:])

def p_repita(p):
    'repita : REPITA corpo ATE expressao'
    p[0] = Node('repita', p[1:])

def p_atribuicao(p):
    'atribuicao : var ATRIBUICAO expressao'
    p[0] = Node('atribuicao', p[1:])

def p_leia(p):
    'leia : LEIA ABRE_PARENTESE var FECHA_PARENTESE'
    p[0] = Node('leia', p[1:])

def p_escreva(p):
    'escreva : ESCREVA ABRE_PARENTESE expressao FECHA_PARENTESE'
    p[0] = Node('escreva', p[1:])

def p_retorna(p):
    'retorna : RETORNA ABRE_PARENTESE expressao FECHA_PARENTESE'
    p[0] = Node('retorna', p[1:])

def p_expressao(p):
    '''expressao : expressao_logica
                 | atribuicao'''
    p[0] = Node('expressao', p[1:])

def p_expressao_logica(p):
    '''expressao_logica : expressao_simples
                        | expressao_logica operador_logico expressao_simples'''
    p[0] = Node('expressao_logica', p[1:])

def p_expressao_simples(p):
    '''expressao_simples : expressao_aditiva
                         | expressao_simples operador_relacional expressao_aditiva'''
    p[0] = Node('expressao_simples', p[1:])

def p_expressao_aditiva(p):
    '''expressao_aditiva : expressao_multiplicativa
                         | expressao_aditiva operador_soma expressao_multiplicativa'''
    p[0] = Node('expressao_aditiva', p[1:])

def p_expressao_multiplicativa(p):
    '''expressao_multiplicativa : expressao_unaria
                                | expressao_multiplicativa operador_multiplicacao expressao_unaria'''
    p[0] = Node('expressao_multiplicativa', p[1:])

def p_expressao_unaria(p):
    '''expressao_unaria : fator
                        | operador_soma fator
                        | operador_negacao fator'''
    p[0] = Node('expressao_unaria', p[1:])

def p_operador_relacional(p):
    '''operador_relacional : MENOR
                           | MAIOR
                           | IGUAL
                           | DIFERENTE
                           | MENOR_IGUAL
                           | MAIOR_IGUAL'''
    p[0] = Node('operador_relacional', p[1:])

def p_operador_soma(p):
    '''operador_soma : MAIS
                     | MENOS'''
    p[0] = Node('operador_soma', p[1:])

def p_operador_logico(p):
    '''operador_logico : E_LOGICO
                       | OU_LOGICO'''
    p[0] = Node('operador_logico', p[1:])

def p_operador_negacao(p):
    'operador_negacao : NEGACAO'
    p[0] = Node('operador_negacao', p[1:])

def p_operador_multiplicacao(p):
    '''operador_multiplicacao : MULT
                              | DIVISAO'''
    p[0] = Node('operador_multiplicacao', p[1:])

def p_fator(p):
    '''fator : ABRE_PARENTESE expressao FECHA_PARENTESE
             | var
             | chamada_funcao
             | numero'''
    p[0] = Node('fator', p[1:])

def p_numero(p):
    '''numero : NUM_INT
              | NUM_FLUT
              | NUM_NOTACAO'''
    p[0] = Node('numero', p[1:])

def p_chamada_funcao(p):
    'chamada_funcao : ID ABRE_PARENTESE lista_argumentos FECHA_PARENTESE'
    p[0] = Node('chamada_funcao', p[1:])

def p_lista_argumentos(p):
    '''lista_argumentos : lista_argumentos VIRGULA expressao
                        | expressao
                        | empty '''
    p[0] = Node('lista_argumentos', p[1:])

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
r = parser.parse(code.read())
# printTree(r)
dot = Digraph()
makeGraph(dot, r)
dot.render('test-output/round-table.gv', view=True)