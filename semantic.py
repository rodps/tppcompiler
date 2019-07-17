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
            lista_param = node.children[1].children[2]
            while True:
                for child in lista_param.children:
                    if child.name == 'parametro':
                        var = {'data_type': child.children[0], 'id': child.children[1].children[0],
                                'scope': id, 'type': 'var'}
                        if table_contains(var['id'], scope=id, type='var'):
                            print("Erro semântico: já existe uma variável com o mesmo nome ('{}'). Escopo: {}"
                                    .format(var['id'], scope))
                            return False
                        symbols_table.append(var)
                        params.append({'data_type': child.children[0], 'id': child.children[1].children[0]})
                
                if len(lista_param.children) > 0 and lista_param.children[0].name == 'lista_parametros':
                    lista_param = lista_param.children[0]
                else:
                    break    
        elif node.children[1].children[2].name == 'parametro':
            param = node.children[1].children[2]
            var = {'data_type': param.children[0], 'id': param.children[1].children[0],
                    'scope': id, 'type': 'var'}
            symbols_table.append(var)
            params.append({'data_type': param.children[0], 'id': param.children[1].children[0]})
        symbol = {'id': id, 'scope': scope[-1], 'type': 'function', 'data_type': data_type,
                  'params': params}
        if symbol in symbols_table:
            print('Erro semântico: Já existe uma função com o mesmo nome. ->', id)
            return False
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
            lista_var = node.children[1]
            while True:
                for child in lista_var.children:
                    if child.name == 'var':
                        id = child.children[0].children[0]
                        indice = child.children[1]
                        dim = 1
                        if check_type(indice) == 'flutuante':
                            print("Erro semântico: tipo do indice deve ser inteiro.")
                            return False
                        while True:
                            if indice.children[0].__str__() == 'indice':
                                dim += 1
                                indice = indice.children[0]
                            else:
                                break;
                        symbol = {'id': id, 'scope': scope[-1], 'type': 'var',
                                    'data_type': data_type, 'dim': dim}
                        if table_contains(id, scope[-1], 'var'):
                            print('Erro semântico: Esta variável já foi declarada. ->', id, 'escopo', scope)
                            return False
                        symbols_table.append(symbol)
                    elif child.name == 'ID':
                        id = child.children[0]
                        symbol = {'id': id, 'scope': scope[-1], 'type': 'var', 'data_type': data_type}
                        if table_contains(id, scope[-1], 'var'):
                            print('Erro semântico: Esta variável já foi declarada. ->', id, 'escopo', scope)
                            return False
                        symbols_table.append(symbol)
                if lista_var.children[0].name == 'lista_variaveis':
                    lista_var = lista_var.children[0]
                else:
                    break

            # for child in node.children[1].children:
            #     if child.name == 'var':
            #         id = child.children[0].children[0]
            #         indice = child.children[1]
            #         dim = 1
            #         while True:
            #             if indice.children[0].__str__() == 'indice':
            #                 dim += 1
            #                 indice = indice.children[0]
            #             else:
            #                 break;
            #         if check_type(indice) == 'flutuante':
            #             print("Erro semântico: tipo do indice deve ser inteiro.")
            #             return
            #         symbol = {'id': id, 'scope': scope[-1], 'type': 'var',
            #                     'data_type': data_type, 'dim': dim}
            #     else:
            #         id = child.children[0]
            #         symbol = {'id': id, 'scope': scope[-1], 'type': 'var', 'data_type': data_type}
            #     if table_contains(id, scope[-1], 'var'):
            #         print('Erro semântico: Esta variável já foi declarada. ->', id, 'escopo', scope[-1])
            #         return
            #     symbols_table.append(symbol)
        else:
            if node.children[1].name == 'var':
                id = node.children[1].children[0].children[0]
                dim = 1
                indice = node.children[1].children[1]
                if check_type(indice) == 'flutuante':
                    print("Erro semântico: tipo do indice deve ser inteiro ({}). Escopo: {}"
                            .format(id, scope))
                    return False
                while True:
                    if indice.children[0].__str__() == 'indice':
                        dim += 1
                        indice = indice.children[0]
                    else:
                        break;
                symbol = {'id': id, 'scope': scope[-1], 'type': 'var',
                            'data_type': data_type, 'dim': dim}
            else:
                id = node.children[1].children[0]
                symbol = {'id': id, 'scope': scope[-1], 'type': 'var', 'data_type': data_type}
            if table_contains(id, scope[-1], 'var'):
                print('Erro semântico: Esta variável já foi declarada. ->', id, 'escopo', scope)
                return False
            symbols_table.append(symbol)

    if node.__str__() == 'chamada_funcao':
        id = node.children[0].children[0]
        args = []
        function = table_contains(id, type='function')

        if not function:
            print("Erro semântico: Esta função não foi declarada. ->", id)
            return False

        if node.children[2].name == 'lista_argumentos':
            lista_arg = node.children[2]
            next = lista_arg
            while True:
                for child in lista_arg.children:
                    if child.name == 'lista_argumentos':
                        next = child
                    else:
                        args.append(check_type(child))
                if next != lista_arg:
                    lista_arg = next
                else:
                    break
                # if child.name == 'ID':
                #     arg = child.children[0]
                #     symbol = table_contains(arg, type='var')
                #     if not symbol:
                #         print("Erro semântico: Esta variável não foi declarada. ->", arg ,', escopo', scope)
                #         return
                #     args.append(symbol['data_type'])
                # if child.name == 'NUM_INT':
                #     arg = child.children[0]
                #     args.append('inteiro')
                # if child.name == 'NUM_FLUT':
                #     arg = child.children[0]
                #     args.append('flutuante')
        # elif node.children[2].name == 'ID':
        #     arg = node.children[2].children[0]
        #     symbol = table_contains(arg, type='var')
        #     if not symbol:
        #         print("Erro semântico: Esta variável não foi declarada. ->", arg)
        #         return
        #     args.append(symbol['data_type'])
        else:
            args.append(check_type(node.children[2]))
        
        if len(args) != len(function['params']):
            print("Erro semântico: Numero de argumentos não combina. ->", id)
            return False
        else:
            for i in range(len(args)):
                assignment(function['params'][i], args[i])
    
    if node.__str__() == 'atribuicao':
        id = None
        if node.children[0].name == 'ID':
            id = node.children[0].children[0]
            for s in scope:
                var = table_contains(id, scope=s)
                if var:
                    break
            if not var:
                print("Erro semântico: váriavel não foi declarada. -> ", id, ", função:", scope[-1])
                return False
        elif node.children[0].name == 'var':
            id = node.children[0].children[0].children[0]
            for s in scope:
                var = table_contains(id, scope=s)
                if var:
                    break
            if not var:
                print("Erro semântico: váriavel não foi declarada. -> ", id, ", função:", scope[-1])
                return False
            indice = node.children[0].children[1]
            for i in range(var['dim']):
                if indice.children[0].__str__() == 'indice':
                    indice = indice.children[0]
                else:
                    if i < (var['dim'] - 1):
                        print("Erro semântico: dimensão da matriz não corresponde ao declarado.")
                        return False
        
        # dtype = 'inteiro'
        # queue = [node.children[2]]
        # while(len(queue) > 0):
        #     next = queue.pop(0)
        #     if next.name == 'ID':
        #         var = table_contains(next.children[0])
        #         if not var:
        #             print("Erro semântico: variável não declarada. ->", next.children[0], ", escopo", scope)
        #             return
        #     if dtype == 'inteiro':
        #         if next.name == 'ID':
        #             var = table_contains(next.children[0])
        #             dtype = var['data_type']
        #         elif next.name == 'NUM_INT':
        #             dtype = 'inteiro'
        #         elif next.name == 'NUM_FLUT':
        #             dtype = 'flutuante'
        #         elif next.name == 'NUM_NOTACAO':
        #             if str(next.children[0]).find('.'):
        #                 dtype = 'flutuante'
        #             else:
        #                 dtype = 'inteiro'
        #     for child in next.children:
        #         if isinstance(child, tree.Node):
        #             queue.append(child)

        dtype = check_type(node.children[2])
        assignment(var, dtype)

    # if node.__str__() == 'indice':
    #     dtype = check_type(node)
    #     if dtype != 'inteiro':
    #         print("Erro semântico: o indice do array deve ser inteiro.")
    
    if node.__str__() == 'leia':
        if not isinstance(node, tree.Node):
            return False
        if node.children[2].name == 'ID':
            if not procura_variavel(node.children[2].children[0]):
                print('Erro semântico: variavel nao declarada na funcao leia')
                return False
        if node.children[2].name == 'var':
            if not checa_array(node.children[2]):
                return False

    if node.__str__() == 'retorna':
        if not isinstance(node, tree.Node):
            return False
        dtype = check_type(node)
        function = table_contains(scope[1])
        if dtype != function['data_type']:
            print("Erro semântico: tipo retornado incompatível. Função -> ", function['id'])
            return False

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

