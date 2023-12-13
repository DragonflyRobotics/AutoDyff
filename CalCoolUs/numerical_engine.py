import networkx as nx
from CalCoolUs.ops.const import Const
from CalCoolUs.preprocess import ASTGraph

class Numerical_Engine:
    def __init__(self, graph, ast) -> None:
        self.graph = graph
        self.ast = ast
        self.last_node = self.ast.getFinalNode(self.graph)

    def solve(self, x, node=None):
        assert type(x) == int or type(x) == float
        if node == None:
            node = self.last_node
        print(f"Working on: {node}")
        if node == "x":
            self.graph.nodes(data=True)['x']['Op'].numerical_value = x
            #print(f"x={x}")
            return x
        elif type(self.graph.nodes(data=True)[node]["Op"]) == Const:
            a = self.graph.nodes(data=True)[node]["Op"].numerical_value
            #print(f"{node}={a}")
            return a
        else:
            neighbors = list(nx.DiGraph.reverse(self.graph, copy=False).neighbors(node))
            print(neighbors)
            self.graph.nodes(data=True)[node]["Op"].numerical_value = self.graph.nodes(data=True)[node]["Op"](self.solve(x, neighbors[0]), self.solve(x, neighbors[1]))
            a = self.graph.nodes(data=True)[node]["Op"].numerical_value
            print(f"{node}={a}")
            return a

    def differentiate(self, x, node=None):
        assert type(x) == int or type(x) == float
        if node == None:
            node = self.last_node
        temp = self.graph.nodes(data=True)[node]["Op"].numerical_value
        print(f"Working on: {node}={temp}")
        if node == "x":
            print(f"x'={1}")
            return 1
        elif type(self.graph.nodes(data=True)[node]["Op"]) == Const:
            print(f"{node}'={0}")
            return 0
        else:
            neighbors = list(nx.DiGraph.reverse(self.graph, copy=False).neighbors(node))
            print(neighbors)
            #a = graph.nodes(data=True)[node]["Op"].getDerivative(differentiate(neighbors[0]), differentiate(neighbors[1]), graph.nodes(data=True)[neighbors[0]]["Op"].numerical_value, graph.nodes(data=True)[neighbors[1]]["Op"].numerical_value)
            a = self.graph.nodes(data=True)[node]["Op"].getDerivative(self.differentiate(x, neighbors[0]), self.differentiate(x, neighbors[1]), self.solve(x, neighbors[0]), self.solve(x, neighbors[1]))

            print(f"{node}'={a}")
            return a
