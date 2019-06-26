from semantic import symbols_table, root
from llvmlite import ir
from tree import Node

module = ir.Module('modulo.bc')
functions = []
vars = []

class Function():
    def __init__(self, id: str, func: ir.Function, entryBlock: ir.Block, exitBlock: ir.Block):
        self.id = id
        self.func = func
        self.entryBlock = entryBlock
        self.exitBlock = exitBlock

class Var():
    def __init__(self, id, var, block):
        self.id = id
        self.var = var
        self.block = block

def percorreArvore(node: Node, scope=None):

    if node.__str__() == 'declaracao_variaveis':
        ids = search(node.children[1], 'ID')
        for id in ids:
            var = get_symbol(id.children[0], type='var')
            if var['scope'] == 'programa':
                v = ir.GlobalVariable(module, ir.IntType(32), var['id'])
                v.initializer = ir.Constant(ir.IntType(32), 0)
                v.linkage = 'common'
                v.align = 4
            else:
                func = get_function(scope)
                builder = ir.IRBuilder(func.entryBlock)
                v = builder.alloca(ir.IntType(32), name=var['id'])
                v.align = 4
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
        scope = id

    if node.__str__() == 'se':
        func = get_function(scope)
        iftrue = func.func.append_basic_block('iftrue')
        if len(node.children) > 5:
            iffalse = func.func.append_basic_block('iffalse')
        ifend = func.func.append_basic_block('ifend')

        op = node.children[1]
        if node.children[0].name == 'ID':
            v = get_var(node.children[0].children[0])



    if isinstance(node, Node):
        for child in node.children:
            percorreArvore(child, scope)


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

def get_var(id) -> Var:
    for v in vars:
        if v.id == id:
            return v

percorreArvore(root)

arquivo = open('code.ll', 'w')
arquivo.write(str(module))
arquivo.close()