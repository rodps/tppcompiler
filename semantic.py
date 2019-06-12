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

    if node.name == 'cabecalho':
        id = node.children[0].children[0]
        symbol = {'ID': id, 'scope': scope, 'type': 'function'}
        if symbol in symbols_table:
            print('Erro semantico: Já existe uma função com o mesmo nome. ->', id)
            return
        symbols_table.append(symbol)
        scope = id
    if node.name == 'declaracao_variaveis':
        for i in range(2, len(node.children)):
            id = node.children[i].children[0]
            symbol = {'ID': id, 'scope': scope, 'type': 'var', 'value': 0}
            if table_contains(id, scope, 'var'):
                print('Erro semantico: Esta variavel ja foi declarada. ->', id)
                return
            symbols_table.append(symbol)

    for child in node.children:
        symbols(child, scope)

def table_contains(ID, scope=None, type=None):
    for symbol in symbols_table:
        if symbol.ID == ID:
            if not scope and not type:
                return True
            if scope and not type:
                if symbol.scope == scope:
                    return True
            if not scope and type:
                if symbol.type == type:
                    return True
            if scope and type:
                if symbol.scope == scope and symbol.type == type:
                    return True
    return False

symbols(root)
print(symbols_table)