import tree
import sys
from parser import root
from graphviz import Digraph

# poda a arvore
tree.prune(root)
dot = Digraph()
tree.make_graph(dot, root)
dot.render('graph-output/arvore-sintatica-poda.gv', view=False)

symbols_table = []
functions = []
scope = ['programa']

def symbols(node: tree.Node):

    if node.__str__() == 'declaracao_funcao':
        functions.append(node)
        data_type = node.children[0]
        id = node.children[1].children[0].children[0]
        params = []
        if node.children[1].children[2].name == 'lista_parametros':
            for child in node.children[1].children[2].children:
                param = {'data_type': child.children[0], 'id': child.children[1].children[0]}
                params.append(param)
        elif node.children[1].children[2].name == 'parametro':
            param = node.children[1].children[2]
            params.append({'data_type': param.children[0], 'id': param.children[1].children[0]})
        symbol = {'id': id, 'scope': scope[-1], 'type': 'function', 'data_type': data_type,
                  'params': params}
        if symbol in symbols_table:
            print('Erro semântico: Já existe uma função com o mesmo nome. ->', id)
            return
        symbols_table.append(symbol)
        scope.append(id)
    
    if node.__str__() == 'se':
        if isinstance(node, tree.Node):
            scope.append('se'+str(node.id))
    
    if node.__str__() == 'senão':
        scope.append('senao'+scope[-1][2:])

    if node.__str__() == 'fim':
        scope.pop()
        if len(scope) > 0:
            if scope[-1][:2] == 'se':
                scope.pop()

    if node.__str__() == 'declaracao_variaveis':
        data_type = node.children[0]
        if node.children[1].name == 'lista_variaveis':
            for child in node.children[1].children:
                if child.name == 'var':
                    id = child.children[0].children[0]
                    indice = child.children[1]
                    index_size = []
                    while True:
                        if check_type(indice) == 'flutuante':
                            print("Erro semântico: tipo do indice deve ser inteiro.")
                            return
                        if indice.children[0].__str__() == 'indice':
                            index_size.append(int(indice.children[2].children[0]))
                            indice = indice.children[0]
                        else:
                            index_size.append(int(indice.children[1].children[0]))
                            break;
                    symbol = {'id': id, 'scope': scope[-1], 'type': 'var',
                                'data_type': data_type, 'index_size': index_size}
                else:
                    id = child.children[0]
                    symbol = {'id': id, 'scope': scope[-1], 'type': 'var', 'data_type': data_type}
                if table_contains(id, scope[-1], 'var'):
                    print('Erro semântico: Esta variável já foi declarada. ->', id, 'escopo', scope[-1])
                    return
                symbols_table.append(symbol)
        else:
            if node.children[1].name == 'var':
                id = node.children[1].children[0].children[0]
            else:
                id = node.children[1].children[0]
            symbol = {'id': id, 'scope': scope[-1], 'type': 'var', 'data_type': data_type}
            if table_contains(id, scope[-1], 'var'):
                print('Erro semântico: Esta variável já foi declarada. ->', id, 'escopo', scope)
                return
            symbols_table.append(symbol)

    if node.__str__() == 'chamada_funcao':
        id = node.children[0].children[0]
        args = []
        function = table_contains(id, type='function')

        if not function:
            print("Erro semântico: Esta função não foi declarada. ->", id)
            return

        if node.children[2].name == 'lista_argumentos':
            for child in node.children[2].children:
                arg = child.children[0]
                symbol = table_contains(arg, type='var')
                if not symbol:
                    print("Erro semântico: Esta variável não foi declarada. ->", arg ,', escopo', scope)
                    return
                args.append(symbol)
        
        elif node.children[2].name == 'ID':
            arg = node.children[2].children[0]
            symbol = table_contains(arg, type='var')
            if not symbol:
                print("Erro semântico: Esta variável não foi declarada. ->", arg)
                return
            args.append(symbol)
        
        if len(args) != len(function['params']):
            print("Erro semântico: Numero de argumentos não combina. ->", id)
            return
        else:
            for i in range(len(args)):
                assignment(function['params'][i]['data_type'], args[i]['data_type'])
    
    if node.__str__() == 'atribuicao':
        id = None
        if node.children[0].name == 'ID':
            id = node.children[0].children[0]
            for s in scope:
                var = table_contains(id)
                if not var:
                    print("Erro semântico: váriavel não foi declarada. -> ", id, ", função:", scope[-1])
                    return
        elif node.children[0].name == 'var':
            id = node.children[0].children[0].children[0]
            var = table_contains(id)
            if not var:
                print("Erro semântico: váriavel não foi declarada. -> ", id, ", função:", scope)
                return
            indice = node.children[0].children[1]
            for i in range(len(var['index_size'])):
                if indice.children[0].__str__() == 'indice':
                    indice = indice.children[0]
                else:
                    if i < (len(var['index_size']) - 1):
                        print("Erro semântico: dimensão da matriz não corresponde ao declarado.")
                        return
        
        dtype = 'inteiro'
        queue = [node.children[2]]
        while(len(queue) > 0):
            next = queue.pop(0)

            if next.name == 'ID':
                var = table_contains(next.children[0])
                if not var:
                    print("Erro semântico: variável não declarada. ->", next.children[0], ", escopo", scope)
                    return

            if dtype == 'inteiro':
                if next.name == 'ID':
                    var = table_contains(next.children[0])
                    dtype = var['data_type']
                elif next.name == 'NUM_INT':
                    dtype = 'inteiro'
                elif next.name == 'NUM_FLUT':
                    dtype = 'flutuante'
                elif next.name == 'NUM_NOTACAO':
                    if str(next.children[0]).find('.'):
                        dtype = 'flutuante'
                    else:
                        dtype = 'inteiro'

            for child in next.children:
                if isinstance(child, tree.Node):
                    queue.append(child)

        assignment(var['data_type'], dtype)

    if node.__str__() == 'indice':
        dtype = check_type(node)
        if dtype != 'inteiro':
            print("Erro semântico: o indice do array deve ser inteiro.")
    
    if node.__str__() == 'leia':
        if not isinstance(node, tree.Node):
            return
        if node.children[2].name == 'ID':
            if not procura_variavel(node.children[2].children[0]):
                print('Erro semântico: variavel nao declarada na funcao leia')
                return
        if node.children[2].name == 'var':
            if not checa_array(node.children[2]):
                return

    if node.__str__() == 'retorna':
        if not isinstance(node, tree.Node):
            return
        dtype = check_type(node)
        function = table_contains(scope[1])
        if dtype != function['data_type']:
            print("Erro semântico: tipo retornado incompatível.")
            return

    if isinstance(node, tree.Node):
        for child in node.children:
            symbols(child)

