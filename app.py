from flask import Flask, request
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy
from sklearn import linear_model # Le modèle linéaire
from sklearn import datasets
from sklearn.metrics import mean_squared_error, r2_score # Métriques d'évaluation

import seaborn as sns

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/predict', methods = ['POST'])
def showPanda():
    data = request.json
    file = pd.read_excel('./results.csv')

    return file.to_json(orient='index')


if __name__ == '__main__':
    app.run()
