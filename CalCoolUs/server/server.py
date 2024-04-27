import os
import numpy as np
import cv2, io, base64
from dotenv import load_dotenv
load_dotenv()

from flask import Flask, render_template, jsonify, request


from CalCoolUs.preprocess import ShuntingYard
from CalCoolUs.preprocess import ASTGraph
from CalCoolUs.numerical_engine import Numerical_Engine


myASTGraph = ASTGraph()
myshunt = ShuntingYard()
app = Flask(__name__)
image = np.zeros((300, 300, 3), dtype="uint8")

def process_latex(equation):
    return str(equation).replace("**", "^")

@app.route('/get_image', methods=['GET'])
def get_image():
    _, img_encoded = cv2.imencode('.jpg', image)
    img_bytes = io.BytesIO(img_encoded).getvalue()
    img_str = base64.b64encode(img_bytes).decode('utf-8')
    return jsonify({'image': img_str})


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

@app.route('/numerical_engine/endpoint_latex', methods=['POST'])
def numerical_engine_endpoint_latex():
    #make image blue
    global image
    image = np.zeros((30, 30, 3), dtype="uint8")
    input_json = request.get_json(force=True) 
    # force=True, above, is necessary if another developer 
    # forgot to set the MIME type to 'application/json'
    x=float(eval(input_json['x']))
    equation=input_json['equation']
    print("----\nGot Request:")
    print('Equation:', input_json['equation'])
    print("At x=", x, type(x))
    print("----")
    equation = myshunt.tokenize_latex(equation)
    #equation = process_latex(latex2sympy(equation)) #LatexNodes2Text().latex_to_text(equation)
    print(f"Processed Equation: {equation}")
    shuntres = myshunt.getPostfixLatex(equation)
    graph = myASTGraph.getAST(shuntres)
    image = myASTGraph.get_image_array(graph)
    ne = Numerical_Engine(graph, myASTGraph)
    try:
        ans = ne.solve(x)
    except Exception as e:
        print(f"!!!!!!!{e}")
        print(f"Exception type: {type(e).__name__}, message: {e}")
        ans = str(e)
    try:
        ans_prime = ne.differentiate(x)
    except Exception as e:
        print(f"!!!!!!!{e}")
        ans_prime = str(e)
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


