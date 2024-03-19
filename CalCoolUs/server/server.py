import os
from dotenv import load_dotenv
load_dotenv()

from flask import Flask, render_template, jsonify, request


from CalCoolUs.preprocess import ShuntingYard
from CalCoolUs.preprocess import ASTGraph
from CalCoolUs.numerical_engine import Numerical_Engine

myASTGraph = ASTGraph()
myshunt = ShuntingYard()
app = Flask(__name__)


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

if os.getenv("FLASK_ENV") == "PROD":
    try:
        app.run(host=os.getenv("PROD_HOST"), port=int(os.getenv("PROD_PORT")))
    except:
        raise ValueError("The env file must have PROD_HOST and PROD_PORT.")
elif os.getenv("FLASK_ENV") == "DEV":
    try:
        print(os.getenv("DEV_HOST"))
        app.run(debug=True, host=os.getenv("DEV_HOST"), port=int(os.getenv("DEV_PORT")))    
    except:
        raise ValueError("The env file must have DEV_HOST and DEV_PORT.")
else:
    raise ValueError("FLASK_ENV not set to DEV or PROD")


