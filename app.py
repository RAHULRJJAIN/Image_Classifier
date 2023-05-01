from flask import Flask, request, jsonify, render_template
import numpy as np
import joblib
app= Flask(__name__)

model= joblib.load(open("saved_model.pkl", "rb"))

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/predict", methods=["POST"])
def predict():
    imagefile= request.files['imagefile']
    image_path = "./images/" + imagefile.filename
    imagefile.save(image_path)


    return render_template("index.html" , prediction = "Image classification") 

if __name__== "__main__":
    app.run(debug=True)