def check_type(node):
    queue = [node]
    while(len(queue) > 0):
        next = queue.pop(0)
        if next.name == 'NUM_FLUT':
            return 'flutuante'
        elif next.name == 'NUM_NOTACAO':
            if str(next.children[0]).find('.'):
                return 'flutuante'            
        elif next.name == 'ID':
            var = table_contains(next.children[0])
            if var:
                if var['data_type'] == 'flutuante':
                    return 'flutuante'
            else:
                print("Erro semântico: variavel nao declarada. -> {}. Escopo: {}"
                        .format(next.children[0], scope))
                return
        elif next.name == 'chamada_funcao':
            var = table_contains(next.children[0].children[0])
            if var:
                if var['data_type'] == 'flutuante':
                    return 'flutuante'
                else:
                    return 'inteiro'
            else:
                print("Erro semântico: função nao declarada. -> {}. Escopo: {}"
                        .format(next.children[0].children[0], scope))
            return
        for child in next.children:
            if isinstance(child, tree.Node):
                queue.append(child)
    return 'inteiro'

def assignment(var1, t2):
    if var1['data_type'] == 'inteiro' and t2 == 'flutuante':
        print("Aviso: cast de flutuante para inteiro ({}). Escopo: {}".format(var1['id'], scope))
    elif var1['data_type'] == 'flutuante' and t2 == 'inteiro':
        print("Aviso: cast de inteiro para flutuante ({}). Escopo {}".format(var1['id'], scope))

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

def tem_principal():
    if table_contains('principal', scope='programa', type='function'):
        return True
    return False    

if symbols(root) == False:
    sys.exit()
for func in functions:
    if tem_retorno(func) != True and func.children[0] != 'vazio':
        print("Erro semântico: função sem retorno ({})."
            .format(func.children[1].children[0].children[0]))
        sys.exit()
if not tem_principal():
    sys.exit("Erro semântico: o programa nao tem funcao principal.")

# for symbol in symbols_table:
#     print(symbol)