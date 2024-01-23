from flask import Flask, render_template, jsonify, request

#import networkx as nx
#from matplotlib import pyplot as plt

from CalCoolUs.preprocess import ShuntingYard
#from CalCoolUs.ops.const import Const
from CalCoolUs.preprocess import ASTGraph
from CalCoolUs.numerical_engine import Numerical_Engine

app = Flask(__name__)
myshunt = ShuntingYard()

#shuntres = myshunt.getPostfix("(x+1)*(x+3)*(x+4)")
#shuntres = myshunt.getPostfix("x*x")



myASTGraph = ASTGraph()
#nx.draw_networkx(graph, with_labels=True)
#plt.savefig("fig.png")







@app.route('/numerical_engine/endpoint', methods=['POST'])
def numerical_engine_endpoint():
    input_json = request.get_json(force=True) 
    # force=True, above, is necessary if another developer 
    # forgot to set the MIME type to 'application/json'
    x=float(eval(input_json['x']))
    equation=input_json['equation']
    print("----\nGot Request:")
    print('Equation:', input_json['equation'])
    print("At x=", x, type(x))
    print("----")
    shuntres = myshunt.getPostfix(equation)
    graph = myASTGraph.getAST(shuntres)
    ne = Numerical_Engine(graph, myASTGraph)
    ans = ne.solve(x)
    ans_prime = ne.differentiate(x)
    dictToReturn = {'f': str(ans), 'f_prime':str(ans_prime)}
    return jsonify(dictToReturn)

@app.route('/')
def home():
   return render_template('index.html')
if __name__ == '__main__':
   app.run(debug=True)
