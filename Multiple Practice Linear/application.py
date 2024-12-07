from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np
import seaborn as sns 
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import StandardScaler

application = Flask(__name__)
app = application

## Import ridge regressor and standard scaler regressor
ridge_model = pickle.load(open(r'D:\DS\Multiple Practice Linear\models\ridge.pkl', 'rb'))
standard_scaler = pickle.load(open(r'D:\DS\Multiple Practice Linear\models\scaler.pkl', 'rb'))


 
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predictdata", methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == "POST":
        pass
    else:
        return render_template('home.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0")