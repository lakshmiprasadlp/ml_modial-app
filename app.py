from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load("lr_model")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    if request.method == "POST":
        agg = int(request.form["age"])
        gender = 1 if request.form["gender"] == "male" else 0
        bmi = float(request.form["bmi"])
        childr = int(request.form["children"])
        smoker = 1 if request.form["smoker"] == "yes" else 0
        reg = int(request.form["region"])

        prediction = model.predict([[agg, gender, bmi, childr, smoker, reg]])
        result = f"Your Insurance Cost is {prediction[0]}"
        return render_template("index.html", result=result)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)

