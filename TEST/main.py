import base64
import io

from flask import Flask, render_template, jsonify, request
import cv2
import numpy as np

app = Flask(__name__)

# Load an example image using OpenCV

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)


