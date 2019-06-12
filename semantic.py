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
        symbol = {'id': id, 'scope': scope, 'type': 'function', 'data_type': data_type}
        if symbol in symbols_table:
            print('Erro semântico: Já existe uma função com o mesmo nome. ->', id)
            return
        symbols_table.append(symbol)
        scope = id

    if node.name == 'declaracao_variaveis':
        for i in range(2, len(node.children)):
            id = node.children[i].children[0]
            data_type = node.children[0]
            symbol = {'id': id, 'scope': scope, 'type': 'var', 'data_type': data_type, 'value': 0}
            if table_contains(id, scope, 'var'):
                print('Erro semântico: Esta variável já foi declarada. ->', id)
                return
            symbols_table.append(symbol)

    if node.name == 'parametro':
        data_type = node.children[0]
        id = node.children[2].children[0]
        symbol = {'id': id, 'scope': scope, 'type': 'var', 'data_type': data_type, 'value': 0}
        if table_contains(id, scope, 'var'):
            print('Erro semântico: Esta variável já foi declarada. ->', id)
            return
        symbols_table.append(symbol)

    if node.name == 'chamada_funcao':
        id = node.children[0]
        function = table_contains(id, type='function')

        if not function:
            print("Erro semântico: Esta função não foi declarada. ->", id)
            return

        if node.children[2] == 'lista_argumentos':
            for child in node.children[2]:
                if isinstance(child, tree.Node):
                    arg = child.children[0]
                    symbol = table_contains(arg, type='var')
                    if not symbol:
                        print("Erro semântico: Esta variável não foi declarada. ->", id)
                        return
                    else:



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