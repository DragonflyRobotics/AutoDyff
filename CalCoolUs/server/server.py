import os
from dotenv import load_dotenv
load_dotenv()

from flask import Flask, render_template, jsonify, request

from CalCoolUs.preprocess import ShuntingYard
from CalCoolUs.preprocess import ASTGraph
from CalCoolUs.numerical_engine import Numerical_Engine


class NumericalEngineEndpoint(object):
    def __init__(self):
        self.myshunt = ShuntingYard()
        self.myASTGraph = ASTGraph()
    def __call__(self): 
        input_json = request.get_json(force=True) 
        # force=True, above, is necessary if another developer 
        # forgot to set the MIME type to 'application/json'
        x=float(eval(input_json['x']))
        equation=input_json['equation']
        print("----\nGot Request:")
        print('Equation:', input_json['equation'])
        print("At x=", x, type(x))
        print("----")
        shuntres = self.myshunt.getPostfix(equation)
        graph = self.myASTGraph.getAST(shuntres)
        ne = Numerical_Engine(graph, self.myASTGraph)
        ans = ne.solve(x)
        ans_prime = ne.differentiate(x)
        dictToReturn = {'f': str(ans), 'f_prime':str(ans_prime)}
        return jsonify(dictToReturn)
   

class HomeEndpoint(object):
    def __init__(self):
        pass
    def __call__(self):
        return render_template('index.html')

class FlaskWrapper(object):
    app = None
    def __init__(self):
        self.app = Flask(__name__)
        self.app.app_context().push()
        print(__name__)
   
    def run(self):
        if os.getenv("FLASK_ENV") == "PROD":
            self.app.run(host=os.getenv("PROD_HOST"), port=int(os.getenv("PROD_PORT")))
        elif os.getenv("FLASK_ENV") == "DEV":
            self.app.run(debug=True, host=os.getenv("DEV_HOST"), port=int(os.getenv("DEV_PORT")))
        else:
            raise ValueError("FLASK_ENV not set to DEV or PROD")

    def add_endpoint(self, url, endpoint_name, action_class, handler=None, methods=['GET']):
        self.app.add_url_rule(url, endpoint_name, action_class(), methods=methods)


if __name__ == "__main__":
    fe = FlaskWrapper()
    fe.add_endpoint('/', 'home', HomeEndpoint(), methods=['GET'])
    fe.add_endpoint('/numerical_engine', 'numerical_engine', NumericalEngineEndpoint(), methods=['POST'])
    fe.run()
