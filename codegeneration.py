from semantic import symbols_table, root
from llvmlite import ir, binding
from tree import Node

module = ir.Module('code.bc')
module.triple = binding.get_default_triple()

# binding.initialize()
# binding.initialize_native_target()
# binding.initialize_native_asmprinter()

# target = binding.Target.from_triple("x86_64-pc-linux-gnu")
# target_machine = target.create_target_machine()

# backing_mod = binding.parse_assembly("")
# engine = binding.create_mcjit_compiler(backing_mod, target_machine)

ftype = ir.FunctionType(ir.IntType(32), [])
leiaInteiro = ir.Function(module, ftype, "leiaInteiro")

ftype = ir.FunctionType(ir.FloatType(), [])
leiaFlutuante = ir.Function(module, ftype, "leiaFlutuante")

ftype = ir.FunctionType(ir.VoidType(), [ir.IntType(32)])
escrevaInteiro = ir.Function(module, ftype, "escrevaInteiro")

ftype = ir.FunctionType(ir.VoidType(), [ir.FloatType()])
escrevaFlutuante = ir.Function(module, ftype, "escrevaFlutuante")

functions = []
ifs = []
vars = []
repeat = []

class Function():
    def __init__(self, id: str, func: ir.Function, entryBlock: ir.Block, exitBlock: ir.Block, retorno):
        self.id = id
        self.func = func
        self.entryBlock = entryBlock
        self.exitBlock = exitBlock
        self.retorno = retorno

class Se():
    def __init__(self, id, iftrue, iffalse, ifend):
        self.id = id
        self.iftrue = iftrue
        self.iffalse = iffalse
        self.ifend = ifend

