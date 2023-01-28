import pickle
import pandas as pd
import numpy as np
from flask import Flask, render_template, request
from sklearn.linear_model import LinearRegression

filename = 'finalized_model.sav'
loaded_model = pickle.load(open(filename, 'rb'))


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html") 


@app.route("/model", methods=['post','get'])
def model():
    num = np.int64(request.form['height'])
    result = loaded_model.predict([[num]])
    return f"<h1>Your Height: {num} & predicted Weight <label style='color:red'>{result[0]}</label></h1>"   

if __name__ == '__main__':
    app.run(debug=True)

