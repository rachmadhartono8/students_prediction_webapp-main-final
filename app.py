# -*- coding: utf-8 -*-
"""
Created on Tue Feb 8 20:52:20 2022

@author: SREERAM S
"""

from flask import Flask, request, render_template, flash, jsonify
import pickle


app = Flask(__name__)
app.secret_key = "apkofriowjfkf"

@app.route("/")
def index():
    return render_template('predictiongraduation.html')
    
@app.route("/output", methods=["POST", "GET"])
def output():
    if request.method == 'POST':
        # Retrieve form data
        ipk_kum = float(request.form['ipk_kum'])
        if ipk_kum >= 3.0:
            prediction = 'Lulus Tepat Waktu'
        elif ipk_kum <= 2.9:
            prediction = 'Tidak lulus'
        else:
            prediction = 'Unknown'
        # print("error")

        return render_template('output.html', prediction=prediction)


        # return render_template('graduationscore.html', prediction=prediction)

        # try:
        #     prediction = students_pred(ipk_kum)
        #     return render_template('graduationscore.html', prediction=prediction)
        # except ValueError:
        #     return render_template('graduationscore.html')
        

# prediction-model
def students_pred(ipk_kum):
    # Load the model
    model = pickle.load(open('model.pkl','rb'))

    # Predictions
    result = model.predict([[ipk_kum]])

    # Output
    if result[0] == 1:
        pred = 'Lulus Tepat Waktu'
    else:
        pred = 'Tidak lulus Waktu'

    return pred

if __name__ == "__main__":
    app.run(debug=True)
