import tree
from parser import root
from graphviz import Digraph

tree.prune(root)
dot = Digraph()
tree.make_graph(dot, root)
dot.render('graph-output/arvore-sintatica-poda.gv', view=False)