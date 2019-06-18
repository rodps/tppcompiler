from graphviz import Digraph

class Node:
    def __init__(self, name, children=[]):
        self.name = name
        self.children = children

    def __str__(self):
        return self.name


def print_tree(root):
    if(root == None):
        return
    print("pai: ", root)
    for child in root.children:
            print(child)
    for child in root.children:
        if(isinstance(child, Node)):
            print_tree(child)

def make_graph(dot, parent, id=0):
    if(id == 0):
        dot.node(str(id), parent.name)
    c = id
    for child in parent.children:
        c += 1
        if(isinstance(child, Node)):
            dot.node(str(c), child.name)
        else:
            dot.node(str(c), child)
        dot.edge(str(id), str(c))
        if(isinstance(child, Node)):
            c = make_graph(dot, child, c)
    return c + 1

def prune(node):
    if not isinstance(node, Node):
        return node
    if node.name in ['ID', 'NUM_INT', 'NUM_FLUT', 'NUM_NOTACAO']:
        return node
    if len(node.children) == 0:
        return node
    
    if len(node.children) > 1:
        i = 0
        while i < len(node.children):
            node.children[i] = prune(node.children[i])
            if node.children[i] in [':', ',']:
                node.children.pop(i)
            else: i += 1
        return node
    else:
        return prune(node.children[0])