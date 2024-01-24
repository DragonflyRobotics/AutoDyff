import networkx as nx
from CalCoolUs.ops.const import Const
from CalCoolUs.preprocess import ASTGraph
from CalCoolUs.log_init import MainLogger


class Numerical_Engine:
    def __init__(self, graph, ast) -> None:
        self.graph = graph
        self.ast = ast
        self.last_node = self.ast.getFinalNode(self.graph)
        root_log = MainLogger()
        self.log = root_log.StandardLogger("NumericalEngine")  # Create a script specific logging instance



    def solve(self, x, node=None):
        self.log.info(f"Started numerical solve with head at {x}...")
        assert type(x) == int or type(x) == float
        if node == None:
            node = self.last_node
        self.log.info(f"Working on: {node}")
        if node == "x":
            self.graph.nodes(data=True)['x']['Op'].numerical_value = x
            #print(f"x={x}")
            return x
        elif type(self.graph.nodes(data=True)[node]["Op"]) == Const:
            a = self.graph.nodes(data=True)[node]["Op"].numerical_value
            #print(f"{node}={a}")
            return a
        else:
            if self.graph.nodes(data=True)[node]["Op"].unary:
                neighbors = list(nx.DiGraph.reverse(self.graph, copy=False).neighbors(node))
                self.graph.nodes(data=True)[node]["Op"].numerical_value = self.graph.nodes(data=True)[node]["Op"](self.solve(x, neighbors[0]))
                a = self.graph.nodes(data=True)[node]["Op"].numerical_value
                self.log.info(f"{node}={a}")

            else:
                neighbors = list(nx.DiGraph.reverse(self.graph, copy=False).neighbors(node))
                self.graph.nodes(data=True)[node]["Op"].numerical_value = self.graph.nodes(data=True)[node]["Op"](self.solve(x, neighbors[0]), self.solve(x, neighbors[1]))
                a = self.graph.nodes(data=True)[node]["Op"].numerical_value
                self.log.info(f"{node}={a}")
            return a

    def differentiate(self, x, node=None):
        self.log.info(f"Started differentiation with head at {x}...")
        assert type(x) == int or type(x) == float
        if node == None:
            node = self.last_node
        # temp = self.graph.nodes(data=True)[node]["Op"].numerical_value
        # self.log.info(f"Working on: {node}={temp}")
        if node == "x":
            self.log.info(f"x'={1}")
            return 1
        elif type(self.graph.nodes(data=True)[node]["Op"]) == Const:
            self.log.info(f"{node}'={0}")
            return 0
        else:
            if self.graph.nodes(data=True)[node]["Op"].unary:
                neighbors = list(nx.DiGraph.reverse(self.graph, copy=False).neighbors(node))
                #a = graph.nodes(data=True)[node]["Op"].getDerivative(differentiate(neighbors[0]), differentiate(neighbors[1]), graph.nodes(data=True)[neighbors[0]]["Op"].numerical_value, graph.nodes(data=True)[neighbors[1]]["Op"].numerical_value)
                a = self.graph.nodes(data=True)[node]["Op"].getDerivative(self.differentiate(x, neighbors[0]), self.solve(x, neighbors[0]))

                self.log.info(f"{node}'={a}")

            else:
                neighbors = list(nx.DiGraph.reverse(self.graph, copy=False).neighbors(node))
                #a = graph.nodes(data=True)[node]["Op"].getDerivative(differentiate(neighbors[0]), differentiate(neighbors[1]), graph.nodes(data=True)[neighbors[0]]["Op"].numerical_value, graph.nodes(data=True)[neighbors[1]]["Op"].numerical_value)
                a = self.graph.nodes(data=True)[node]["Op"].getDerivative(self.differentiate(x, neighbors[0]), self.differentiate(x, neighbors[1]), self.solve(x, neighbors[0]), self.solve(x, neighbors[1]))

                self.log.info(f"{node}'={a}")
            return a