class Var():
    def __init__(self, id, var, scope, type):
        self.id = id
        self.var = var
        self.scope = scope
        self.type = type

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
                if var['data_type'] == 'inteiro':
                    v = ir.GlobalVariable(module, ir.IntType(32), var['id'])
                    v.initializer = ir.Constant(ir.IntType(32), 0)
                    v.linkage = 'common'
                    v.align = 4
                    vars.insert(0, Var(var['id'], v, scope[-1], ir.IntType(32)))
                else:
                    v = ir.GlobalVariable(module, ir.FloatType(), var['id'])
                    v.initializer = ir.Constant(ir.FloatType(), 0)
                    v.linkage = 'common'
                    v.align = 4
                    vars.insert(0, Var(var['id'], v, scope[-1], ir.FloatType()))
            else:
                if var['data_type'] == 'inteiro':
                    v = builder.alloca(ir.IntType(32), name=var['id'])
                    v.align = 4
                    vars.insert(0, Var(var['id'], v, scope[-1], ir.IntType(32)))
                else:
                    v = builder.alloca(ir.FloatType(), name=var['id'])
                    v.align = 4
                    vars.insert(0, Var(var['id'], v, scope[-1], ir.FloatType()))
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
        if id == 'principal':
            id = 'main'
        f = ir.Function(module, t_func, id)

        entryBlock = f.append_basic_block('entry')
        endBasicBlock = f.append_basic_block('exit')
        
        builder = ir.IRBuilder(entryBlock)
        Zero = ir.Constant(ir.IntType(32), 0)
        returnVal = builder.alloca(ir.IntType(32), name='retorno')
        builder.store(Zero, returnVal)

        for i in range(len(func['params'])):
            if func['params'][i]['data_type'] == 'inteiro':
                v = builder.alloca(ir.IntType(32), name=func['params'][i]['id'])
                v.align = 4
            else:
                v = builder.alloca(ir.FloatType(), name=func['params'][i]['id'])
                v.align = 4
            builder.store(f.args[i], v)
            vars.insert(0, Var(func['params'][i]['id'], v, id, ir.IntType(32)))

        functions.append(Function(id, f, entryBlock, endBasicBlock, returnVal))

        scope.append(id)
    
    if node.__str__() == 'chamada_funcao':
        func = chamada_funcao(node, builder)
        builder.call(func[0], func[1])

    if node.__str__() == 'se':
        if not isinstance(node, Node):
            return
        func = get_function(scope[1])
        iftrue = func.func.append_basic_block('iftrue' + str(node.id))
        if len(node.children) > 5:
            iffalse = func.func.append_basic_block('iffalse' + str(node.id))
        else:
            iffalse = None
        ifend = func.func.append_basic_block('ifend' + str(node.id))

        ifs.append(Se('se'+str(node.id), iftrue, iffalse, ifend))
        scope.append('se' + str(node.id))

        expressao = node.children[1]
        # op = expressao.children[1]

        # if expressao.children[0].name == 'ID':
        #     v1 = get_var(expressao.children[0].children[0])
        #     v1_cmp = builder.load(v1.var, align=4)
        # elif expressao.children[0].name == 'NUM_INT':
        #     v1_cmp = ir.Constant(ir.IntType(32), int(expressao.children[0].children[0]))
        # elif expressao.children[0].name == 'NUM_FLUT':
        #     v1_cmp = ir.Constant(ir.FloatType(), float(expressao.children[0].children[0]))

        # if expressao.children[2].name == 'ID':
        #     v2 = get_var(expressao.children[2].children[0])
        #     v2_cmp = builder.load(v2.var, 'v2_cmp', align=4)
        # elif expressao.children[2].name == 'NUM_INT':
        #     v2_cmp = ir.Constant(ir.IntType(32), int(expressao.children[2].children[0]))
        # elif expressao.children[2].name == 'NUM_FLUT':
        #     v2_cmp = ir.Constant(ir.FloatType(), float(expressao.children[2].children[0]))

        # if_test = builder.icmp_signed(op, v1_cmp, v2_cmp)
        if_test = build_expressao(expressao, builder)
        if len(node.children) > 5:
            builder.cbranch(if_test, iftrue, iffalse)
        else:
            builder.cbranch(if_test, iftrue, ifend)
        builder.position_at_end(iftrue)

    # if node.__str__() == 'então':
    #     se = get_if(scope[-1])
    #     builder.position_at_end(se.iftrue)
    
    if node.__str__() == 'senão':
        se = get_if(scope[-1])
        if not builder.block.is_terminated:
            builder.branch(se.ifend)
        builder.position_at_end(se.iffalse)

    if node.__str__() == 'atribuicao':
        exp = build_expressao(node.children[2], builder)
        var = get_var(node.children[0].children[0])
        builder.store(exp, var.var)
        return

    if node.__str__() == 'fim':
        remove = []
        for v in vars:
            if v.scope == scope[-1]:
                remove.append(v)
        for v in remove:
            vars.remove(v)
        if len(scope) > 2:
            ifend = get_if(scope[-1]).ifend
            if not builder.block.is_terminated:
                builder.branch(ifend)
            builder.position_at_end(ifend)
        else:
            func = get_function(scope[1])
            if not builder.block.is_terminated:    
                builder.branch(func.exitBlock)
            builder.position_at_end(func.exitBlock)
            builder.ret(builder.load(func.retorno, ""))
        scope.pop()

        # if len(scope) == 2:
        #     builder.branch(get_function(scope[1]).exitBlock)

        # if len(scope) > 1:
        #     builder.position_at_end(get_function(scope[1]).entryBlock)
    
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
        builder.cbranch(iftest, repita.end, repita.block)
        builder.position_at_end(repita.end)

    if node.__str__() == 'retorna':
        if not isinstance(node, Node):
            return
        val = build_expressao(node.children[2], builder)
        # builder.ret(val)
        func = get_function(scope[1])
        builder.store(val, func.retorno)
        # if not builder.block.is_terminated:
        builder.branch(func.exitBlock)
        return

    if node.__str__() == 'leia':
        if not isinstance(node, Node):
            return
        v = get_var(node.children[2].children[0])
        if v.type == ir.IntType(32):
            call = builder.call(leiaInteiro, [])
        if v.type == ir.FloatType():
            call = builder.call(leiaFlutuante, [])
        builder.store(call, v.var)

    if node.__str__() == 'escreva':
        if not isinstance(node, Node):
            return
        v = build_expressao(node.children[2], builder)
        if v.type == ir.IntType(32):
            builder.call(escrevaInteiro, [v])
        if v.type == ir.FloatType():
            builder.call(escrevaFlutuante, [v])
        return

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
    if node.name == 'chamada_funcao':
        func = chamada_funcao(node, builder)
        params = func[0].args
        args = func[1]
        for i in range(len(params)):
            if params[i].type == ir.FloatType() and args[i].type == ir.IntType(32):
                args[i] = builder.sitofp(args[i], ir.FloatType())
            if params[i].type == ir.IntType(32) and args[i].type == ir.FloatType():
                args[i] = builder.fptosi(args[i], ir.IntType(32))
        return builder.call(func[0], args)
    if node.name == 'expressao_aditiva':
        if node.children[1] == '+':
            return builder.add(build_expressao(node.children[0], builder), build_expressao(node.children[2], builder))
        if node.children[1] == '-':
            return builder.sub(build_expressao(node.children[0], builder), build_expressao(node.children[2], builder))
    if node.name == 'expressao_multiplicativa':
        return builder.mul(build_expressao(node.children[0], builder), build_expressao(node.children[2], builder))
    if node.name == 'expressao_simples':
        op = node.children[1]
        if op == '=':
            op = '=='
        a_cmp = build_expressao(node.children[0], builder)
        b_cmp = build_expressao(node.children[2], builder)
        return builder.icmp_signed(op, a_cmp, b_cmp)
    if node.name == 'expressao_logica':
        op = node.children[1]
        a_cmp = build_expressao(node.children[0], builder)
        b_cmp = build_expressao(node.children[2], builder)
        if op == '&&':
            return builder.and_(a_cmp, b_cmp)
        if op == '||':
            return builder.or_(a_cmp, b_cmp)
    if node.name == 'expressao_unaria':
        op = node.children[0]
        value = build_expressao(node.children[1], builder)
        if op == '!':
            return builder.not_(value)
    if node.name == 'fator':
        return build_expressao(node.children[1], builder)
    
    print('none', node.name)
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

def chamada_funcao(node, builder):
    func = get_function(node.children[0].children[0])
    args = []
    queue = [node.children[2]]
    if node.children[2].name == 'lista_argumentos':
        lista_args = node.children[2]
        next = lista_args
        while True:
            for arg in lista_args.children:
                if arg.name == 'lista_argumentos':
                    next = arg
                else:
                    args.append(build_expressao(arg, builder))
            if lista_args != next:
                lista_args = next
            else:
                break
    else:
        arg = node.children[2]
        args.append(build_expressao(arg, builder))
    # while len(queue) > 0:
    #     next = queue.pop(0)
    #     arg = build_expressao(next, builder)
    #     if arg != None:
    #         args.append(arg)
    #     for child in next.children:
    #         if isinstance(child, Node) and next.name != 'chamada_funcao':
    #             queue.append(child)
    return (func.func, args)

percorreArvore(root)

arquivo = open('code.ll', 'w')
arquivo.write(str(module))
arquivo.close()