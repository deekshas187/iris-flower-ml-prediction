from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load("iris_model.pkl")

@app.route("/")
def home():
    return render_template("iris.html")

@app.route("/predict", methods=["POST"])
def predict():
    sepal_length = float(request.form["sepal_length"])
    sepal_width = float(request.form["sepal_width"])
    petal_length = float(request.form["petal_length"])
    petal_width = float(request.form["petal_width"])

    features = np.array([[sepal_length, sepal_width, petal_length, petal_width]])

    prediction = model.predict(features)[0]

    return render_template("iris.html", result=prediction)

if __name__ == "__main__":
    app.run(debug=True)