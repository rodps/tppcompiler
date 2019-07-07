from semantic import symbols_table, root
from llvmlite import ir
from tree import Node

module = ir.Module('modulo.bc')
functions = []
ifs = []
vars = []
repeat = []

class Function():
    def __init__(self, id: str, func: ir.Function, entryBlock: ir.Block, exitBlock: ir.Block):
        self.id = id
        self.func = func
        self.entryBlock = entryBlock
        self.exitBlock = exitBlock

class Se():
    def __init__(self, id, iftrue, iffalse, ifend):
        self.id = id
        self.iftrue = iftrue
        self.iffalse = iffalse
        self.ifend = ifend

class Var():
    def __init__(self, id, var, scope):
        self.id = id
        self.var = var
        self.scope = scope

class Repita():
    def __init__(self, id, block, end, expressao):
        self.id = id
        self.block = block
        self.expressao = expressao
        self.end = end

def percorreArvore(node: Node, scope=['global'], builder=None):

    if node.__str__() == 'declaracao_variaveis':
        ids = search(node.children[1], 'ID')
        for id in ids:
            var = get_symbol(id.children[0], type='var')
            if var['scope'] == 'programa':
                v = ir.GlobalVariable(module, ir.IntType(32), var['id'])
                v.initializer = ir.Constant(ir.IntType(32), 0)
                v.linkage = 'common'
                v.align = 4
                vars.insert(0, Var(var['id'], v, scope[-1]))
            else:
                # func = get_function(scope[-1])
                # builder = ir.IRBuilder(func.entryBlock)
                v = builder.alloca(ir.IntType(32), name=var['id'])
                v.align = 4
                vars.insert(0, Var(var['id'], v, scope[-1]))
            symbols_table.remove(var)
    
    if node.__str__() == 'declaracao_funcao':
        type = node.children[0]
        id = node.children[1].children[0].children[0]
        func = get_symbol(id, type='function')
        if type == 'inteiro':
            ftype = ir.IntType(32)
        elif type == 'flutuante':
            ftype = ir.FloatType()
        else:
            ftype = ir.VoidType()

        params = ()
        for p in func['params']:
            if p['data_type'] == 'inteiro':
                params += (ir.IntType(32),)
            elif p['data_type'] == 'flutuante':
                params += (ir.FloatType(),)
            else:
                params += (ir.VoidType(),)

        t_func = ir.FunctionType(ftype, params)
        f = ir.Function(module, t_func, id)
        entryBlock = f.append_basic_block('entry')
        endBasicBlock = f.append_basic_block('exit')
        functions.append(Function(id, f, entryBlock, endBasicBlock))
        builder = ir.IRBuilder(entryBlock)
        scope.append(id)

    if node.__str__() == 'se':
        if not isinstance(node, Node):
            return
        func = get_function(scope[-1])
        iftrue = func.func.append_basic_block('iftrue' + str(node.id))
        if len(node.children) > 5:
            iffalse = func.func.append_basic_block('iffalse' + str(node.id))
        ifend = func.func.append_basic_block('ifend' + str(node.id))

        ifs.append(Se('se'+str(node.id), iftrue, iffalse, ifend))
        scope.append('se' + str(node.id))

        expressao = node.children[1]
        op = expressao.children[1]

        if expressao.children[0].name == 'ID':
            v1 = get_var(expressao.children[0].children[0])
            v1_cmp = builder.load(v1.var, 'v1_cmp', align=4)
        elif expressao.children[0].name == 'NUM_INT':
            v1_cmp = ir.Constant(ir.IntType(32), int(expressao.children[0].children[0]))
        elif expressao.children[0].name == 'NUM_FLUT':
            v1_cmp = ir.Constant(ir.FloatType(), float(expressao.children[0].children[0]))

        if expressao.children[2].name == 'ID':
            v2 = get_var(expressao.children[2].children[0])
            v2_cmp = builder.load(v2.var, 'v2_cmp', align=4)
        elif expressao.children[2].name == 'NUM_INT':
            v2_cmp = ir.Constant(ir.IntType(32), int(expressao.children[2].children[0]))
        elif expressao.children[2].name == 'NUM_FLUT':
            v2_cmp = ir.Constant(ir.FloatType(), float(expressao.children[2].children[0]))

        if_test = builder.icmp_signed(op, v1_cmp, v2_cmp)
        if len(node.children) > 5:
            builder.cbranch(if_test, iftrue, iffalse)
        else:
            builder.cbranch(if_test, iftrue, ifend)

    if node.__str__() == 'então':
        se = get_if(scope[-1])
        builder.position_at_end(se.iftrue)
    
    if node.__str__() == 'senão':
        se = get_if(scope[-1])
        builder.position_at_end(se.iffalse)

    if node.__str__() == 'atribuicao':
        exp = build_expressao(node.children[2], builder)
        var = get_var(node.children[0].children[0]).var
        builder.store(exp, var)
        return

    if node.__str__() == 'fim':
        for v in vars:
            if v.scope == scope[-1]:
                vars.remove(v)
        scope.pop()

        # if len(scope) == 2:
        #     builder.branch(get_function(scope[1]).exitBlock)

        if len(scope) > 1:
            builder.position_at_end(get_function(scope[1]).entryBlock)
    
    if node.__str__() == 'repita':
        if isinstance(node, Node):
            id = 'repita'+str(node.id)
            repita = builder.append_basic_block(id)
            repitaend = builder.append_basic_block(id+"end")
            b = builder.branch(repita)
            builder.position_at_end(repita)
            repeat.append(Repita(id, repita, repitaend, node.children[3]))
    
    if node.__str__() == 'até':
        repita = repeat.pop()
        iftest = build_expressao(repita.expressao, builder)
        builder.cbranch(iftest, repita.block, repita.end)
        builder.position_at_end(repita.end)

    if node.__str__() == 'retorna':
        if not isinstance(node, Node):
            return
        val = build_expressao(node.children[2], builder)
        builder.ret(val)
              
    if isinstance(node, Node):
        for child in node.children:
            percorreArvore(child, scope, builder)

