# 🌸 Iris Flower Prediction ML Project

![Python](https://img.shields.io/badge/Python-3.13-blue)
![Flask](https://img.shields.io/badge/Flask-2.x-orange)

## Description
This project predicts the species of an Iris flower (**Setosa, Versicolor, Virginica**) based on its **sepal length, sepal width, petal length, and petal width**.  
It uses a **Random Forest Classifier** trained on the Iris dataset stored in MongoDB. The trained model is saved as `iris_model.pkl` and used in a Flask web application for live predictions.

## Project Structure

```

IRISML/
│
├── templates/
│   └── iris.html        # HTML form for prediction
├── train_model.py       # Script to train the model
├── app.py               # Flask application
├── iris_model.pkl       # Saved trained model
├── iris.csv             # Dataset (optional if using MongoDB)
├── requirements.txt     # Required Python packages

````

## Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd IRISML
````

2. Create a virtual environment and activate it:

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python -m venv venv
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Training the Model

Run the following command to train the model:

```bash
python train_model.py
```

**Sample Output:**

```
Dataset Preview:
sepal_length	sepal_width	petal_length	petal_width	species
5.1	        3.5	        1.4	        0.2	        Setosa
4.9	        3.0	        1.4	        0.2	        Setosa
4.7	        3.2	        1.3	        0.2	        Setosa
4.6	        3.1	        1.5	        0.2	        Setosa
5.0	        3.6	        1.4	        0.2	        Setosa

Model trained successfully!
Running on http://127.0.0.1:5000
```

## Running the Flask App

1. Start the Flask server:

```bash
python app.py
```

2. Open your browser and go to:

```
http://127.0.0.1:5000
```

3. Enter the sepal and petal measurements in the form and click **Predict**.

**Example Prediction Output:**

```
Predicted Species: Setosa
```
