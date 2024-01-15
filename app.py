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
        nama_mahasiswa = request.form['nama_mahasiswa']
        nim = request.form['nim']
        ipk_kum = float(request.form['ipk_kum'])
        if ipk_kum >= 3.0:
            prediction = 'Lulus Tepat Waktu'
        elif ipk_kum <= 2.9:
            prediction = 'Tidak lulus Tepat Waktu'
        else:
            prediction = 'Unknown'

        return render_template('output.html', nama_mahasiswa=nama_mahasiswa, nim=nim, ipk_kum=ipk_kum, prediction=prediction)
        

def students_pred(ipk_kum):
    model = pickle.load(open('model.pkl','rb'))

    result = model.predict([[ipk_kum]])

    if result[0] == 1:
        pred = 'Lulus Tepat Waktu'
    else:
        pred = 'Tidak lulus Waktu'

    return pred

if __name__ == "__main__":
    app.run(debug=True)