def build_expressao(node, builder):
    if node.name == 'ID':
        var = get_var(node.children[0]).var
        return builder.load(var, "")
    if node.name == 'NUM_INT':
        return ir.Constant(ir.IntType(32), int(node.children[0]))
    if node.name == 'NUM_FLUT':
        return ir.Constant(ir.FloatType(), float(node.children[0]))
    if node.name == 'expressao_aditiva':
        return builder.add(build_expressao(node.children[0], builder), build_expressao(node.children[2], builder))
    if node.name == 'expressao_multiplicativa':
        return builder.mul(build_expressao(node.children[0], builder), build_expressao(node.children[2], builder))
    if node.name == 'expressao_simples':
        op = node.children[1]
        if op == '=':
            op = '=='
        a_cmp = build_expressao(node.children[0], builder)
        b_cmp = build_expressao(node.children[2], builder)
        return builder.icmp_signed(op, a_cmp, b_cmp)
    if node.name == 'fator':
        return build_expressao(node.children[1], builder)
    
    # for child in node.children:
    #     if isinstance(child, Node):
    #         return expressao(child, builder)

def search(root: Node, node_name: str) -> list:
    queue = [root]
    res = []
    while len(queue) > 0:
        next = queue.pop(0)
        if next.__str__() == node_name:
            res.append(next)
        if isinstance(next, Node):
            for child in next.children:
                queue.append(child)
    return res

def get_symbol(id, scope=None, type=None):
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

def get_function(id) -> Function:
    for f in functions:
        if(f.id == id):
            return f

def get_if(id) -> Se:
    for i in ifs:
        if(i.id == id):
            return i

def get_var(id) -> Var:
    for v in vars:
        if v.id == id:
            return v

percorreArvore(root)

arquivo = open('code.ll', 'w')
arquivo.write(str(module))
arquivo.close()