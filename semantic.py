import tree
from parser import root
from graphviz import Digraph

# poda a arvore
tree.prune(root)
dot = Digraph()
tree.make_graph(dot, root)
dot.render('graph-output/arvore-sintatica-poda.gv', view=False)

symbols_table = []

def symbols(node: tree.Node, scope='programa'):
    
    if not isinstance(node, tree.Node):
        return

    if node.name == 'declaracao_funcao':
        data_type = node.children[0]
        id = node.children[1].children[0].children[0]
        params = []
        if node.children[1].children[2].name == 'lista_parametros':
            for child in node.children[1].children[2].children:
                param = {'type': child.children[0], 'id': child.children[1].children[0], 'value': 0}
                params.append(param)
        elif node.children[1].children[2].name == 'parametro':
            param = node.children[1].children[2]
            params.append({'type': param.children[0], 'id': param.children[1].children[0], 'value': 0})
        symbol = {'id': id, 'scope': scope, 'type': 'function', 'data_type': data_type,
                  'params': params}
        if symbol in symbols_table:
            print('Erro semântico: Já existe uma função com o mesmo nome. ->', id)
            return
        symbols_table.append(symbol)
        scope = id

    if node.name == 'declaracao_variaveis':
        data_type = node.children[0]
        if node.children[1].name == 'lista_variaveis':
            for child in node.children[1].children:
                id = child.children[0]
                symbol = {'id': id, 'scope': scope, 'type': 'var', 'data_type': data_type, 'value': 0}
                if table_contains(id, scope, 'var'):
                    print('Erro semântico: Esta variável já foi declarada. ->', id, 'escopo', scope)
                    return
                symbols_table.append(symbol)
        else:
            id = node.children[1].children[0]
            symbol = {'id': id, 'scope': scope, 'type': 'var', 'data_type': data_type, 'value': 0}
            if table_contains(id, scope, 'var'):
                print('Erro semântico: Esta variável já foi declarada. ->', id, 'escopo', scope)
                return
            symbols_table.append(symbol)

    if node.name == 'chamada_funcao':
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
            print("Erro semântico: Numero de argumentos. ->", id)
            return
        else:
            for i in range(len(args)):
                function['params'][i]['value'] = args[i]['value']

    for child in node.children:
        symbols(child, scope)

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
print(symbols_table)