def checa_array(node):
    queue = [node.children[1]]
    dim = 1
    while len(queue) > 0:
        next = queue.pop(0)
        if next.name == 'NUM_FLUT':
            print("Erro semântico: indice só pode conter número inteiro.")
            return False
        if next.name == 'ID':
            var = procura_variavel(next.children[0])
            if not var:
                return False
            if var['data_type'] == 'flutuante':
                print("Erro semântico: indice só pode conter número inteiro.")
                return False
        for child in next.children:
            if isinstance(child, tree.Node):
                if child.name == 'indice':
                    dim += 1
                queue.append(child)
    var = procura_variavel(node.children[0].children[0])
    if not var:
        print("Erro semântico: variável não foi declarada. ->", node.children[0].children[0])
        return False
    if len(var['index_size']) != dim:
        print("Erro semântico: dimensões do array nao correspondem ao declarado.", node.children[0].children[0])
        return False

def procura_variavel(varname):
    for s in scope:
        var = table_contains(varname, scope=s, type='var')
        if var:
            return var

def tem_retorno(node):
    if node.name == 'se':
        if len(node.children) > 5:
            se = tem_retorno(node.children[3])
            senao = tem_retorno(node.children[5])
            return (se and senao)
    elif node.name == 'retorna':
        return True

    for child in node.children:
        if isinstance(child, tree.Node):
            if tem_retorno(child) == True:
                return True

def search(node, name):
    queue = [node]
    while len(queue) > 0:
        next = queue.pop(0)
        if next.name == name:
            return next
        for child in next.children:
            if isinstance(child, tree.Node):
                queue.append(child)

def check_type(node):
    queue = [node]
    while(len(queue) > 0):
        next = queue.pop(0)
        if next.name == 'NUM_FLUT':
            return 'flutuante'
        elif next.name == 'NUM_NOTACAO':
            if str(next.children[0]).find('.'):
                return 'flutuante'
        for child in next.children:
            if isinstance(child, tree.Node):
                queue.append(child)
    return 'inteiro'

def assignment(t1, t2):
    if t1 == 'inteiro' and t2 == 'flutuante':
        print("Aviso: cast de flutuante para inteiro.")
    elif t1 == 'flutuante' and t2 == 'inteiro':
        print("Aviso: cast de inteiro para flutuante.")

def table_contains(id, scope=None, type=None):
    for symbol in symbols_table:
        if symbol['id'] == id:
            if not scope and not type:
                return symbol
            if scope and not type:
                if symbol['scope'] == scope:
                    return symbol
            if not scope and type:
                if symbol['type'] == type:
                    return symbol
            if scope and type:
                if symbol['scope'] == scope and symbol['type'] == type:
                    return symbol
    return False

symbols(root)
for func in functions:
    if tem_retorno(func) != True:
        print("Erro semântico: função sem retorno.")
print(symbols_table)