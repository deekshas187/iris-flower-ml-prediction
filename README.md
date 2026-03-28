# 🌸 Iris Flower Prediction ML Project

![Python](https://img.shields.io/badge/Python-3.13-blue)
![Flask](https://img.shields.io/badge/Flask-2.x-orange)
![MongoDB](https://img.shields.io/badge/MongoDB-5.x-green)

## Description

This project predicts the species of an Iris flower (**Setosa, Versicolor, Virginica**) based on its **sepal length, sepal width, petal length, and petal width**.
It uses a **Random Forest Classifier** trained on the Iris dataset stored in **MongoDB**. The trained model is saved as `iris_model.pkl` and used in a **Flask web application** for live predictions.
All data for training and testing is fetched from MongoDB, demonstrating integration between a **NoSQL database** and machine learning workflows.

## MongoDB Integration

The Iris dataset is stored in a MongoDB collection called `iris` inside the `irisDB` database. Each document has the following structure:

```json
{
  "_id": ObjectId("..."),
  "sepal": {"length": 5.1, "width": 3.5},
  "petal": {"length": 1.4, "width": 0.2},
  "variety": "Setosa"
}
```

**Sample MongoDB connection in Python:**

```python
from pymongo import MongoClient

# Connect to local MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["irisDB"]
collection = db["iris"]

# Fetch data
data = list(collection.find())
```

## Project Structure

```
IRISML/
│
├── templates/
│   └── iris.html        # HTML form for prediction
├── train_model.py       # Script to train the model (fetches data from MongoDB)
├── app.py               # Flask application for live predictions
├── iris_model.pkl       # Saved trained model
├── iris.csv             # Optional dataset (if you want offline CSV)
├── requirements.txt     # Required Python packages
```

## Installation

1. Clone the repository:

```bash
git clone <your-repo-url>
cd IRISML
```

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

4. Make sure MongoDB is running locally or update the connection string in `train_model.py` and `app.py` accordingly.

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
