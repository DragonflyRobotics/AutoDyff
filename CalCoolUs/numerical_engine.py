import networkx as nx # Importing networkx for graph operations
from CalCoolUs.ops.const import Const # Importing the Const class from the const.py file
from CalCoolUs.preprocess import ASTGraph # Importing the ASTGraph class from the preprocess.py file
from CalCoolUs.log_init import MainLogger # Importing the MainLogger class from the log_init.py file


class Numerical_Engine:
    def __init__(self, graph, ast) -> None:
        self.graph = graph
        self.ast = ast
        self.last_node = self.ast.getFinalNode(self.graph) # Getting the last node of the AST
        root_log = MainLogger() # Creating a MainLogger instance
        self.log = root_log.StandardLogger("NumericalEngine")  # Create a script specific logging instance



    def solve(self, x, node=None): # Function to solve the expression
        self.log.info(f"Started numerical solve with head at {x}...")
        assert type(x) == int or type(x) == float
        if node == None: # If the node is not provided, set it to the last node
            node = self.last_node # Setting the node to the last node
        self.log.info(f"Working on: {node}")
        if "x" in node: # If the node is an x node, set the value of x to the node
            self.graph.nodes(data=True)['x']['Op'].numerical_value = x # Setting the value of x to the node
            #print(f"x={x}")
            return x # Returning the value of x
        elif type(self.graph.nodes(data=True)[node]["Op"]) == Const: # If the node is a constant, return the value of the constant
            a = self.graph.nodes(data=True)[node]["Op"].numerical_value # Getting the value of the constant
            #print(f"{node}={a}")
            return a # Returning the value of the constant
        else:
            if self.graph.nodes(data=True)[node]["Op"].unary: # If the node is a unary operator
                neighbors = list(nx.DiGraph.reverse(self.graph, copy=False).neighbors(node)) # Getting the neighbors of the node
                self.graph.nodes(data=True)[node]["Op"].numerical_value = self.graph.nodes(data=True)[node]["Op"](self.solve(x, neighbors[0])) # Setting the value of the node to the result of the unary operation
                a = self.graph.nodes(data=True)[node]["Op"].numerical_value # Getting the value of the node
                self.log.info(f"{node}={a}") # Logging the value of the node

            else: # If the node is a binary operator
                neighbors = list(nx.DiGraph.reverse(self.graph, copy=False).neighbors(node)) # Getting the neighbors of the node
                self.graph.nodes(data=True)[node]["Op"].numerical_value = self.graph.nodes(data=True)[node]["Op"](self.solve(x, neighbors[0]), self.solve(x, neighbors[1])) # Setting the value of the node to the result of the binary operation
                a = self.graph.nodes(data=True)[node]["Op"].numerical_value # Getting the value of the node
                self.log.info(f"{node}={a}") # Logging the value of the node
            return a # Returning the value of the node

    def differentiate(self, x, node=None): # Function to differentiate the expression
        self.log.info(f"Started differentiation with head at {x}...") # Logging the start of the differentiation
        assert type(x) == int or type(x) == float # Asserting that x is an integer or a float
        if node == None: # If the node is not provided, set it to the last node
            node = self.last_node # Setting the node to the last node
        # temp = self.graph.nodes(data=True)[node]["Op"].numerical_value
        # self.log.info(f"Working on: {node}={temp}")
        if 'x' in node: # If the node is an x node, return 1
            self.log.info(f"x'={1}") # Logging the derivative of x
            return 1 # Returning 1
        elif type(self.graph.nodes(data=True)[node]["Op"]) == Const: # If the node is a constant, return 0
            self.log.info(f"{node}'={0}") # Logging the derivative of the constant
            return 0 # Returning 0
        else: # If the node is an operator
            if self.graph.nodes(data=True)[node]["Op"].unary: # If the node is a unary operator
                neighbors = list(nx.DiGraph.reverse(self.graph, copy=False).neighbors(node)) # Getting the neighbors of the node
                #a = graph.nodes(data=True)[node]["Op"].getDerivative(differentiate(neighbors[0]), differentiate(neighbors[1]), graph.nodes(data=True)[neighbors[0]]["Op"].numerical_value, graph.nodes(data=True)[neighbors[1]]["Op"].numerical_value)
                a = self.graph.nodes(data=True)[node]["Op"].getDerivative(self.differentiate(x, neighbors[0]), self.solve(x, neighbors[0]))     # Getting the derivative of the unary operator
                self.log.info(f"{node}'={a}") # Logging the derivative of the unary operator

            else: # If the node is a binary operator
                neighbors = list(nx.DiGraph.reverse(self.graph, copy=False).neighbors(node)) # Getting the neighbors of the node
                #a = graph.nodes(data=True)[node]["Op"].getDerivative(differentiate(neighbors[0]), differentiate(neighbors[1]), graph.nodes(data=True)[neighbors[0]]["Op"].numerical_value, graph.nodes(data=True)[neighbors[1]]["Op"].numerical_value)
                a = self.graph.nodes(data=True)[node]["Op"].getDerivative(self.differentiate(x, neighbors[0]), self.differentiate(x, neighbors[1]), self.solve(x, neighbors[0]), self.solve(x, neighbors[1])) # Getting the derivative of the binary operator

                self.log.info(f"{node}'={a}")
            return a # Returning the derivative of the node
